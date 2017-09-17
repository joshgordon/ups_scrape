#!/usr/bin/env python2
from influxdb import InfluxDBClient
import paho.mqtt.client as mqtt
import datetime

mappings = {'load_w': 'power', 'supply_v': 'voltage', 'battery': 'percent', 'battery_v': 'battery_voltage'}

def on_connect(client, userdata, flags, rc):
    print ("Connected with result code {}".format(rc))
    client.subscribe("gordon/smarthouse/ups/office/#")


def on_message(client, userdata, msg):
    try:
        value = float(msg.payload.decode('utf-8'))
    except:
        return
    kind = msg.topic.split('/')[-1]
    if kind in mappings:
        kind = mappings[kind]
    body=[{
        "measurement": kind,
        "time": datetime.datetime.utcnow().isoformat(),
        "fields": {
            "value": value
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
