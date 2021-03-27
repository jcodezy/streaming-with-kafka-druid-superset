# A streaming data pipeline for real-time analysis using Apache (Kafka, Druid & Superset) and GCP
![architecture diagram](https://github.com/jcodezy/streaming-with-kafka-druid-superset/blob/master/assets/architecture-diagram-1.png)

## About
I wanted to use Apache Kafka, Druid, Superset and GCP to create real-time analytics pipeline.   

## Requirements
* GCP account and at least three nodes (note: the Druid data node requires at minimum 8gb of RAM unless you edit configurations in config files)

## Setup 
See the individual markdown files in this repo to get detailed instructions on how to get going, starting with Druid. 
#### **The rest of this README.md assumes you have these components installed and ready to run altogether** 

### Data Source: ACLED Data 
To simulate a stream of data, I downloaded a 2020 dataset from ACLED and created a generator, [/data.py](https://github.com/jcodezy/streaming-with-kafka-druid-superset/blob/master/data.py) and [/producer.py](https://github.com/jcodezy/streaming-with-kafka-druid-superset/blob/master/producer.py) file to send the data to Kafka. These are real events that happened in 2020, but for the purpose of this project, I changed the `timestamp` to time.now() to simulate events coming through in real time.
      
## Running the components
**See each component's markdown file on how to install each component.** 

#### How to SSH into VM
```
# After downloading Google's SDK, run
gcloud compute ssh --project [PROJECT] --zone [ZONE] [GCP_USERNAME]@[GCP_VM_NAME] 
```
#### Start Zookeeper
Zookeeper needs to start before Druid and Kafka/ 
```
# SSH into Zookeeper node
sudo /usr/local/zookeeper/apache-zookeeper-3.6.2-bin/bin/zkServer.sh start
```
#### Start Druid cluster
``` 
# SSH into Master node and run
sudo apache-druid-0.20.1/bin/start-cluster-master-no-zk-server

# SSH into Data node and run
sudo apache-druid-0.20.1/bin/start-cluster-data-server

# SSH into Query node and run
sudo apache-druid-0.20.1/bin/start-cluster-query-server
```
#### Druid UI
Access Druid's web UI by going into a browser and entering
```
# replace IP with the query node external IP
[IP]:8888
```

#### Start Kafka
```
# SSH into Kafka node and run
sudo kafka_2.13-2.7.0/bin/kafka-server-start config/server.properties 
```

#### Start Superset
```
# SSH into Superset if Superset is on a node; run
superset run -h 0.0.0.0 -p 8088 --with-threads --reload --debugger
``` 
#### Access Superset's UI 
Go to a browser and run `[SUPERSET_NODE_IP]:8088`

#### Add Druid as a database in Superset
`admin` and `password1` defined in Druid's basic security authentication protocol; defined in the common.runtime.properties config file in each Druid node.  
Add `druid://admin@password1@[DRUID_QUERY_IP]:8888` in Superset's database page. 

                        
