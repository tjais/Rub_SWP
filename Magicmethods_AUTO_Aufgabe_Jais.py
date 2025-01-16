class Auto:
    def __init__(self, ps):
        if not isinstance(ps, (int, float)) or ps <= 0:
            raise ValueError("PS muss eine positive Zahl sein!")
        self.ps = ps

    # String-Darstellung
    def __str__(self):
        return f"Auto mit {self.ps} PS"

    def __repr__(self):
        return f"Auto({self.ps})"

    # Addition
    def __add__(self, other):
        if isinstance(other, Auto):
            return Auto(self.ps + other.ps)
        raise TypeError("Nur Auto-Objekte können addiert werden!")

    # Subtraktion
    def __sub__(self, other):
        if isinstance(other, Auto):
            result_ps = self.ps - other.ps
            if result_ps <= 0:
                raise ValueError("Das Ergebnis hat keine PS mehr (<= 0)!")
            return Auto(result_ps)
        raise TypeError("Nur Auto-Objekte können subtrahiert werden!")

    # Multiplikation
    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            if factor <= 0:
                raise ValueError("Der Multiplikationsfaktor muss größer als 0 sein!")
            return Auto(self.ps * factor)
        raise TypeError("Auto-Objekte können nur mit Zahlen multipliziert werden!")

    # Vergleichsoperationen
    def __eq__(self, other):
        if isinstance(other, Auto):
            return self.ps == other.ps
        return False

    def __lt__(self, other):
        if isinstance(other, Auto):
            return self.ps < other.ps
        raise TypeError("Vergleich nur mit anderen Auto-Objekten möglich!")

    def __gt__(self, other):
        if isinstance(other, Auto):
            return self.ps > other.ps
        raise TypeError("Vergleich nur mit anderen Auto-Objekten möglich!")

    def __len__(self):
        return self.ps  # Gibt die PS als Länge zurück (nur symbolisch)




a1 = Auto(50)
a2 = Auto(60)


print(a1)
print(a2)

a3 = a1 + a2
print(a3)


a4 = a2 - a1
print(a4)


a5 = a1 * 2
print(a5)


print(len(a1))


print(a1 == a2)
print(a1 < a2)
print(a1 > a2)


try:
    a1 + 10
except TypeError as e:
    print(e)

try:
    a1 * -1
except ValueError as e:
    print(e)

try:
    a1 - Auto(100)
except ValueError as e:
    print(e)
