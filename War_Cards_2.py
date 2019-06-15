"""
Simple War card game simulator
"""

from random import shuffle

class Card:
    suits = ['Spades',
             'Hearts',
             'Diamonds',
             'Clubs']

    values = [None, None, '2', '3',
              '4', '5', '6', '7',
              '8', '9', '10',
              'Jack', 'Queen',
              'King', 'Ace']

    def __init__(self, v, s):
        """suit + value are ints"""
        self.value = v
        self.suit = s

    def __lt__(self, card2):
        """Less-than comparison"""
        if self.value < card2.value:
            return True
        elif self.value == card2.value:
            if self.suit < card2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, card2):
        if self.value > card2.value:
            return True
        elif self.value == card2.value:
            if self.suit > card2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " \
            + self.suits[self.suit]
        return v


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
            shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input("Enter Player One's name: ")
        name2 = input("Enter Player Two's name: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "{} wins this round".format(winner)
        print(w)

    def draw(self, p1Name, p1Card, p2Name, p2Card):
        d = "{} drew {}\n{} drew {}".format(p1Name, p1Card, p2Name, p2Card)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("Beginning War!")
        while len(cards) >= 2:
            m = "Press q to quit. Press any key to play: "
            response = input(m)
            if response == 'q':
                break
            p1Card = self.deck.rm_card()
            p2Card = self.deck.rm_card()
            p1Name = self.p1.name
            p2Name = self.p2.name
            self.draw(p1Name, p1Card, p2Name, p2Card)
            if p1Card > p2Card:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)

        print("War is over. {} wins".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"

game = Game()
game.play_game()