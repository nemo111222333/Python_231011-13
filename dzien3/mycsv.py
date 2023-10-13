import csv


def odczyt():
    with open('dane.csv') as csv_file:
        csvdata = csv.reader(csv_file, delimiter=',')
        for row in csvdata:
            # print(row)
            if len(row) > 0:
                for field in row:
                    print(field)
                # print(row[0])
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


biblioteka = {"Baśnie":["Andersen","Hans Christian", "polski"], "First step in Python": ["Doe", "John", "english"], "Pan Tadeusz": ["Mickiewicz", "Adam", "polski"]}


def zapis(nazwa_pliku, biblioteka):
    with open('dane_out.csv', 'a', encoding='utf-8', newline='\n') as csv_file:
        csvdata = csv.writer(csv_file, delimiter=';')
        for ksiazka in biblioteka:
            tmp = biblioteka[ksiazka]
            tmp.insert(0,ksiazka)
            csvdata.writerow(tmp)

zapis('', biblioteka)