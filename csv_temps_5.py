import matplotlib.pyplot as plt
import csv
from datetime import datetime

open_file1 = open('sitka_weather_2018_simple.csv', 'r')
open_file2 = open('death_valley_2018_simple.csv','r')

csv_file1 = csv.reader(open_file1, delimiter=',')
csv_file2 = csv.reader(open_file2, delimiter=',')

header_row1 = next(csv_file1)
station1 = next(csv_file1)
header_row2 = next(csv_file2)
station2 = next(csv_file2)
l1 = [i for i in range(len(header_row1))]
l2 = [i for i in range(len(header_row2))]
header1 = dict(zip(header_row1,l1))
header2 = dict(zip(header_row2,l2))
station1_name = station1[header1['NAME']]
station2_name = station2[header2['NAME']]

highs1,highs2,lows1,lows2,dates1,dates2 = [],[],[],[],[],[]
# the two following blocks could have been a function, but I went with copy/paste instead.
for row in csv_file1:
    try:
        high1 = int(row[header1['TMAX']])
        low1 = int(row[header1['TMIN']])
        current_date1 = datetime.strptime(row[header1['DATE']], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for {current_date1}") # use f to format variables into strings, similar to %.2f
    else:
        highs1.append(high1)
        lows1.append(low1)
        dates1.append(current_date1)

for row in csv_file2:
    try:
        high2 = int(row[header2['TMAX']])
        low2 = int(row[header2['TMIN']])
        current_date2 = datetime.strptime(row[header2['DATE']], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for {current_date2}") # use f to format variables into strings, similar to %.2f
    else:
        highs2.append(high2)
        lows2.append(low2)
        dates2.append(current_date2)
# this block will try the data if its all good, and continue with the else statements if there are no exceptions.
# if there are exceptions, the else block will not be executed.

fig, ax = plt.subplots(2,figsize=(10,6))
fig.suptitle(f'Temperature comparison between {station1_name} and {station2_name}. ')
fig.autofmt_xdate()
# The call to fig.autfmt_xdate() draws the date labels diagonally to prevent them from # overlapping.

ax[0].plot(dates1, highs1, color='red', alpha=0.8)
ax[0].plot(dates1, lows1, color='blue', alpha=0.8)
ax[0].fill_between(dates1, highs1, lows1, facecolor='blue',alpha=0.1)
ax[0].set_title(station1[header1['NAME']], fontsize=10)
ax[0].set_xlabel('',fontsize=10)
ax[0].set_ylabel('Temperature (F)',fontsize=10)
ax[0].tick_params(axis='both',which='minor',labelsize=10)

ax[1].plot(dates2, highs2, color='red', alpha=0.8)
ax[1].plot(dates2, lows2, color='blue', alpha=0.8)
ax[1].fill_between(dates2, highs2, lows2, facecolor='blue',alpha=0.1)
ax[1].set_title(station2[header2['NAME']], fontsize=10)
ax[1].set_xlabel('',fontsize=10)
ax[1].set_ylabel('Temperature (F)',fontsize=10)
ax[1].tick_params(axis='both',which='minor',labelsize=10)

plt.show()