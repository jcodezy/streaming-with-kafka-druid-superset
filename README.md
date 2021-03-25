# A streaming data pipeline for real-time analysis using Apache (Kafka, Druid & Superset) and GCP
![architecture diagram](https://github.com/jcodezy/streaming-with-kafka-druid-superset/blob/master/assets/architecture-diagram-1.png)

## 1. Introduction
I wanted to use Apache Kafka, Druid, Superset and GCP to create real-time analytics pipeline. 

## 2. Setup
See the individual markdown files in this repo to get detailed instructions on how to get going. 
#### **The rest of this README.md assumes you have these components installed and ready to run altogether** 

## 2.Components
### Data Source: ACLED Data 
To simulate a stream of data, I downloaded a 2020 dataset from ACLED and created a generator, [data.py](https://github.com/jcodezy/streaming-with-kafka-druid-superset/blob/master/data.py) and [producer.py](https://github.com/jcodezy/streaming-with-kafka-druid-superset/blob/master/producer.py) file to send the data to Kafka. These are real events that happened in 2020, but for the purpose of this project, I changed the `timestamp` to time.now() to simulate events coming through in real time.
      
### 3. How to run components (in order) 
** See each component's markdown file on how to install each component. ** 

#### SSH into VM
```
# After downloading Google's SDK, run
gcloud compute ssh --project [PROJECT] --zone [ZONE] [GCP_USERNAME]@[GCP_VM_NAME] 
```
#### Start Zookeeper
`sudo /usr/local/zookeeper/apache-zookeeper-3.6.2-bin/bin/zkServer.sh start`
#### Start Druid nodes
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

#### Start Superset
#### Start ACLED data source stream 
### Kafka 
#### Running Kafka 
```

```

### Druid 


### Superset 
- add druid database                                      
