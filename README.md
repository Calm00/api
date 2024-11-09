# 我的API仓库

## 一言API

一个随机返回精选句子的API服务

### 使用方法
1. 安装依赖
```bash
pip install -r requirements.txt
```
2. 迁移数据库
```bash
python manage.py makemigrations
python manage.py migrate
```
3. 创建超级用户
```bash
python manage.py createsuperuser
```
4. 运行
```bash
python manage.py runserver
```