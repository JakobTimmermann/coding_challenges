def calculate_score(hand):
    numbers = [card[0] for card in hand]
    suits = [card[1] for card in hand]
    for idx, n in enumerate(numbers):
        if n in number_map.keys():
            numbers[idx] = number_map[n]
        else:
            numbers[idx] = int(n)
    numbers.sort(reverse=True)
    frequencies = {}
    for n in numbers:
        frequencies[n] = frequencies.setdefault(n, 0) + 1

    if len(set(suits)) == 1:
        suits_score = score_for_same_suits(numbers)
    else:
        suits_score = 0

    numbers_score = get_number_score(frequencies)
    if is_straight(numbers) and numbers_score < 18:
        numbers_score = 18
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    sorted_frequencies = dict(sorted_frequencies)
    return max(numbers_score, suits_score), sorted_frequencies


def get_number_score(frequencies):
    freqs = list(frequencies.values())
    pairs = freqs.count(2)
    threes = freqs.count(3)
    fours = freqs.count(4)
    if fours:
        return 21
    if threes and pairs:
        return 20
    if threes:
        return 17
    if pairs == 2:
        return 16
    if pairs == 1:
        return 15
    return max(frequencies.keys())


def is_straight(numbers):
    for idx in range(len(numbers)-1):
        if numbers[idx] != numbers[idx+1] + 1:
            return False
    return True


def score_for_same_suits(numbers):
    if is_straight(numbers):
        if numbers[0] == 14:
            return 23
        else:
            return 22
    return 19


with open("p054_poker.txt", "r") as file:
    games = file.readlines()

games = [hand.strip().split() for hand in games]

number_map = {
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}

player_one_wins = 0

for cards in games:
    hand_one = cards[:5]
    hand_two = cards[5:]
    score_one, freqs_one = calculate_score(hand_one)
    score_two, freqs_two = calculate_score(hand_two)
    if score_one > score_two:
        player_one_wins += 1
    elif score_one == score_two:
        cards_one = list(freqs_one.keys())
        cards_two = list(freqs_two.keys())
        for idx, card_one in enumerate(cards_one):
            card_two = cards_two[idx]
            if card_one == card_two:
                continue
            break
        if card_one > card_two:
            player_one_wins += 1

print(player_one_wins)