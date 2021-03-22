"""
The 'get_row' generator function is used in producer.py 
and streams out an "event", row by row from a large dataset
starting from 01-Jan-2020 to 31-Dec-2020.

Find more information on ACLED dataset at: 
https://acleddate.com
"""


import csv 
from datetime import datetime

def get_row():
    with open('dataset/2020-01-01-2020-12-31-FIXED.csv') as f:
        csv_reader = csv.reader(f, delimiter=',')
        next(csv_reader, None)
        for row in csv_reader:
            yield {
                "data_id" : row[0],
                "iso": row[1],
                "event_date": datetime.utcnow().strftime("%Y-%m-%d"),
                "year": datetime.now().strftime("%Y"),
                "event_type": row[8],
                "sub_event_type": row[9], 
                "actor1": row[10],
                "assoc_actor_1": row[11],
                "interaction": row[16],
                "region": row[17],
                "country": row[18],
                "admin1": row[19],
                "admin2": row[20],
                "admin3": row[21],
                "location": row[22],
                "latitude": row[23],
                "longitude": row[24],
                "source": row[26],
                "notes": row[28],
                "fatalities": row[29], 
                "timestamp": int(datetime.utcnow().timestamp())
            }
