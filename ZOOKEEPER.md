## Zookeeper 
Zookeeper is both a Kafka AND Druid dependency. Zookeeper can be installed on its own
server, but we'll install Zookeeper on the the Druid Master node. 

#### Druid and Kafka cannot start without Zookeeper; make sure to run Zookeeper before starting Druid and Kafka processes.

### Installing Zookeeper
#### SSH into node where Zookeeper will be installed and run
```
# Download Zookeeper
wget https://httpd-mirror.sergal.org/apache/zookeeper/zookeeper-3.6.2/apache-zookeeper-3.6.2-bin.tar.gz
tar -xzf https://httpd-mirror.sergal.org/apache/zookeeper/zookeeper-3.6.2/apache-zookeeper-3.6.2-bin.tar.gz

# Create folder and move zookeeper
sudo mkdir -p /usr/local/zookeeper
sudo mv zookeeper-3.6.2 /usr/local/zookeeper

# Create folder for dataDir
sudo mkdir -p /var/lib/zookeeper

# Create config file if it does not exist in /zookeeper/conf/zoo.cfg
sudo vim /usr/local/zookeeper/conf/zoo.cfg

# Add properties inside config file
tickTime=2000
dataDir=/var/lib/zookeeper
clientPort=2181
```


 
