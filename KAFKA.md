# Kafka 

#### Note: 
I set up Kafka on the Master node, but feel free to download and run locally as steps are
pretty much identical until you start pointing/referencing IPs for Kafka to work with.  

### Setting up Kafka on VM
```
# ssh into node where you want Kafka installed
gcloud compute ssh --project [PROJECT_NAME] --zone [ZONE] username@server_name # example: jcodezy@vm-server-name 

# download kafka 
wget https://httpd-mirror.sergal.org/apache/kafka/2.7.0/kafka-2.7.0-src.tgz 
tar -xzf https://httpd-mirror.sergal.org/apache/kafka/2.7.0/kafka-2.7.0-src.tgz
```

### Kafka's bootstrap-server
The following will setup Kafka's server process by referencing an ip:port known as the Kafka Broker.
If you've set up a GCP VM, then 'advertised_listeners' will be that of the VMs external IP. The 
default port for Kafka is 9092...so in essence: advertised_listeners=[VM_EXTERNAL_IP]:9092 

#### Find `advertised.listeners' in kafka-2.7.0/config/server.properties
```
# Change advertised listeners
advertised.listeners=PLAINTEXT://[VM_EXTERNAL_IP]:9092

# Note that you can tune and play around with Kafka's default settings 
# inside this file too (ie. partitions, replications, etc)
```
