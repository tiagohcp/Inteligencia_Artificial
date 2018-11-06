import csv
import os
import pandas
import matplotlib.pyplot as plt

data = csv.reader(open("players_stats.csv","r"))
gerado = csv.writer(open("player_stats_new.csv","w"),lineterminator='\r')
path =  os.path.dirname(os.path.realpath(__file__))
dir = os.listdir(path)
cont = 0
cont = 0

for rows in data:
    if rows[24] == '' or rows[29] == '' or rows[30] == '' or rows[32] == '': 
        next
    else:
        gerado.writerow(rows)
