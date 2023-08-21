from linkedQFile import LinkedQ
import sys


def main():
    deck = LinkedQ()  # // Creates object of class Linkedq. This is where we will store the initial state of the cards. With the top cards at left of the linkedQ and bottom cards to right of the linkedQ
    out_deck = LinkedQ() # // Creates one more object of class linkedq. This is where we put the cards we took out after each iteration of the card algorithim.
    svar = None

    svar = sys.stdin.readline()
    for x in svar.split():
        if x != ' ' and x != '\n':
            deck.enqueue(x)

    while deck.isEmpty() == False:  # // Repeats the 2 step shuffling process until the deck is empty

        tmp1 = deck.dequeue()  # // Takes top card out
        deck.enqueue(tmp1)  # // Puts that card at the bottom of deck

        tmp2 = deck.dequeue()  # // Takes top card out
        out_deck.enqueue(tmp2)  # // Puts that card outside the deck
    print(out_deck)


if __name__ == "__main__":
    main()


