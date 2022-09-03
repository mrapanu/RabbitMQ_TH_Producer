import pika
import time
import board
import adafruit_dht
import json
from datetime import datetime

dhtDevice = adafruit_dht.DHT22(board.D27)

while True:
    try:
        # Print the values to the serial port
        temperature = dhtDevice.temperature 
        humidity = dhtDevice.humidity
        date = datetime.now()
        dt_string = date.strftime("%m/%d/%Y %H:%M:%S")
        body = {
                "room": "ROOM_1",
                "date": dt_string,
                "temperature": temperature,
                "humidity": humidity
               }

        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel() 
        channel.basic_publish(exchange='amqp_main_ex',
                      routing_key='rabbitkey',
                      body=json.dumps(body),
                      properties=pika.BasicProperties(
                          delivery_mode = 2, # make message persistent
                      ))
        print("[x] Sending data %r" % body)
        connection.close()
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(120.0)

