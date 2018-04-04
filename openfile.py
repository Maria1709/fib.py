# openfile.py
# Maria o sullivan 11-03-2018
#Open file Iris as a comma separated value file in text format called f
with open("data/iris.csv") as f:
      for line in f: 
#print columns 1-4 formatted with comas to separate
print('{:5} {:5} {:5} {:5}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))
