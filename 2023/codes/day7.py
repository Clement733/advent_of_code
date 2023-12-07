from collections import Counter
text = open('../inputs/day7')

# Assign value to cards
def calc(mode):

    if mode == 1:
        card_values = {x: i for i, x in enumerate("AKQJT98765432")}
    else:
        card_values = {x: i for i, x in enumerate("AKQT98765432J")}
    (
            five_of_a_kind,
            four_of_a_kind,
            full_house,
            three_of_a_kind,
            two_pair,
            one_pair,
            high_card,
        ) = range(7)
    # Look at every line, determine the combination of card in them
    hands = []
    for line in text:
        combs = line.split(' ')[0]
        bids = int(line.strip().split(' ')[1])
        values = [card_values[x] for x in combs]
        joker = 0
        count_h = Counter(combs)
        if mode == 2:
            joker = count_h['J']
            del count_h['J']
        count_v = Counter(count_h.values())

        if len(count_h) == 1 or len(count_h) == 0:
            hand_type = five_of_a_kind
        elif max(count_h.values()) + joker == 4:
            hand_type = four_of_a_kind
        elif (len(count_h) == 2 and 2 in count_h.values() and 3 in count_h.values()) or (count_v[2] == 2 and joker == 1):
            hand_type = full_house
        elif (3 - joker) in count_h.values():
            hand_type = three_of_a_kind
        elif (2 in count_v and count_v[2] == 2) or (joker > 0 and 2 in count_v):
            hand_type = two_pair
        elif (2 - joker) in count_h.values():
            hand_type = one_pair
        else:
            hand_type = high_card

        hands.append((hand_type, tuple(values), combs, bids))
        hands.sort(reverse=True)
        ret = 0
        for i, (hand_type, values, combs, bids) in enumerate(hands):
            ret += bids * (i + 1)
    print(ret)

calc(2)
