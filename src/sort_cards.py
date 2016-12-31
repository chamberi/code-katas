"""The sort cards module sorts cards from Ace to King."""


def sort_cards(cards):
    """The module takes in a list of cards, and sorts it from Ace to King."""
    for idx, val in enumerate(cards):
        if val == 'A':
            cards[idx] = '1'
        elif val == 'T':
            cards[idx] = '9.5'
        elif val == 'J':
            cards[idx] = '9.6'
        elif val == 'Q':
            cards[idx] = '9.7'
        elif val == 'K':
            cards[idx] = '9.8'
    cards.sort()
    for idx2, val2 in enumerate(cards):
        if val2 == "1":
            cards[idx2] = "A"
        if val2 == "9.5":
            cards[idx2] = "T"
        if val2 == "9.6":
            cards[idx2] = "J"
        if val2 == "9.7":
            cards[idx2] = "Q"
        if val2 == "9.8":
            cards[idx2] = "K"
    return cards
