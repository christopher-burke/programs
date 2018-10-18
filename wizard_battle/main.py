#!/usr/bin/env python3

"""Wizard Battle Program."""

import time
import random
from actors import Wizard, Creature


def main():
    game_loop()


def game_loop():

    creatures = [
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000),
    ]

    hero = Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)
        print(f'A {active_creature} has appeared from a dark forest...')

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd.lower() == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print(f'{hero.name} needs time to recover...')
                time.sleep(5)
                print(f'{hero.name} returns!')

        elif cmd.lower() == 'r':
            print('runaway')
        elif cmd.lower() == 'l':
            print('look around')
        else:
            print('Exiting...')
            break


if __name__ == "__main__":
    main()
