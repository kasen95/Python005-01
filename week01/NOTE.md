#开发前工作
##说明
1.python2和python3不完全兼容，注意项目版本选择；
2.官方文档：https://docs.python.org，了解版本差异化，新增特性，多阅读该文档；
3.安装目录不要有中文、空格、特殊字符，特别第三方库对以上支持较差；
4.多个Python共存时，在Terminal中输入python3，会在$PATH的环境目录中**按照顺序**去找python3匹配；
5.不建议删除系统自带的python2.7版本，自带了很多与系统交互的脚本；
6.pip安装的site-packages是与python版本相互关联的 

##pip
1.pip配置文件
安装路径：~/.pip/pip.conf，没有的话新建
配置文件格式:
```
[global]
index-url=https://pypi.tuna.tsinghua.edu.cn/simple
```

##虚拟环境
可理解为虚拟环境容器化：
一、虚拟环境创建
1.虚拟环境创建
python3.7 -m venv 项目目录
2.虚拟环境生效，激活
source 项目目录/bin/activate
3.which python3
python3指向该虚拟环境
4.deactivate
恢复成原始环境
5.退出项目目录后，就恢复成了系统环境

二、虚拟环境迁移
1.确保python、pip环境一致
2.激活虚拟环境
source 项目目录1/bin/activate
3.导出虚拟环境依赖包
pip3 freeze > requirements.txt
4.退出虚拟环境
deactivate
5.激活第2个环境的虚拟环境
source 项目目录2/bin/activate
6.确保python、pip环境一致
7.从虚拟环境1的requirements.txt安装依赖包到虚拟环境2
pip3 install -r ./requirements.txt
8.退出虚拟环境
deactivate

##python基础
###基本数据类型
1.查看字符串有哪些方法
str.capitalize查看
2.列表常用方法
append(),count(),insert(),reverse(),clear(),extend(),pop(),sort(),function(object)
3.列表和元组的区别
列表：动态，长度和元素可变，可增删改；
元组：静态，长度不可变，不可增删改；性能优于列表，存储空间不变，占用小，不需要加锁；
###高级数据类型
collections 容器数据类型
nametuple() 命名元组
deque 双端队列
Counter 计数器
OrderedDict 有顺序的字典
补充下字典的底层原理

###常用Python模块
1.time
time.localtime()
time.strftime("%Y-%m-%d %X",time,localtime())
2.datetime
3.logging
4.random
5.json
6.pathlib
7.os.path

###logging模块
更强大的功能，查阅python.doc
```
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("android_build")
```
###random模块
1.random()
2.randrange(0,100,2)
3.choice([list])
随机选取元素
4.sample([list],k=3)
随机抽取多个元素

###json模块
1.json.loads()
解码
2.json.dumps()
编码

###路径模块
工作上用了posixpath,可以看下pathlib用法，不推荐使用os.path（跨平台时不好用）

###守护进程
1.如何区分父进程和子进程
根据pid值判断，0为子进程；>0为父进程，返回值为创造出的子进程的pid；-1进程出错；









