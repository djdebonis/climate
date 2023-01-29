#!/usr/bin/python
import sys
import csv
import time
import os

from datetime import datetime
import Adafruit_DHT

#global variables

# time (in seconds) between temperature grabs
interval = 600

# column names for output file
columns = ["date", "time", "temperature", "humidity"]


def getData(sensor = 11, pin = 4):
    humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)

    return(humidity, temperature)



def read_temp_and_humidity(sensor = 11, pin = 4):
    temp_c, humidity = getData(sensor,pin)

    if temp_c:
        temp_f = temp_c * (9 / 5) + 32
        return round(temp_f, 2), round(humidity, 2)

    return None, None

def main():
        while True:

            temperature, humidity = read_temp_and_humidity(11,4)

            current_dateTime = datetime.now()
            current_date = current_dateTime.strftime("%Y-%m-%d")
            current_time = current_dateTime.strftime("%H:%M:%S")
            new_row = [current_date, current_time, temperature, humidity]

            # if there is already a .csv, don't rewrite columns
            if os.path.exists("temperatures_basement.csv"):
                # a for append
                csvfile =  open("temperatures_basement.csv", "a", newline="")
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(new_row)
                csvfile.close()

            # elif the path doesn't exist, make sure to write column names
            else:
                csvfile = open("temperatures_basement.csv", "w", newline="")
                csvwriter = csv.writer(csvfile)

                csvwriter.writerow(columns)
                csvwriter.writerow(new_row)

                csvfile.close()

            print(humidity)
            print(temperature)

            time.sleep(interval)

if __name__ == "__main__":
    main()
