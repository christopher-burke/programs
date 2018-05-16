#!/usr/bin/env python3

"""Guess that card."""

import random
from collections import namedtuple
from itertools import chain

DEBUG = False

# Setup
# Build Card deck. Shuffle, then select 1 card.
Card = namedtuple("Card", ['rank', 'suit'])
ranks = chain(range(2, 11), "J,Q,K,A".split(','))
suits = 'spade,club,heart,diamond'.split(',')
Deck = [Card(rank=r, suit=s) for r in ranks for s in suits]
random.shuffle(Deck)
the_card = Deck[random.randint(0, len(Deck)-1)]  # randint is a >= N >= b
if DEBUG:
    print(the_card)  # Print the selected card.

# Picture card rank translation.
picture_cards = {
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}

# Suit emoji
symbols = {
    'spade': '♠️',
    'club': '♣️',
    'heart': '♥️',
    'diamond': '♦️',
}

# Input prompts
rank_input = 'Card Rank? (2-10, J, Q, K, or A): '
suit_input = 'Card Suit? (spade, club, heart, or diamond): '

# Guess again... msg
guess_again_msg = "Guess again..."

# Rank tester msg
rank_tester_msg = {
    'low': "{} was too low.",
    'high': "{} was too high.",
    'correct': "{} is correct!",
}

# Suit tester msg
suit_tester_msg = {
    False: "{} is incorrect.",
    True: "{} is correct!",
}

# Final results msg
result_msg = {
    'guesses': "It took you {} guesses.",
    'guess': "It took you {} guess. AMAZING.",
    'final': "You got it! The {} of {}'s was the card.'",
}

# Guess Card setup
guess = Card(rank=0, suit="none")  # A place holder card
guesses = 1  # there will always be 1 guess.

while guess != the_card:
    # Guess rank amd suit input
    if guess.rank != the_card.rank:
        guess_rank = input(rank_input)
        try:
            guess_rank = int(guess_rank)
        except (TypeError, ValueError):
            guess_rank = guess_rank
    if guess.suit != the_card.suit:
        guess_suit = input(suit_input)

    # Create Card with guess inputs
    guess = Card(rank=guess_rank, suit=guess_suit.lower())
    # Rank Tester
    guess_rank_value = picture_cards.get(guess.rank, guess.rank)
    the_card_rank_value = picture_cards.get(the_card.rank, the_card.rank)

    _ = guess_rank_value - the_card_rank_value

    if _ < 0:
        print(rank_tester_msg['low'].format(guess.rank))
    elif _ > 0:
        print(rank_tester_msg['high'].format(guess.rank))
    else:
        print(rank_tester_msg['correct'].format(guess.rank))

    # Suit Tester
    _ = (guess.suit == the_card.suit)
    print(suit_tester_msg[_].format(guess.suit))

    if any([guess.rank != the_card.rank, guess.suit != the_card.suit, ]):
        print(guess_again_msg)
        guesses += 1

    if DEBUG:
        print()
        print(guess, the_card, guess == the_card)
        print(guesses)
        print()

    # Final Result
    if guess == the_card:
        if guesses > 1:
            print(result_msg['guesses'])
        else:
            print(result_msg['guess'])

        print(result_msg['final'].format(
            guess.rank,
            guess.suit
        )
        )


print("DONE!")
