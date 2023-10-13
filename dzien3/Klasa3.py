class Okno:
    def __init__(self, il_elementow):
        self.typ = "okno pojedyncze"
        self.ramka = "ramka"
        self.il_elementow = il_elementow
    def draw(self):
        print(self.typ)
        print(self.ramka)
        if (self.il_elementow == 1):
            print("1 element")


class Okno2(Okno):
    def __init__(self, il_elementow):
        Okno.__init__(self, il_elementow)
        self.typ="okno wielu elementów"

    def draw(self):
        Okno.draw(self)
        print("2 elementy poziomo")

class Okno4(Okno2):
    def __init__(self, il_elementow):
        Okno2.__init__(self, il_elementow)
    def draw(self):
        Okno2.draw(self)
        print("+ 2 elementy poziomo")


o1 = Okno(1)
o2 = Okno2(2)
o4 = Okno4(4)

# o1.draw()
o2.draw()
# o4.draw()