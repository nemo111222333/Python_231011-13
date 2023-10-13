import csv


def odczyt():
    with open('dane.csv') as csv_file:
        csvdata = csv.reader(csvfile=csv_file, delimiter=',')
        for row in csvdata:
            # print(row)
            if len(row) > 0:
                print(row[0])
            else:
                print('<wiersz pusty>')
            # for field in row:
            #     print(field)


def odczyt1():
    plik1 = open('dane.csv')
    data = plik1.read()
    csvdata = csv.reader(data, delimiter=',')

    for row in csvdata:
        print(row)


odczyt()
