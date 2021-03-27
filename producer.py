"""
The main function of this program is to send generated data (data.py) to a Kakfa producer
running on 'KAFKA_HOST_IP:9092' and print out a copy of the data to the terminal.
"""

import json
import time
import random
import csv
from data import get_row
from kafka import KafkaProducer

# Replace kafka variables 
#TOPIC=TOPIC
#KAFKA_HOST_IP=KAFKA_HOST_IP

def json_serializer(data):
    """
    Callable function. Ensures JSON format persists through
    creation and during Kafka ingress/egress
    """ 

    return json.dumps(data).encode("utf-8")

# Instantiate Kafka Producer 
producer = KafkaProducer(
    bootstrap_servers = [f'{KAFKA_HOST_IP}:9092'], # ie. bootstrap-server-ip:9092   
    value_serializer=json_serializer # 
) 

if __name__ == "__main__":
    while True:
        row = get_row()
        for r in row:
            print(r)
            producer.send(f"{TOPIC}", r) # Kafka topic  
            random_int= random.uniform(1, 3)
            time.sleep(random_int)
