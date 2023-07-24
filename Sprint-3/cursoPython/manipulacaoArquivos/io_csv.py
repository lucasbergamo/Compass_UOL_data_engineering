import csv

with open('pessoas_1.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome: {}, Idade {}'.format(*pessoa))
