#!/usr/bin/env python3

"""Wizard Battle Program."""

import time
import random
from actors import Wizard, Creature, SmallAnimal, Dragon


def main():
    """Begin the Wizard Battle.

    The wizard battle program entry point.
    """
    game_loop()


def game_loop():
    """Game loop."""
    creatures = [
        SmallAnimal(name='Toad',
                    level=1),

        Creature(name='Tiger',
                 level=12),

        SmallAnimal(name='Bat',
                    level=3),

        Dragon(name='Dragon',
               level=50,
               scale_thickness=75,
               fire_breathing=True),

        Wizard(name='Evil Wizard',
               level=1000),
    ]

    hero = Wizard(name='Gandolf',
                  level=75)

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
            print(f'{hero.name} runs away!')
        elif cmd.lower() == 'l':
            print(f'{hero.name} looks around and sees:')
            for creature in creatures:
                print(f'{creature}.')
        else:
            print('Exiting...')
            break


if __name__ == "__main__":
    main()
    print(f'Thank you for playing.')
