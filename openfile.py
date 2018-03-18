# openfile.py
# Maria o sullivan 11-03-2018
with open("data/iris.csv") as f:
      for line in f: 
print('{:5} {:5} {:5} {:5}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))
