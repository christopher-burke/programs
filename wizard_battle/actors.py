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
    """Wizard actor in Wizard Battle."""

    def attack(self, creature) -> bool:
        """Wizard Attack method."""
        print(f'{self.name} attacks {creature.name}!')

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print(f'{self.name} roll [{my_roll}].')
        print(f'{creature.name} roll [{creature_roll}].')

        if my_roll >= creature_roll:
            print(f'{self.name} has triumphed over {creature.name}.')
            return True
        else:
            print(f'{self.name} has been DEFEATED!!!')
            return False


class Dragon(Creature):
    """Dragon in Wizard Battle."""

    def __init__(self, name, level, scale_thickness, fire_breathing, *args, **kwargs):
        super().__init__(name, level, *args, **kwargs)
        self.scale_thickness = scale_thickness
        self.fire_breathing = fire_breathing

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_mod = 5 if self.fire_breathing else 1
        scale_mod = self.scale_thickness // 10
        return int(base_roll * fire_mod * scale_mod)


class SmallAnimal(Creature):
    """Small Animal in Wizard Battle."""

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        print(base_roll)
        return int(base_roll // 2)
