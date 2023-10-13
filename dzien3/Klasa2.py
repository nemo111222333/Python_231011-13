class Muppet:
    def __init__(self, name="muppet"):
        self.name = name
        self.kind = "muppet"
        self.x1 = "silence"

    def showme(self):
        print(f"Hello, my name is {self.name} and I'm {self.kind}")

    def voice(self):
        print("silence")


class Pig(Muppet):
    def __init__(self, name="muppet pig"):
        Muppet.__init__(self, name)
        self.kind = "pig"
        x1 = "chrum"

    def voice(self):
        print("oink, chrum chrum")

    def move(self):
        print("walks")


class Frog(Muppet):
    def __init__(self, name="muppet frog"):
        Muppet.__init__(self, name)
        self.kind = "frog"
        self.x1 = "croak"

    def voice(self):
        print("croak")

    def jump(self):
        print("jump")


class Guinea:
    def __init__(self, swimmer=True):
        self.swimmer = swimmer

    def move(self):
        print("swim")

    def voice(self):
        print("grrr")

    def dive(self):
        print("dive")


class GuineaPig(Guinea, Pig):
    def __init__(self, name, swimmer):
        Guinea.__init__(self, swimmer)
        Pig.__init__(self, name)

    def voiceExtra(self):
        Guinea.voice(self)
        # Pig.voice(self)


Holy = GuineaPig("Holy", False)
Holy.showme()
Holy.voice()
Holy.voiceExtra()
Holy.move()
Holy.dive()

# muppet = Muppet("XXX")
# muppet.showme()
# muppet.voice()
#
# Piggy = Pig("Miss Piggy")
# Piggy.showme()
# Piggy.voice()
# Piggy.move()
# Lola = Pig("Lola")
# Lola.showme()
# Lola.voice()
# Lola.move()
#
# Kermit = Frog("Kermit")
# Kermit.showme()
# Kermit.voice()
# Kermit.jump()
#
#
# yyyy = Guinea()
# yyyy.move()