import sqlite3

# conn = sqlite3.connect("ogrod.db")
# cursor = conn.cursor()
# cursor.execute("create table rosliny (nazwa text, ilosc integer, kolor text, cena integer, toksyczna boolean)")
# cursor.execute("insert into rosliny (nazwa, ilosc, kolor, cena, toksyczna) values ('roslina1', 1, 'czerwony', 10, 'true')")
# cursor.execute("insert into rosliny (nazwa, ilosc, kolor, cena, toksyczna) values ('dynia', 15, 'pomarańczowa', 5, 'false')")
# cursor.execute("insert into rosliny (nazwa, ilosc, kolor, cena, toksyczna) values ('monstera', 2, 'zielony', 50, 'true')")
# conn.commit()
# conn.close()


conn = sqlite3.connect("ogrod.db")
cursor = conn.cursor()
rows = cursor.execute("select * from rosliny")
for row in rows:
    if row[4] == 'true':
        print(row)
        for field in row:
            print(field)
conn.close()
