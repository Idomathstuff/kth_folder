from lab8.linkedQFile import LinkedQ
from arrayQFile import ArrayQ
import sys

def main():
    deck = LinkedQ() # // Creates object of class Linkedq. This is where we will store the initial state of the cards. With the top cards at left of the linkedQ and bottom cards to right of the linkedQ
    out_deck = LinkedQ() # // Creates one more object of class linkedq. This is where we put the cards we took out after each iteration of the card algorithim.
    svar = None

    while True:
        print("Lägg kort på deck. Om du är klar ange enter: ")
        try: # // Just a try loop that breaks when you don't enter an integer.
            svar = int(sys.stdin.readline())
            deck.enqueue(svar) # // enqueues your answer to the deck
        except:
            break
    print('Dina kort: ', deck)
    while deck.isEmpty() == False: #Repeats the 2 step shuffling process until the deck is empty

        tmp1 = deck.dequeue() # // Takes top card out
        deck.enqueue(tmp1) # // Puts that card at the bottom of deck

        # print(deck, '   ', out_deck)

        tmp2 = deck.dequeue() # // Takes top card out
        out_deck.enqueue(tmp2) # // Puts that card outside the deck

        # print(deck, '   ', out_deck)

    print('Shuffling klar: ',out_deck)


def mainA():
    deck = ArrayQ()  # // Creates object of class Linkedq. This is where we will store the initial state of the cards. With the top cards at left of the linkedQ and bottom cards to right of the linkedQ
    # // Creates one more object of class linkedq. This is where we put the cards we took out after each iteration of the card algorithim.
    out_deck = LinkedQ()
    svar = None

    while True:
        print("Lägg kort på deck. Om du är klar ange enter: ")
        try:  
            svar = input()# // Just a try loop that breaks when you don't enter an integer.
            deck.enqueue(svar)  # // enqueues your answer to the deck
        except:
            break
    print('Dina kort: ', deck)
    while deck.isEmpty() == False:  # Repeats the 2 step shuffling process until the deck is empty

        tmp1 = deck.dequeue()  # // Takes top card out
        deck.enqueue(tmp1)  # // Puts that card at the bottom of deck

        # print(deck, '   ', out_deck)

        tmp2 = deck.dequeue()  # // Takes top card out
        out_deck.enqueue(tmp2)  # // Puts that card outside the deck

        # print(deck, '   ', out_deck)

    print('Shuffling klar: ', out_deck)


mainA()