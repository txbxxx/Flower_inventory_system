# Flower-_inventory_system

````
 注意本项目使用的虚拟环境，欢迎大家提意见2865260231@qq.com`
````

#### 方法1

1.使用git或者下载ZIP到本地

```
git clone https://github.com/txbxxx/Flower_inventory_system
```

2.解压文件后直接打开虚拟环境，需要修改一下文件

```
#pyvenv.cfg

home = C:\Program Files\python  #修改为当前系统Python的主目录
include-system-site-packages = false
version = 3.8.6	#修改为当前系统Python版本
```

```
#active文件再虚拟环境中的Script目录下

......
VIRTUAL_ENV="......" #修改为当前项目的目录绝对地址
export VIRTUAL_ENV
```

3.启动虚拟环境运行django服务
