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
        SmallAnimal(name='Bat',
                    level=3),
        Creature(name='Tiger',
                 level=12),
        Creature(name='Tiger',
                 level=80),
        Dragon(name='Dragon',
               level=50,
               scale_thickness=75,
               fire_breathing=True),
        Dragon(name='Dragon',
               level=100,
               scale_thickness=50,
               fire_breathing=False),
        Wizard(name='Evil Wizard',
               level=1000),
    ]

    hero = Wizard(name='Gandolf',
                  level=75)

    turns = 0
    while True:

        active_creature = random.choice(creatures)
        print(f'A {active_creature} has appeared from a dark forest...')

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')

        if cmd.lower() == 'a':
            if hero.fight(active_creature):
                creatures.remove(active_creature)
                hero.level_up(active_creature)
            else:
                hero.rest()

        elif cmd.lower() == 'r':
            print(f'{hero.name} runs away!')
        elif cmd.lower() == 'l':
            print(f'{hero.name} looks around and sees:')
            for creature in creatures:
                print(f'{creature}.')

            # Does the active creature choose to attack the Hero!
            if active_creature in creatures and \
                    active_creature.attack():
                if active_creature.fight(hero):
                    hero.rest()
                else:
                    creatures.remove(active_creature)
                    hero.level_up(2)

        elif cmd.lower() in ('q', 'x'):
            print('Exiting...')
            break

        if not creatures:
            print('You have won! Exiting...')
            break
        turns += 1


if __name__ == "__main__":
    main()
    print(f'Thank you for playing.')
