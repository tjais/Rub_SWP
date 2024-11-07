import random




def ziehung(r1, r2, r3, a):
    zahlen = list(range(r1, r2))
    gezogene_zahlen = []

    for i in range(r3):
        zahl = random.choice(zahlen)
        zahlen.remove(zahl)
        a[zahl] += 1
        gezogene_zahlen.append(zahl)

    print("Gezogene Zahlen:", gezogene_zahlen)

def ergebnis_ausgeben(a):
    print("\nErgebnisse der Ziehung:")
    for b in a:
        print(b, ":", a[b])

if __name__ == '__main__':
    r: str = input('Geben Sie die Parameter Ihres Spiels fest (getrennt durch Kommas): ')
    range_of_game = r.split(',')
    inp: str = input('Anzahl der Durchgänge?: ')
    a = {i: 0 for i in range(int(range_of_game[0]), int(range_of_game[1]))}
    for c in range(int(inp)):
        ziehung(int(range_of_game[0]), int(range_of_game[1]), int(range_of_game[2]), a)

    ergebnis_ausgeben(a)
