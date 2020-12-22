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

def deck_hash(deck_1, deck_2):
    deck_1_hash = 0
    deck_2_hash = 0
    for i, card in enumerate(deck_1):
        deck_1_hash += card*100**i
    for i, card in enumerate(deck_2):
        deck_2_hash += card*100**i
    return (deck_1_hash, deck_2_hash)

def combat(p1_cards, p2_cards):
    seen_decks = set()
    while len(p1_cards) > 0 and len(p2_cards) > 0:
        hashes = deck_hash(p1_cards, p2_cards)
        if hashes in seen_decks:
            return (1, p1_cards)
        seen_decks.add(hashes)
        card_1 = p1_cards.pop(0)
        card_2 = p2_cards.pop(0)
        if len(p1_cards) >= card_1 and len(p2_cards) >= card_2:
            sub_game = combat(p1_cards[:card_1], p2_cards[:card_2])
            if sub_game[0] == 1:
                p1_cards.append(card_1)
                p1_cards.append(card_2)
            else:
                p2_cards.append(card_2)
                p2_cards.append(card_1)
        else: 
            if card_1 > card_2:
                p1_cards.append(card_1)
                p1_cards.append(card_2)
            else:
                p2_cards.append(card_2)
                p2_cards.append(card_1)
    if len(p1_cards) > 0:
        return (1, p1_cards)
    else:
        return (2, p2_cards)

winner, cards = combat(p1_cards, p2_cards)
score = 0
for i, card in enumerate(cards):
    score += card * (len(cards) - i)
print(score)
