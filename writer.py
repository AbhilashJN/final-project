import csv
f=open('coordsfile.csv','a+')
writer = csv.writer(f)
writer.writerow([12.7,72.7])
writer.writerow([12.7,72.7])
writer.writerow([12.7,72.7])
f.close()
print 'finished writing'