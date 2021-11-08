# hadoop 毕设流程



技术栈：Java、maven、hadoop、flask、前端知识



步骤

1. 搭建hadoop 分布式环境，hdfs 存储训练数据，MapReduce（MR）进行训练数据的协同过滤计算（搭了三台虚拟机）

|      | hadoop102                  | hadoop103                            | hadoop104                           |
| ---- | -------------------------- | ------------------------------------ | ----------------------------------- |
| HDFS | **NameNode**<br />DataNode | DataNode                             | **SecondaryNameNode**<br />DataNode |
| YARN | NodeManager                | **ResourceManager**<br />NodeManager | NodeManager                         |

2. 训练完数据交由服务器将推荐结果数据进行Topk 筛选展现给用户
3. 启动flask 服务器





