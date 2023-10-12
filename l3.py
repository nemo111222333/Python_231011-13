# x = [i for i in range(10)]
# print(x)
#
# y = [i for i in range(10) if i % 2 == 0]
# print(y)

# lista dni tygodnia =
# {"poniedziałek": 1, "wtorek": 2, "sroda": 3, "czwartek": 4, "piątek": 5, "sobota": 6, "niedziela": 7}
# zrobić listę zaczynających się od "p"


# dni = {"poniedziałek": 1, "wtorek": 2, "sroda": 3, "czwartek": 4, "piątek": 5, "sobota": 6, "niedziela": 7}
# print({value: key for key, value in dni.items()})


bardzo_dluga_zmienna_majaca_jeszcze_dluzsza_wartosc = \
    "adadsdasdasdasdsdasdadsasdasdasdsadasdasdasdasasdasdasdasdasdsdasds"

print(bardzo_dluga_zmienna_majaca_jeszcze_dluzsza_wartosc)

szachownica = [["białe", "czarne", "białe", "czarne", "białe", "czarne", "białe", "czarne"],
               ["czarne", "białe", "czarne", "białe", "czarne", "białe", "czarne", "białe"],
               ["białe", "czarne", "białe", "czarne", "białe", "czarne", "białe", "czarne"],
               ["czarne", "białe", "czarne", "białe", "czarne", "białe", "czarne", "białe"],
               ["białe", "czarne", "białe", "czarne", "białe", "czarne", "białe", "czarne"],
               ["czarne", "białe", "czarne", "białe", "czarne", "białe", "czarne", "białe"],
               ["białe", "czarne", "białe", "czarne", "białe", "czarne", "białe", "czarne"],
               ["czarne", "białe", "czarne", "białe", "czarne", "białe", "czarne", "białe"]
               ]

sql1 = "select * from table1 where field1 = 1"
print(sql1)

sql2 = """  
            select * 
            from table1 
            where field1 = 1"""
print(sql2)
print("ala")