#!/usr/bin/env python3

"""Wizard Battle Program."""

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
        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd.lower() == 'a':
            print('attack')
        elif cmd.lower() == 'r':
            print('runaway')
        elif cmd.lower() == 'l':
            print('look around')
        else:
            print('Exiting...')
            break


if __name__ == "__main__":
    main()
