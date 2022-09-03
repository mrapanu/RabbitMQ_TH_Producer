# A basic RabbitMQ producer for temperature and humidity using DHT22 sensor

## 1. Setup on Raspberry Pi 4 / Raspberry Pi Zero 2W

###### 1.1 Install python3 and the libraries:
```
# apt install python3 python3-dev python3-pip -y
# python3 -m pip install --upgrade pip setuptools wheel
# python3 -m pip install pika --upgrade    // pika is the client for RabbitMQ
# pip3 install adafruit-circuitpython-dht 
# pip3 install --install-option="--force-pi" Adafruit_DHT  
```

###### 1.2 Wiring the Raspberry Pi with the DHT22 sensor:

! /img/wiring_pi_dht22.png

###### 1.3 Starting the producer:
```
# nohup python3 temperature_humidity_producer.py &
```

###### Note: the producers should start after the consumer is online