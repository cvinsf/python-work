SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(rank)
        self.suit_index = SUITS.index(suit)
# Check if cards are equal to each other via rank and suit
    def __eq__(self, other):
        return self.rank_index == other.rank_index and self.suit_index == other.suit_index
# check if card is less than by comparing rank, then suit
    def __lt__(self, other):
        if self.rank_index < other.rank_index:
            return True
        elif self.rank_index == other.rank_index:
            return self.suit_index < other.suit_index
        else:
            return False
# check if card is greater by comparing rank first, if equal compare suit
    def __gt__(self, other):
        if self.rank_index > other.rank_index:
            return True
        elif self.rank_index == other.rank_index:
            return self.suit_index > other.suit_index
        else:
            return False

    # don't touch below this line

    def __str__(self):
        return f"{self.rank} of {self.suit}"
