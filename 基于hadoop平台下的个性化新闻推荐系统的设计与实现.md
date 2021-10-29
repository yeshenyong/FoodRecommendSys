# **基于hadoop平台下的个性化新闻推荐系统的设计与实现**



- 爬虫爬数据
- 建表建数据库
- 前后端搭建，展示页面
- hadoop 分布式数据库训练（hadoop 分配 + MapReduce 训练存储）
- 训练结果同步后端



- *Hadoop*框架中最核心设计就是：*HDFS*和*MapReduce*，*HDFS*实现存储，而*MapReduce*实现原理分析处理
- spark
- 



其中

​	MapReduce:Map操作主要是将一组键值对数据映射为一组 新的键值对数据，Reduce操作是归纳操作



- 推荐算法
- 用户画像（个性化）
- 召回策略
- 排序算法
- 



​	模型更新功能又被划分为：读取训练数据功能、训练模型功能与保存模型功 能。其中读取训练数据功能是从`HDFS`上获取训练样本生成功能产出训练样本到系统中；训练模型的功能首先使用机器学习算法对用户一新闻一点击率进行建模，确定预测模型，在确定模型求解方法即最优化算法，在这些都实现的前提下对模型进行求解，并实时获取模型Auc与Loss确定何时结束训练；保存模型功能是将模 型参数保存到HDFS为下次模型训练做支持。



1. 数据集（爬虫 or 网上数据集，80%用于训练，20%用于预测）
2. hadoop 分布式数据集分配 + 计算（多个节点不同数据量之间的对比）
3. recall 召回率体现





### hadoop

 Namenode、Datanode

*NameNode*：保存整个文件系统的目录信息、文件信息及分块信息，这是由唯一一台主机专门保存，当然这台主机如果出错，*NameNode*就失效了。**在*Hadoop2.开始支持*activity-standy*模式*----*如果主*NameNode*失效，启动备用主机运行*NameNode**。

*DataNode*：分布在廉价的计算机上，用于存储*Block*块文件。

*Block*：将一个文件进行分块，通常是*64M*。

![img](https://img-blog.csdn.net/20151123230919155?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)



*Namenode*全权管理数据块的复制，它周期性地从集群中的每个*Datanode*接收心跳信号和块状态报告*(Blockreport)*。接收到心跳信号意味着该*Datanode*节点工作正常。块状态报告包含了一个该*Datanode*上所有数据块的列表。*Namenode*全权管理数据块的复制，它周期性地从集群中的每个*Datanode*接收心跳信号和块状态报告*(Blockreport)*。接收到心跳信号意味着该*Datanode*节点工作正常。块状态报告包含了一个该*Datanode*上所有数据块的列表。





- 周期性（maybe一天训练一次数据，训练结果保存在）
- 

