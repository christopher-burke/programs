#!/usr/bin/env python3

"""Wizard Battle - Actors."""
import random


class Creature:
    def __init__(self, name: str, level: int, *args, **kwargs):
        self.name = name
        self.level = level

    def __repr__(self):
        return f'{self.__class__.__name__}(name=\'{self.name}\', level={self.level})'

    def __str__(self):
        return f'{self.name} of level {self.level}'
        # return f'Creature: {self.name} of level {self.level}.'

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    def attack(self, creature):
        print(f'{self.name} attacks {creature.name}!')

        my_roll = random.randint(1, 12) * self.level
        creature_roll = random.randint(1, 12) * creature.level

        print(f'{self.name} roll [{my_roll}].')
        print(f'{creature.name} roll [{creature_roll}].')

        if my_roll >= creature_roll:
            print(f'{self.name} has triumphed over {creature.name}.')
            return True
        else:
            print(f'{self.name} has been DEFEATED!!!')
            return False


class Dragon(Creature):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)


class Ork(Creature):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
