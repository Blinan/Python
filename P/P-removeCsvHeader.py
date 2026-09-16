import csv
from pathlib import Path
import os

os.makedirs(Path.cwd()/'removeCsvHeader', exist_ok=True)

for csvFilename in os.listdir(Path.cwd()/'automate_online-materials'/'removeCsvHeader'):
    if not csvFilename.endswith('.csv'):
        continue
    print('Removing header from ' + csvFilename + '...')
    csvdata = []
    csvFileObj = open(Path.cwd()/'automate_online-materials'/'removeCsvHeader'/csvFilename)
    csvReaderObj = csv.reader(csvFileObj)
    for row in csvReaderObj:
        if csvReaderObj.line_num == 1:
            continue
        csvdata.append(row)
    csvFileObj.close()

    csvFileObj = open(Path.cwd()/'removeCsvHeader'/('headerRemoved'+csvFilename),'w',newline='')
    csvWriterObj = csv.writer(csvFileObj)

    for row in csvdata:
        csvWriterObj.writerow(row)

    csvFileObj.close()
