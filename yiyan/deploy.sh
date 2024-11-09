#!/bin/bash

# 确保脚本在错误时停止
set -e

echo "开始部署一言API项目..."

# 安装系统依赖
echo "正在安装系统依赖..."
sudo apt update
sudo apt install -y python3-pip python3-venv mariadb-server nginx

# 创建项目目录
echo "创建项目目录..."
sudo mkdir -p /var/www/yiyan
sudo chown -R $USER:$USER /var/www/yiyan

# 复制项目文件
echo "复制项目文件..."
sudo mkdir -p logs
cp -r ./* /var/www/yiyan/

# 创建虚拟环境
echo "创建并激活虚拟环境..."
cd /var/www/yiyan
python3 -m venv venv
source venv/bin/activate

# 安装项目依赖
echo "安装项目依赖..."
pip install -r requirements.txt

# 创建日志目录
echo "创建日志目录..."
mkdir -p logs
chmod 755 logs

# 配置 MySQL
echo "配置 MySQL..."
sudo mysql -e "CREATE DATABASE IF NOT EXISTS yiyan CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
sudo mysql -e "CREATE USER IF NOT EXISTS 'yiyan'@'localhost' IDENTIFIED BY 'mysql@yiyan2006';"
sudo mysql -e "GRANT ALL PRIVILEGES ON yiyan.* TO 'yiyan'@'localhost';"
sudo mysql -e "FLUSH PRIVILEGES;"

# Django 数据库迁移
echo "执行数据库迁移..."
python3 manage.py makemigrations
python3 manage.py migrate

# 收集静态文件
echo "收集静态文件..."
python3 manage.py collectstatic --noinput

# 创建 Gunicorn 服务文件
echo "配置 Gunicorn 服务..."
sudo tee /etc/systemd/system/gunicorn_yiyan.service << EOF
[Unit]
Description=gunicorn daemon for yiyan
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/yiyan
ExecStart=/var/www/yiyan/venv/bin/gunicorn --config gunicorn.conf.py yiyan.wsgi:application

[Install]
WantedBy=multi-user.target
EOF

# 设置权限
echo "设置文件权限..."
sudo chown -R www-data:www-data /var/www/yiyan
sudo chmod -R 755 /var/www/yiyan

# 启动服务
echo "启动服务..."
sudo systemctl daemon-reload
sudo systemctl enable gunicorn_yiyan
sudo systemctl start gunicorn_yiyan

echo "部署完成！"
echo "请执行以下命令创建超级用户："
echo "cd /var/www/yiyan && source venv/bin/activate && python manage.py createsuperuser" 