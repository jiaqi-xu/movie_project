# movie_project

Mac OS 环境搭建
1. python3.6： https://www.python.org/
2. mysql5.6（集成工具MAMP）： https://www.mamp.info
   -命令行找不到路径问题：添加环境变量到 ~/.bash_profile
    export PATH=$PATH:/Applications/MAMP/Library/bin
3. pycharm
4. 安装虚拟环境：pip3 install virtualenv


Virtualenv的使用
1. 创建虚拟环境：virtualenv -p /usr/local/bin/python3 movie_project （因为当时mac上既有python3，也有python2，该命令是为了创建python3的虚拟环境）
2. 激活虚拟环境：source movie_project/bin/activate
3. 退出虚拟化环境：deactivate

Flask的安装
1. 安装前检测: pip3 freeze
2. 安装flask: pip3 install flask
3. 安装后检测： pip3 freeze

微电影网站：

— 前台模块(home)：
	— 数据模型： models.py
	— 表单处理： home/forms.py
	— 模版目录： templates/home
	— 静态目录： static 

— 后台模块(admin):
	— 数据模型： models.py
	— 表单处理： admin/forms.py
	— 模版目录： templates/admin
	— 静态目录： static

前后台项目目录分析：
manager.py          		入口启动脚本
app		     			项目app
	__init__.py			初始化文件
	models.py		数据模型文件
	static			静态目录
	home/admin		前台／后台模块
		__init__.py		初始化脚本
		views.py		视图处理文件
		forms.py		表单处理文件
	templates			模版目录
		home/admin	前台／后台模版


