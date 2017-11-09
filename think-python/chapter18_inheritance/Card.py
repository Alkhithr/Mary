"""Let's talk about inheritance"""


import random


class Card:
    """spades = 3, hearts = 2, diamonds = 1, clubs = 0
    jack = 11, queen = 12, king = 13"""

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (self.rank_names[self.rank], self.suit_names[self.suit])

    def __lt__(self, other):
        result = False
        if 1 < self.rank < other.rank:
            result = True
        elif self.rank == other.rank and self.suit < other.suit:
            result = True
        elif self.rank == 1 and other.rank > 1:
            result = False
        return result


class Deck:
    """52 cards"""
    def __init__(self):
        self.cards = []
        for suit in range(0, 4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        result = []
        for card in self.cards:
            result.append(str(card))
        return '|'.join(result)

    def card_pop(self):
        return self.cards.pop()

    def card_add(self, card):
        return self.cards.append(card)

    def shuffle(self):
        return random.shuffle(self.cards)

    def sort(self):
        deck_with_ordinal = dict()
        sorted_deck = []
#       sort the deck using __lt__ from the Card class
        for card in self.cards:
            card_ordinal = str(card.suit) + str(card.rank)
            if len(card_ordinal) == 2:
                card_ordinal = '0' + str(card.suit) + str(card.rank)
            deck_with_ordinal[card_ordinal] = card
        for i in sorted(deck_with_ordinal):
            sorted_deck.append(str(deck_with_ordinal[i]))
        return '|'.join(sorted_deck)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.card_add(self.card_pop())


class Hand(Deck):
    """This is a hand of playing cards. Cards = parent. Hand = child
    when you override a method, the interface of the new method should be the same as the old.
    It should take the same parameters, return the same type, and obey the same preconditions and postconditions.
    If you violate this rule, which is called the “Liskov substitution principle”,
    your code will collapse like (sorry) a house of cards."""
    def __init__(self, label=''):
        self.cards = []
        self.label = label


def find_defining_class(obj, method_name):
    """MRO = method resolution order"""
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty


def test_stuff():
    """Play around with Cards
    spades = 3, hearts = 2, diamonds = 1, clubs = 0
    jack = 11, queen = 12, king = 13"""
    sep = '\n'+'-'*100+'\n'
    test_card = Card(0, 1)
    print(test_card)

    card_1 = Card(1, 1)
    card_2 = Card(1, 2)

    print('%s is lower than %s : %s' % (card_1, card_2, card_1.__lt__(card_2)), end='\n\n')

    deck = Deck()
    card_3 = Card(rank=12, suit=3)
    print(card_3)

    print('Untouched Deck: \n', deck, end=sep)

    deck.card_pop()
    print('removed last card: \n', deck, end=sep)

    deck.shuffle()
    print('shuffled deck: \n', deck, end=sep)

    print('sorted deck: \n', deck.sort(), end=sep)

    hand = Hand(label='test hand')
    deck = Deck()
    deck.shuffle()
    deck.move_cards(hand, 11)
    print(hand)
    print(deck)

    print(find_defining_class(hand, 'shuffle'))


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    hand = Hand()

    deck.move_cards(hand, 5)
    hand.sort()
    print(hand)
