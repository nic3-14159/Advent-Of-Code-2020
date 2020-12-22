import sys
player_2 = False
p1_cards = list()
p2_cards = list()
for line in sys.stdin:
    if line.strip() == "Player 2:":
        player_2 = True
        continue
    if line.strip() == "Player 1:" or line.strip() == "":
        continue
    if player_2:
        p2_cards.append(int(line.strip()))
    else:
        p1_cards.append(int(line.strip()))
num_cards = len(p1_cards) + len(p2_cards)

while len(p1_cards) > 0 and len(p2_cards) > 0:
    card_1 = p1_cards.pop(0)
    card_2 = p2_cards.pop(0)
    if card_1 > card_2:
        p1_cards.append(card_1)
        p1_cards.append(card_2)
    else:
        p2_cards.append(card_2)
        p2_cards.append(card_1)
    print(p1_cards)
    print(p2_cards)
    print()

score = 0
print(p1_cards)
print(p2_cards)
for i, card in enumerate(p1_cards if len(p1_cards) > 0 else p2_cards):
    print(card, num_cards, i)
    score += card * (num_cards - i)
print(score)
