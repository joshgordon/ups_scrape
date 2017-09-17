#!/usr/bin/env python2
from influxdb import InfluxDBClient
import json
import paho.mqtt.client as mqtt
import datetime

# sensor names to table names in influx
mappings = {'28ff2583581644a': 'temp1', '28ffb43a51164bc': 'temp2'}

def CtoF(tempC):
    return (9/5.0) * tempC + 32


def on_connect(client, userdata, flags, rc):
    print ("Connected with result code {}".format(rc))
    client.subscribe("gordon/smarthouse/temp/#")


def on_message(client, userdata, msg):
    try:
        temp = float(msg.payload.decode('utf-8'))
    except:
        return
    sensor = msg.topic.split('/')[-1]
    if sensor in mappings:
        sensor = mappings[sensor]
    body=[{
        "measurement": sensor,
        "time": datetime.datetime.utcnow().isoformat(),
        "fields": {
            "value": CtoF(temp)
        }
    }]
    ifdb_client.write_points(body)
    print(body)

client = mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message

client.connect('mqtt.bluesmoke.network', 1883, 60)

ifdb_client = InfluxDBClient('localhost', 8086, database='grafana')
client.loop_forever()
