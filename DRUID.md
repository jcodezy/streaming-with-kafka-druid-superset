# DRUID Clustered Deployment

#### Note:
I chose to deploy a Druid cluster versus the standalone setup to try and resemble a 
Production implementation of a cluster on GCP. Additionally, Druid demands a lot of CPU/RAM
if run locally but it is possible to tune this if you know what you're doing. 
If you want to run locally, you can do this by customizing the JMX/max heap sizes in 
`conf/druid/cluster/_common/common.server.properties`. 

## GCP Druid Cluster
Google Cloud Compute VMs 
#### 1. "druid-master-1": 
* This server contains Druid's Coordinator and Overlord processes and they are in charge of handling Druid's metadata and coordination
needs of the cluster.
* e2-custom (2vCPUs, 5.5GB memory)
#### 2. "druid-query-1":
* Druid brokers inside the query server accept queries and farm them out to the rest of the cluster. 
* e2-standard-4 (4 vCPUs, 16 GB memory)
#### 3. "druid-data-1":
* Druid Historicals and MiddleManagers in this server handle the ingested data in the cluster. 
* e2-custom (2 vCPUs, 13.25 GB memory)

## Setting up Druid 
#### SSH into each server node
`gcloud compute ssh --project [PROJECT_NAME] --zone [ZONE] [SERVER_NODE_NAME]`
 
### For each of the three servers, complete Druid setup
```
# Download Druid 
wget https://mirror.dsrg.utoronto.ca/apache/druid/0.20.1/apache-druid-0.20.1-bin.tar.gz
tar -xzf https://mirror.dsrg.utoronto.ca/apache/druid/0.20.1/apache-druid-0.20.1-bin.tar.gz

# Update libraries
sudo apt-get update

# Java JDK
# Ensure you have JDK 8 or higher 
sudo apt install default-jdk -y 

# Install Perl
sudo apt-get install perl -y 

# Install Postgres for metadata
sudo apt install postgres

```

## common.runtime.properties
### Important Note: the common.runtime.properties file across all druid nodes should be the SAME. Make one copy and replace the existing common.runtime.properties in each node.
Find the config file inside `apache-druid-0.20.1/conf/druid/cluster/_common/`
or  
`sudo vim apache-druid-0.20.1/conf/druid/cluster/_common/common.runtime.properties`

And replace the following:
```
# Add Kafka & Postgres to Druid's extensions list
druid.extensions.loadList=["druid-google-extensions", "postgres-metadata-storage", "druid-datasketches", "druid-kafka-indexing-service"]

# Update IP to the server/node internal IP where this is installed;
druid.host=[YOUR.HOST.IP] # internal ip of VM instance  

# Zookeeper service host ip (where Zookeeper is installed -- Master, in this case)
druid.zk.service.host=[ZOOKEEPER.IP]

# Postgres Metadata
druid.metadata.storage.type=postgres
druid.metadata.storage.connector.host=[POSTGRES.IP]
druid.metadata.storage.connector.connectURI=jdbc:postgresql://localhost:5432/druid
druid.metadata.storage.connector.user=druid
druid.metadata.storage.connector.password=password1

# For GCS Storage:
druid.storage.type=google
druid.google.bucket=[YOUR_BUCKET_NAME]
druid.google.prefix=[YOUR_BUCKET_NAME]/segments

# Indexing Service Logs
druid.indexer.logs.type=google
druid.indexer.logs.bucket=[YOUR_BUCKET_NAME]
druid.indexer.logs.prefix=[YOUR_BUCKET_NAME]/indexing-logs

#Creating authenticator
druid.auth.authenticatorChain=["MyBasicMetadataAuthenticator"]

druid.auth.authenticatorChain=["MyBasicMetadataAuthenticator"]
druid.auth.authenticator.MyBasicMetadataAuthenticator.type=basic
druid.auth.authenticator.MyBasicMetadataAuthenticator.initialAdminPassword=password1
druid.auth.authenticator.MyBasicMetadataAuthenticator.initialInternalClientPassword=password2
druid.auth.authenticator.MyBasicMetadataAuthenticator.credentialsValidator.type=metadata
druid.auth.authenticator.MyBasicMetadataAuthenticator.skipOnFailure=false
druid.auth.authenticator.MyBasicMetadataAuthenticator.authorizerName=MyBasicMetadataAuthorizer

druid.auth.authenticator.MyBasicMetadataAuthenticator.enableCacheNotifications=true
druid.auth.authenticator.MyBasicMetadataAuthenticator.cacheNotificationTimeout=5000
druid.auth.authenticator.MyBasicMetadataAuthenticator.credentialIterations=10000

#Escalator
druid.escalator.type=basic
druid.escalator.internalClientUsername=druid_system
druid.escalator.internalClientPassword=password2
druid.escalator.authorizerName=MyBasicMetadataAuthorizer

#Creating Authorizer chequear
druid.auth.authorizers=["MyBasicMetadataAuthorizer"]
druid.auth.authorizer.MyBasicMetadataAuthorizer.type=basic
druid.auth.authorizer.MyBasicMetadataAuthorizer.enableCacheNotifications=true
druid.auth.authorizer.MyBasicMetadataAuthorizer.cacheNotificationTimeout=5000
```
#### See `examples/common.runtime.properties` of this repo for the full example.  
