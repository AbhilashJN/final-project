import csv

f=open('coordsfile.csv','r+')
reader = csv.reader(f)
final=[]
for row in reader:
	if float(row[0])==14.990593333 and float(row[1])==77.713053333:
		final.append(row)
f.seek(0)
f.truncate()
writer = csv.writer(f,lineterminator='\n')
writer.writerows(final)
