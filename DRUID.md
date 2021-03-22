# DRUID Clustered Deployment

#### Note:
I chose to deploy a Druid cluster versus the standalone setup to try and resemble a 
Production implementation of a cluster on GCP. Additionally, Druid demands a lot of CPU/RAM
if run locally but it is possible to tune this if you know what you're doing. 
If you want to run locally, you can do this by customizing the JMX/max heap sizes in 
`conf/druid/cluster/_common/common.server.properties`. 

### GCP Druid Cluster
#### Google Cloud Compute VMs 
1. "druid-master-1": 
* This server contains Druid's Coordinator and Overlord processes and they are in charge of handling Druid's metadata and coordination
needs of the cluster.
* e2-custom (2vCPUs, 5.5GB memory)
2. "druid-query-1":
* Druid brokers inside the query server accept queries and farm them out to the rest of the cluster. 
* e2-standard-4 (4 vCPUs, 16 GB memory)
3. "druid-data-1":
* Druid Historicals and MiddleManagers in this server handle the ingested data in the cluster. 
* e2-custom (2 vCPUs, 13.25 GB memory)



 
 
