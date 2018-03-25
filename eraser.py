import sys
import csv
from math import radians, cos, sin, asin, sqrt

def calcDistance(lat1, lon1, lat2, lon2):
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # 6367 km is the radius of the Earth
    km = 6367 * c
    return km


f=open('coordsfile.csv','r+')
reader = csv.reader(f)
final=[]
for row in reader:
	if calcDistance(float(row[0]),float(row[1]),float(sys.argv[1]),float(sys.argv[2]))>0.2:
		final.append(row)
f.seek(0)
f.truncate()
writer = csv.writer(f,lineterminator='\n')
writer.writerows(final)
