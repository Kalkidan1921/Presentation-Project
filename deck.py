# Created by Tavish Peckham on 5.11.17

from random import sample
"""
    Deck objects are 52 card standard playing card decks.
"""

allCards = ("Ace of Diamonds", "Ace of Spades", "Ace of Hearts",
            "Ace of Clubs", "2 of Diamonds", "2 of Spades", "2 of Hearts",
            "2 of Clubs", "3 of Diamonds", "3 of Spades", "3 of Hearts",
            "3 of Clubs", "4 of Diamonds", "4 of Spades", "4 of Hearts",
            "4 of Clubs", "5 of Diamonds", "5 of Spades", "5 of Hearts",
            "5 of Clubs", "6 of Diamonds", "6 of Spades", "6 of Hearts",
            "6 of Clubs", "7 of Diamonds", "7 of Spades", "7 of Hearts",
            "7 of Clubs", "8 of Diamonds", "8 of Spades", "8 of Hearts",
            "8 of Clubs", "9 of Diamonds", "9 of Spades", "9 of Hearts",
            "9 of Clubs", "10 of Diamonds", "10 of Spades", "10 of Hearts",
            "10 of Clubs", "Jack of Diamonds", "Jack of Spades",
            "Jack of Hearts", "Jack of Clubs", "Queen of Diamonds",
            "Queen of Spades", "Queen of Hearts", "Queen of Clubs",
            "King of Diamonds", "King of Spades", "King of Hearts",
            "King of Clubs")

games = {"blackjack": ["hit", "hold"], "texas hold 'em": [""], "go fish": [""]}
S_IDLE = 0
S_BLACKJACK = 1
S_TEXAS = 2
S_FISH = 3
S_IDLE = 4
S_CHOOSING = 5


class Deck:
    def __init__(self):  # Creates a new deck object.
        self.cards = self.reset(allCards)

    def getDeck(self):  # Returns all cards left in the deck.
        return self.cards

    def shuffle(self, cardList):  # Shuffles all cards in the deck.
        self.cards = sample(cardList, k=len(cardList))

    def reset(self, cardList):  # Sets and returns the deck to the given deck.
        self.cards = sample(cardList, k=len(cardList))
        return self.cards

    def reveal(self):  # Returns the top card of the deck.
        topCard = self.cards[0]
        return topCard

    def burn(self, numToBurn):  # Burns the top x cards of the deck.
        if numToBurn < len(self.cards) and numToBurn > 0:
            self.cards = self.cards[numToBurn:]
            return ("%d cards burned." % (numToBurn))
        else:
            return ("Unable to burn %d cards." % (numToBurn))


class DealerBot:
    def __init__(self):
        self.state = S_IDLE

    def interMsg(self, msg):
        recipients, response = "all", ""
        if msg == "play":
            response = """
[Dealerbot] Hello, my name is Dealerbot. Which game would you like to play?>
1. blackjack
2. texas hold 'em
3. go fish"""

            self.state = S_CHOOSING

        if self.state is S_CHOOSING:
            if msg == "1":
                response = "Welcome to Blackjack. 1 to play, 2 for rules."
                self.state = S_BLACKJACK
            elif msg == "2":
                response = "Welcome to Texas Hold em.  1 to play, 2 for rules."
                self.state = S_TEXAS
            elif msg == "3":
                response = "Welcome to Go Fish.  1 to play, 2 for rules."
                self.state = S_FISH

        elif self.state is S_BLACKJACK:
            if msg == "1":
                response = "Play"
            elif msg == "2":
                response = "Rules"
            elif msg == "hit":
                response = "hit"

        if (msg == "stop"):
            recipients, response = "all", "Thanks for playing!"
            self.state = S_IDLE

        if response != "":
            response = " \n" + response

        return recipients, response


def blackjack():
    return ("Welcome to Blackjack. What would you like to do? (q to quit)> ")
    return ("1> Play")
    return ("2> Rules")

    selection = ""
    while selection not in ["1", "2", "q"]:
        selection = input("Enter your selection here (q to quit)> ")
    if selection == "1":
        return ("lol")


def texas():
    return (
        "Welcome to Texas Hold 'Em. What would you like to do? (q to quit)> ")
    return ("1> Play")
    return ("2> Rules")

    selection = ""
    while selection not in ["1", "2", "q"]:
        selection = input("Enter your selection here (q to quit)> ")


def fish():
    return ("Welcome to Go Fish. What would you like to do? (q to quit)> ")
    return ("1> Play")
    return ("2> Rules")

    selection = ""
    while selection not in ["1", "2", "q"]:
        selection = input("Enter your selection here (q to quit)> ")


"""testDeck.reveal()
testDeck.shuffle()
testDeck.reveal()
testDeck.burn()
testDeck.reveal()



selection = ""
while selection not in ["1", "2", "3", "q"]:
    selection = input("Enter your selection here (q to quit)> ")

if selection.lower() == "q":
    return ("Goodbye!")
elif selection == "1":
    blackjack()
elif selection == "2":
    texas()
elif selection == "3":
    fish()
else:
    return ("how did you get here? Dealberbot must reset.")"""
