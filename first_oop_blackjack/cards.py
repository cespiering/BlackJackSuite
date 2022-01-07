# Classes for the playing cards

# Card class
    # each card must have a number, suit and value
    # each card must be able to be face up or face down(?) - default to face up

# Deck class
    # each deck must have all 52 playing cards
    #

# Shoe class
    # shoe will take in n decks
    # shuffle, remove cards, hit a stopping point (cut)

# Hand class
    # hand will take in two cards, add cards, keep track of hand value, track bust

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.set_value()
        
        
    def set_value(self):
        if self.rank in ['K', 'Q', 'J']:
            return 10
        if self.rank == 'A':
            return 11
        else:
            return self.rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    
class Deck:
    suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
    ranks = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        for suit in self.suits:
            for rank in self.ranks:
                new_card = Card(rank, suit)
                self.cards.append(new_card)

class Shoe:
    
    def __init__(self, num_of_decks):
        self.full_shoe = []
        self.num_of_decks = num_of_decks

    def shuffle_shoe(self):
        ordered_shoe = []
        for x in range(self.num_of_decks):
            next_deck = Deck()
            ordered_shoe.extend(next_deck.cards)
        return ordered_shoe
        #Create the shuffle feature

    def reset_shoe(self):
        pass
        #reshuffle shoe when 75% of cards have been dealt

    def remove_card(self):
        pass
        #remove a dealt card from the shoe
        # in next iterations, use a linked list






shoe = Shoe(2)
test = shoe.shuffle_shoe()
print(len(test))