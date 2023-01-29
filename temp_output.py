#!/usr/bin/python
import sys
import csv
import time
import os

from datetime import datetime

import Adafruit_DHT

interval = 5

columns = ["date", "time", "temperature", "humidity"]

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11,4)

    current_dateTime = datetime.now()
    current_date = current_dateTime.strftime("%Y-%m-%d")
    current_time = current_dateTime.strftime("%H:%M:%S")
    new_row = [current_date, current_time, temperature, humidity]

    if os.path.exists("temperatures_basement.csv"):
        csvfile =  open("temperatures_basement.csv", "a", newline="")
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(new_row)
        csvfile.close()

    else:
        csvfile = open("temperatures_basement.csv", "w", newline="")
        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(columns)
        csvwriter.writerow(new_row)

        csvfile.close()


    print(humidity)
    print(temperature)
    

    time.sleep(interval)
