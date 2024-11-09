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
python3 manage.py makemigrations
python3 manage.py migrate
```
4. 创建超级用户
```bash
python3 manage.py createsuperuser
```
5. 运行
```bash
python3 manage.py runserver
```

### API 接口说明
- 获取随机句子：`GET /yiyan/get/`
- 管理界面：`/yiyan/admin/`
- RESTful API：
  - 获取所有句子：`GET /yiyan/sentences/`
  - 添加新句子：`POST /yiyan/sentences/`
  - 更新句子：`PUT /yiyan/sentences/{id}/`
  - 删除句子：`DELETE /yiyan/sentences/{id}/`