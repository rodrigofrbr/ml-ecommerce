import numpy as np
import pandas as pd
import requests
import csv


with open("data/distancia.csv", 'r') as file_r:
    with open("data\distancia_update.csv", 'w') as file_w:
        reader = csv.reader(file_r)
        writer = csv.writer(file_w)

        for row in reader:
            url = 'refer to OSRM API Instance' + row[2] + ',' + row[1] + ';' + row[4] + ',' + row[3]
            print(url)

            query = 'UPDATE TABLENAME SET DISTANCE = ' + str(requests.get(url).json()['routes'][0]['distance']) + ' WHERE ORDER_ID = ' + "'" + row[0] + "'"
            
            writer.writerow([query])

    



    

        