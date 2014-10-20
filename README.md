Rabbit_battle
=============

主要由以下几个部分组成：

rabbit{arrow，bullet，AI}

terrain

client

server

规则（初始）：

1、不能跑出地图外

2、射箭间隔最短为1s

3、初始为100血，受到攻击每次掉10滴，等于或小于0时死亡

4、幸存者获胜

规则（可选）：

1、加入战争迷雾机制，即一般情况下一方无法看到任何东西（或者只有一定的可视范围）

2、当使用照明弹的时候，所有兔子都可以看到对方，1s或2s后使用照明弹的一方还能获取一次对方的位置


代码编写:

主要部分采用面向对象来写，包括rabbit,terrain,arrow,bullet，AI几个部分

client和server采用面向过程来写，暂时不确定并发多线程是否要用gevent来写

其中地图和兔子以及一些动画效果采用pygame库来写

2014.10.17日更新：
重新改写了rabbit,bullet,terrain类，将一些通用的数据放入类的静态变量中
去除了原来的arrow类
重写了测试文件，现在为test_only中
note：python中变量名其实特么是指针！如果是要变量相互赋值的话要用copy.deepcopy()！坑得一腿！


2014.10.18日更新：
1、完成了Rabbit的move函数，增加了Rabbit的移动速度为5
2、添加了server.py和client.py两个文件（未完成）
3、添加了用于rabbit信息交互的消息模板文件rabbit.proto(还不完善)
4、测试文件现在可运行射击等简单示例
5、目前打算是server负责维护数据和交互，client用户呈现，AI相对独立（这个暂未想好）

protobuf使用：
下好包后解压，然后在python文件夹中运行python setup.py build,成功后再运行python setup.py install
安装成功后用protoc.exe文件编译写好的proto文件，然后运行protoc filename.proto --python_out /outputdir
成功后会在指定的文件夹下产生一个py文件


2014.10.20日更新
1、稍微完善了rabbit.proto的定义
2、修改了server和client的思路，现在分为server(client)和manage两个类，manage负责连接，server(client)负责数据交互，并且使用gevent并发
3、增加了base_server.py基类，用于提供基本的数据操作
4、增加了message.py文件，用户对数据进行封装