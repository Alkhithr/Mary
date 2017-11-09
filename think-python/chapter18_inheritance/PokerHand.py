"If you run PokerHand.py, it deals seven 7-card poker hands and checks to see if any of them contains a flush. """
from Card import Hand, Deck


class PokerHand(Hand):

    __excluded__ = ["count_pairs"]

    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def group_cards(self):
        card_groups = dict()
        for card in self.cards:
            card = str.split(str(card), ' ')
            try:
                card_groups[card[0]] += 1
            except KeyError:
                card_groups[card[0]] = 1
        return card_groups

    def count_pairs(self):
        pairs = 0
        for card in self.group_cards():
            if self.group_cards()[card] == 2:
                pairs += 1
        return pairs

    def count_threes(self):
        threes = 0
        for card in self.group_cards():
            if self.group_cards()[card] == 3:
                threes += 1
        return threes

    def has_pair(self):
        """return True or False according to whether or not the hand meets the relevant criteria."""
        return self.count_pairs() == 1

    def has_two_pair(self):
        return self.count_pairs() == 2

    def has_three_of_a_kind(self):
        return self.count_threes() == 3

    def has_straight(self):
        self.cards.sort()
        first_card = self.cards[0]
        return first_card

    def classify(self):
        """figures out the highest-value classification for a hand and sets the label attribute accordingly.
        For example, a 7-card hand might contain a flush and a pair; it should be labeled “flush”.
        straight
        flush

        4 - of - a - kind
        full house
        flush
        straight
        3 - of - a - kind
        two pairs
        a pair
        high card"""
        pass


def figure_out_classification():
    """figures out the highest-value classification for a hand and sets the label attribute accordingly.
    For example, a 7-card hand might contain a flush and a pair; it should be labeled “flush”."""
    pass


def print_classification_probability():
    """Run your program with larger and larger numbers of hands until the output values converge to a reasonable degree of accuracy.
    Compare your results to the values at http://en.wikipedia.org/wiki/Hand_rankings."""
    pass


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    hand = PokerHand()
    deck.move_cards(hand, 5)
    print(hand)
    print(hand.group_cards())

    print('has pair:\t', hand.has_pair())
    print('has two pairs: \t', hand.has_two_pair())
    print('has_straight: \t', hand.has_straight())

