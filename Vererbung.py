
class Tier:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def beschreibung(self):
        return f"{self.name} ist {self.alter} Jahre alt."


class Saeugetier(Tier):
    def __init__(self, name, alter, fellfarbe):
        super().__init__(name, alter)
        self.fellfarbe = fellfarbe
    def beschreibung(self):
        return f"{self.name} ist {self.alter} Jahre alt und hat {self.fellfarbe}es Fell."


class Vogel(Tier):
    def __init__(self, name, alter, flugfaehigkeit):
        super().__init__(name, alter)
        self.flugfaehigkeit = flugfaehigkeit
    def beschreibung(self):
        return f"{self.name} ist {self.alter} Jahre alt und kann {self.flugfaehigkeit}."




if __name__ == "__main__":
    hund = Saeugetier("Rex", 5, "braun")
    adler = Vogel("Adler", 3, "fliegen")

    print(hund.beschreibung())
    print(adler.beschreibung())
