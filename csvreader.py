import csv

coordsFile = open('coordsfile.csv','r')
coordsReader = csv.reader(coordsFile)
coordsArray=[]
for row in coordsReader:
	coordsArray.append([float(row[0]),float(row[1])])
print coordsArray