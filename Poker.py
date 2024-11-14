import random
import matplotlib.pyplot as plt

value_names = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suit_names = ["Kreuze", "Pik", "Herz", "Karo"]

def get_card_name(card):
    value = value_names[card % 13]
    suit = suit_names[card // 13]
    return f"{value} {suit}"

def is_pair(hand):
    values = [card % 13 for card in hand]
    return len(set(values)) < len(values)

def is_three_of_a_kind(hand):
    values = [card % 13 for card in hand]
    return any(values.count(v) == 3 for v in values)

def is_straight(hand):
    values = sorted([card % 13 for card in hand])
    return values == list(range(values[0], values[0] + 5))

def is_flush(hand):
    suits = [card // 13 for card in hand]
    return len(set(suits)) == 1

def is_full_house(hand):
    values = [card % 13 for card in hand]
    return len(set(values)) == 2 and any(values.count(v) == 3 for v in values)

def is_four_of_a_kind(hand):
    values = [card % 13 for card in hand]
    return any(values.count(v) == 4 for v in values)

def is_royal_flush(hand):
    values = sorted([card % 13 for card in hand])
    suits = [card // 13 for card in hand]
    return values == [8, 9, 10, 11, 12] and len(set(suits)) == 1

def test_combination(hand):
    if is_royal_flush(hand):
        return "Royal Flush"
    elif is_four_of_a_kind(hand):
        return "Vierling"
    elif is_full_house(hand):
        return "Full House"
    elif is_flush(hand):
        return "Flush"
    elif is_straight(hand):
        return "Straight"
    elif is_three_of_a_kind(hand):
        return "Drilling"
    elif is_pair(hand):
        return "Paar"
    else:
        return "Nichts"

def simulate_games(num_games):
    results = {
        "Royal Flush": 0,
        "Vierling": 0,
        "Full House": 0,
        "Flush": 0,
        "Straight": 0,
        "Drilling": 0,
        "Paar": 0,
        "Nichts": 0
    }

    try:
        for _ in range(num_games):
            deck = list(range(52))
            random.shuffle(deck)
            hand = random.sample(deck, 5)
            combination = test_combination(hand)
            results[combination] += 1
            hand_names = [get_card_name(card) for card in hand]
            print(hand_names)
            print(combination)
    except Exception as e:
        print("Ein Fehler ist während der Spielsimulation aufgetreten:", e)
    return results

def plot_results(results, num_games):
    try:
        labels = list(results.keys())
        counts = [results[combination] for combination in labels]
        percentages = [(count / num_games) * 100 for count in counts]

        plt.bar(labels, percentages, color='skyblue')
        plt.xlabel('Kombination')
        plt.ylabel('Prozentualer Anteil (%)')
        plt.xticks(rotation=45)
        plt.title(f'Pokerkombinationen aus {num_games} Spielen')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print("Ein Fehler ist beim Plotten der Ergebnisse aufgetreten:", e)

if __name__ == '__main__':

        num_games = int(input('Anzahl der Durchgänge?: '))
        results = simulate_games(num_games)
        plot_results(results, num_games)
