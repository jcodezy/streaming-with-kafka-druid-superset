# A streaming data pipeline for real-time analysis using Apache (Kafka, Druid & Superset) and GCP
![architecture diagram](https://github.com/jcodezy/streaming-with-kafka-druid-superset/blob/master/assets/architecture-diagram-1.png)

## About
I wanted to use Apache Kafka, Druid, Superset and GCP to create real-time analytics pipeline. ACLED is a data aggregatorof real events around the world involving conflict and forms of civil unrest. This project is to show how a data pipeline could be used to ingest that data and create real-time analytics that could be used for critical decision-making versus moving data in batch fashion.    

More information on ACLED can be found [HERE](https://acleddata.com/#/dashboard)

## Requirements
* GCP account
* Minimum three nodes (note: the Druid data node requires at minimum 8gb of RAM unless you edit configurations in config files) 

### Data Source: ACLED Data 
To simulate a stream of data, I downloaded a 2020 dataset from ACLED and created a generator, [/data.py](https://github.com/jcodezy/streaming-with-kafka-druid-superset/blob/master/data.py) and [/producer.py](https://github.com/jcodezy/streaming-with-kafka-druid-superset/blob/master/producer.py) file to send the data to Kafka. These are real events that happened in 2020, but for the purpose of this project, I changed the `timestamp` to time.now() to simulate events coming through in real time.
      
## Starting the components
**See markdown file for zookeeper, druid, kafka and superset and install each component first, starting with druid.** 

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

# Access Druid's web UI by going into a browser and entering
QUERY_NODE_IP:8888 # query node's external IP

# Sign in with username:'druid_system' and pwd:password2 as defined in:
# /config/druid/cluster/_common/common.runtime.properties  
```

#### Start Kafka server and create Topic 
```
# SSH into Kafka node and run
sudo kafka_2.13-2.7.0/bin/kafka-server-start config/server.properties 

# Create Kafka Topic
sudo kafka_2.13-2.7.0/bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic SOME_TOPIC_NAME 
```

#### Superset login and adding a database
```
# SSH into Superset if Superset is on a node; run
superset run -h 0.0.0.0 -p 8088 --with-threads --reload --debugger

# Access Superset's UI; go to a browser and run 
[SUPERSET_NODE_IP]:8088

# Sign in with username & password as defined at Superset installation

# Go to data > databases > add database and add
druid://admin@password1@[DRUID_QUERY_IP]:8888 
``` 

## Connecting Kafka & Druid 
In the Druid UI, select Load Data > Kafka and fill out the following 
![kafka-druid-spec](https://github.com/jcodezy/streaming-with-kafka-druid-superset/blob/master/assets/kafka-druid-spec.png)

## Starting data source 
#### Run producer.py
```
# Go to where producer.py file is and run
python3 producer.py
```
## producer.py inside Kafka consumer
![kafka-consumer-gif](https://github.com/jcodezy/streaming-with-kafka-druid-superset/blob/master/assets/kafka-consumer.gif)









