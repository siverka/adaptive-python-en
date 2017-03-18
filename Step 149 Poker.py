suits = ['C', 'D', 'H', 'S']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


# Hands which do not fit any higher category are ranked by the value of their highest card.
def high_card(cards):
    return True


# Two of the five cards in the hand have the same value.
def pair(cards):
    vals = [v[:-1] for v in cards]
    return any([vals.count(v) == 2 for v in set(vals)])


# The hand contains two different pairs.
def two_pairs(cards):
    vals = [v[:-1] for v in cards]
    counts = [vals.count(v) == 2 for v in set(vals)]
    return counts.count(True) == 2


# Three of the cards in the hand have the same value.
def three_of_a_kind(cards):
    vals = [v[:-1] for v in cards]
    return any([vals.count(v) == 3 for v in set(vals)])


# Hand contains five cards with consecutive values.
def straight(cards):
    indxs = [values.index(v[:-1]) for v in cards]
    indxs.sort()
    if indxs == [0, 1, 2, 3, 12]:
        return True
    res = [indxs[i + 1] - indxs[i] == 1 for i in range(len(indxs) - 1)]
    return all(res)


# Hand contains five cards of the same suit.
def flush(cards):
    s = [card[-1] for card in cards]
    return len(set(s)) == 1


# Three cards of the same value, with the remaining two cards forming a pair.
def full_house(cards):
    return pair(cards) and three_of_a_kind(cards)


# Four cards with the same value.
def four_of_a_kind(cards):
    vals = [v[:-1] for v in cards]
    return any([vals.count(v) == 4 for v in set(vals)])


# Five cards of the same suit in numerical order.
def straight_flush(cards):
    return straight(cards) and flush(cards)


# Consists of the ace, king, queen, jack and ten of a suit.
def royal_flush(cards):
    if not flush(cards):
        return False
    vals = ['10', 'J', 'Q', 'K', 'A']
    return all([v[:-1] in vals for v in cards])


def poker_hand(cards):
    combinations = [royal_flush, straight_flush, four_of_a_kind, full_house, flush, straight, three_of_a_kind,
                    two_pairs, pair, high_card]
    names = ['Royal Flush', 'Straight Flush', 'Four of a Kind', 'Full House', 'Flush', 'Straight',
             'Three of a Kind', 'Two Pairs', 'Pair', 'High Card']

    for i in range(len(combinations)):
        if combinations[i](cards):
            return names[i]


hand = input().split()
# hand = ['10C', 'JC', 'QC', 'KC', 'AC']
print(poker_hand(hand))
