* 安装MySQL
```bash
sudo apt-get install mysql-server
sudo apt-get isntall mysql-client
sudo apt-get install libmysqlclient-dev
```

* 安装python-dev
```bash
sudo apt-get install python-dev
```

* 虚拟环境中安装图像库
```bash
pip install pillow
```

* 虚拟环境中安装mysql-python
```bash
pip install MySQL-python
```

* 平台版本
    * django==1.8.4
    * python==2.7.4
    * pycharm==4.5.3 

* MySQL数据库设置
    * 新建数据库:
    ```bash
    create database misslovedb default charset=utf8;
    ```
    * 创建用户:
    ```bash
    create user 'testn'@'localhost' identified by '123456';
    ```
    * 添加权限:
    ```bash
    grant all privileges on misslovedb.* to 'testn'@'localhost';
    flush privileges;
    ```

*****
2015-08-31任务:

~~* 文章: 新建文章,查看文章内容,首页显示文章题目~~
~~* 评论: 新建评论,查看评论~~
~~* 用户: 用户注册，用户资料及显示用户发表过的文章和评论及管理,修改用户资料,~~ **实现鼠标悬停显示用户资料————未完成，等待……**

*追加思考*

* 文章: 可顶&踩,实现按浏览次数排序,按顶数排序
* 实现全局搜索,Redis缓存
* 网站介绍页面: 包括网站基本介绍,各版区数量百分比,用户恋爱状态百分比饼图……

******
2015年09月01日任务：

* 用户修改密码，实现富文本显示，Redis缓存，全局搜索
* 删除评论，发现并优化权限显示隐藏小细节，调好首页及个板块目录页，编辑评论，编辑文章



