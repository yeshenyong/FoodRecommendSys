# Hadoop 3.x 



Hadoop 1.x 组成：Common（辅助工具）、HDFS（数据存储）、MapReduce（计算+资源调度）

Hadoop 2.x 组成：Common（辅助工具）、HDFS（数据存储）、MapReduce（计算）、Yarn（资源调度）

Hadoop 3.x 组成：与2.x一样





## HDFS 架构概述

例子

> 200T 资料，一台电脑只有1T，不舍得资料。

将数据资料分别存储在多个机器上

那么数据都存储在什么位置？

NameNode：记录数据都存储在什么位置上

DataNode：具体存储数据

2NN：秘书，辅助NameNode的工作



### NameNode（nn）

存储文件的元数据，如文件名，文件目录结构，文件类型（生成时间、副本数、文件权限），以及每个文件的块列表和块所在的DataNode等



### DataNode（dn）

在本地文件系统存储文件块数据，以及块数据的校验和



### Secondary NameNode（2nn）

每隔一段时间对NameNode元数据备份



## YARN 架构概述

### ResourceManager（RM）

整个集群资源（内存、CPU等）的老大

### NodeManager（NM）

单个节点服务器资源老大

### ApplicationMaster（AM）

单个任务运行的老大

### Container

容器，相当一台独立的服务器，里面封装了任务运行所需要的资源，如内存、cpu、磁盘、网络等



说明1：客户端可以有多个

说明2：集群上可以运行多个ApplicationMaster

说明3：每个NodeManager上可以有多个Container

![image-20211030102600290](C:\Users\10505\AppData\Roaming\Typora\typora-user-images\image-20211030102600290.png)





## MapReduce 架构概述

根据请求找到所需的文件位置并返回给请求端



## 推荐系统项目框架

![image-20211030103705483](C:\Users\10505\AppData\Roaming\Typora\typora-user-images\image-20211030103705483.png)







## hadoop 目录结构



**bin：**

**etc：**

lib：

include：C语言头文件

native：动态链接库

libexec：

**sbin：命令服务**

share：学习资料，说明文档





scp：用于拷贝

rsync：远程同步工具，用rsync做文件的复制要比scp的速度快，rsync只对差异文件做更新。scp是把所有文件都复制过去

```shell
rsync -av ./hadoop yeshenyong@hadoop104:/opt/module/
```



xsync 集群分发脚本（自己手写全局命令脚本）



```shell
#!/bin/bash

#1. 判断参数个数
if [ $# -lt 1 ]
then
        echo Not Enough Arguement!
        exit;
fi

#2. 遍历集群所有机器
for host in hadoop102 hadoop103 hadoop104
do
        echo =======================  $host  ======================= 
        #3. 遍历所有目录，挨个发送

        for file in $@
        do
                #4. 判断文件是否存在
                if [ -e $file ]
                        then
                                #5. 获取父目录
                                pdir=$(cd -P $(dirname $file); pwd)

                                #6. 获取当前文件名称
                                fname=$(basename $file)
                                ssh $host "mkdir -p $pdir"
                                rsync -av $pdir/$fname $host:$pdir
                        else
                                echo $file dose not exits!
                fi
        done
done
```



ln -s aaa bbb

cd -P aaa

进入aaa 的软链接文件下





## ssh免密登录



hadoop102 生成密钥对，把公钥给所要ssh连接的服务器

```sh
ssh-keygen -t rsa
```



```
ssh-copy-id hadoop103
```

即可



## Hadoop 集群配置



|      | hadoop102                  | hadoop103                            | hadoop104                           |
| ---- | -------------------------- | ------------------------------------ | ----------------------------------- |
| HDFS | **NameNode**<br />DataNode | DataNode                             | **SecondaryNameNode**<br />DataNode |
| YARN | NodeManager                | **ResourceManager**<br />NodeManager | NodeManager                         |

注意

- NameNode 和 SecondaryNameNode 不要安装在同一台服务器
- ResourceManager 也很消耗内存，不要和NameNode、SecondaryNameNode 配置在同一台机器上



## Hadoop 配置文件

Hadoop 配置文件分两类：默认配置文件和自定义配置文件，只有用户想修改某一默认值时，才需要修改自定义配置文件，更改相应属性值

（1）默认配置文件

| 要获取的默认文件     | 文件存放在Hadoop的jar包中的位置                        |
| -------------------- | ------------------------------------------------------ |
| [core-default.xml]   | hadoop-common-3.1.3.jar/core-default.xml               |
| [hdfs-default.xml]   | hadoop-hdfs-3.1.3.jar/hdfs-default.xml                 |
| [yarn-default.xml]   | hadoop-yarn-common-3.1.3.jar/yarn-default.xml          |
| [mapred-default.xml] | hadoop-mapred-client-core-3.1.3.jar/mapred-default.xml |



（2）自定义配置文件：

core-site.xml、hdfs-site.xml、yarn-site.xml、mapred-site.xml 四个配置文件存放在$HADOOP_HOME/etc/hadoop 这个路径上，用户可以根据项目需求重新进行修改配置



core-site.xml

```xml
<configuration>
<!-- 指定NameNode的地址 -->
<property>
  <name>fs.defaultFS</name>
  <value>hdfs://hadoop102:8020</value>
</property>
<!-- 指定hadoop数据的存储目录 -->
<property>
  <name>hadoop.tmp.dir</name>
  <value>/opt/module/hadoop-3.1.3/data</value>
</property>
</configuration>
```



hdfs-site.xml

```xml
<configuration>

<!-- nn web 端访问地址-->

<property>

<name>dfs.namenode.http-address</name>
<value>hadoop102:9870</value>

</property>

<!-- 2nn web 端访问地址 -->
<property>

<name>dfs.namenode.secondary.http-address</name>
<value>hadoop104:9868</value>

</property>

</configuration>
```



yarn-site.xml

```xml
<configuration>

<!-- Site specific YARN configuration properties -->

<!-- 指定MR走shuffle -->
<property>
<name>yarn.nodemanager.aux-services</name>
<value>mapreduce_shuffle</value>
</property>

<!-- 指定ResouceManager的地址 -->
<property>
<name>yarn.resourcemanager.hostname</name>
<value>hadoop103</value>
</property>

<!-- 环境变量的继承 -->
<property>
<name>yarn.nodemanager.env-whitelist</name>
<value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME</value>
</property>

</configuration>
```



mapred-site.xml 

```xml
<configuration>
<!-- 指定MapReduce 程序运行在YARN上 -->
<property>
<name>mapreduce.framework.name</name>
<value>yarn</value>
</property>
</configuration>
```





### 启动集群

hadoop2

```sh
hdfs namenode -format
sbin/start-dfs.sh
jps # 检验
```



```
yeshenyong@hadoop102-hadoop-3.1.3$ /opt/module/hadoop-3.1.3/sbin/start-dfs.sh
yeshenyong@hadoop103-hadoop-3.1.3$ /opt/module/hadoop-3.1.3/sbin/start-yarn.sh
```



### MR

```
hadoop jar /opt/module/hadoop-3.1.3/share/hadoop/mapreduce/MapReduce-1.0-SNAPSHOT.jar com.food.mapreduce.foodRecommend.ItemCFMain /food/input /food/tmp3 /food/tmp4 /food/output2

```



hadoop102:9870 上面download下来



## web页面暴露



Web端查看HDFS 的NameNode

- 浏览器输入：http://hadoop102:9870
- 查看HDFS上存储的数据信息



Web端查看YARN的ResourceManager

- 浏览器输入：http://hadoop103:8088
- 查看YARN上运行的Job信息





### 集群基本测试



集群停掉：先把yarn停掉、再去namenode停掉

```shell
jps
jpsall
```



## MapReduce

### map

Key,value 成output集合





### Reduce

每个key调用一次reduce，

如

key 1

key 1

=> key, 1, 1集合形式展现，迭代器for循环遍历



企业大部分在windows环境下进行开发，然后上传到Linux 服务器环境再进行下一步操作



## Debug 调试

https://www.bilibili.com/video/BV1Qp4y1n7EN?p=77

