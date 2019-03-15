import random
from datetime import datetime
random.seed(datetime.now())

class Card (object):
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value


class Deck (object):
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    value = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    cards = []
    def __init__(self):
        # Build a deck of cards
        for i in range(len(self.ranks)):
            for j in self.suits:
                self.cards.append(Card(self.ranks[i], j, self.value[i]))
    def deal(self):
        if len(self.cards) > 0:
            dealt_card = self.cards.pop(0)
            print("\tDealt: {0} of {1}".format(dealt_card.rank, dealt_card.suit))
            return dealt_card
        else:
            print("\tDeck does not have enough cards. {0} cards remain.".format(len(self.cards)))
            return None
    def shuffle(self):
        random.shuffle(self.cards)


class Game (object):
    deck = None
    score_player = 0
    score_computer = 0
    def __init__(self):
        # Make a deck and shuffle it.
        self.deck = Deck()
        self.deck.shuffle()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("We are starting the game!")
        rounds = input("How many rounds would you like to play? ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        for i in range(rounds):
            self.round()
        self.print_scores()
    def print_scores(self):
        print("#############")
        print("Player:   {0:2d}".format(self.score_player))
        print("Computer: {0:2d}".format(self.score_computer))
        if self.score_player > self.score_computer:
            print("The player is the winner.")
        elif self.score_computer > self.score_player:
            print("The computer is the winner.")
        else:
            print("It was a tied game.")
        print("#############")
    def round(self):
        # deal a card to the player and computer
        print("**************************")
        print("\tDealing to player:")
        card_player = self.deck.deal()
        print("\tDealing to computer:")
        card_computer = self.deck.deal()
        print("**************************")
        # Make sure both players got cards
        if card_player and card_computer:
            # Compare values and award point
            if (card_player.value > card_computer.value):
                print("The player had a higher value.")
                self.score_player += 1
            elif (card_computer.value > card_player.value):
                print("The computer had a higher value.")
                self.score_computer += 1
            else:
                print("The player and the computer tied.")
        else:
            print("Not enough cards remain. Game Over.")
            self.print_scores()
            exit()


game = Game()
