# 我的API仓库

## 一言API

一个随机返回精选句子的API服务

### 使用方法
1. 安装依赖
```bash
pip install -r requirements.txt
```
2. 创建`logs`目录
```bash
mkdir logs
```
3. 迁移数据库
```bash
python manage.py makemigrations
python manage.py migrate
```
3. 收集静态文件
```bash
python manage.py collectstatic
```
4. 创建超级用户
```bash
python manage.py createsuperuser
```
4. 运行
```bash
python manage.py runserver
```