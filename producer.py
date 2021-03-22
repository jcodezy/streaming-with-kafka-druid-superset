"""
The main function of this program is to send generated data (data.py) to a Kakfa producer
running on 'SOME.HOST.IP:9092' and print out a copy of the data to the terminal.
"""

import json
import time
import random
import csv
from data import get_row
from kafka import KafkaProducer

def json_serializer(data):
    """
    Callable function. Ensures JSON format persists through
    creation and during Kafka ingress/egress
    """ 

    return json.dumps(data).encode("utf-8")

# Instantiate Kafka Producer 
producer = KafkaProducer(
    bootstrap_servers = ['<SOME.HOST.IP>:9092'], # bootstrap-server-ip:9092   
    value_serializer=json_serializer # 
) 

if __name__ == "__main__":
    while True:
        row = get_row()
        for r in row:
            print(r)
            producer.send("{TOPIC}", r) # TOPIC to send messages to  
            random_int= random.uniform(1, 3)
            time.sleep(random_int)
