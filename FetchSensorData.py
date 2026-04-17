import paho.mqtt.client as mqtt
import mysql.connector
import time
from datetime import datetime
import json

# Zugangsdaten MQTT
server = "broker.hivemq.com"
topic= "efi124/projekt/sensor"

# Zugangsdaten MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="efi124",
    password="",
    database="sensor_data"
)

def save_to_db(data):
    mycursor = mydb.cursor()
    sql = "INSERT INTO measurements (temperature, humidity, pressure, altitude, timestamp) VALUES (%s, %s, %s, %s, %s)"
    val = (data['temperature'], data['humidity'], data['pressure'], data['altitude'], data['timestamp'])
    mycursor.execute(sql, val)
    mydb.commit()

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(topic, 0)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    data['timestamp'] = datetime.fromtimestamp(data['timestamp']+ 946684800).strftime('%Y-%m-%d %H:%M:%S')
    print(f"Message received: {data}")
    save_to_db(data)
    print("Data saved to database")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect(server, 1883, 60)
client.loop_forever()