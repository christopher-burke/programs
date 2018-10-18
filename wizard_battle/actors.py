#!/usr/bin/env python3

"""Wizard Battle - Actors."""
import random
import time


class Creature:
    def __init__(self, name: str, level: int, *args, **kwargs):
        self.name = name
        self.level = level
        self.modifier = random.randint(5, 12)

    def level_up(self, defeated_creature):
        self.level += 1 if defeated_creature < self else 5
        print(f'You are now level {self.level}.')

    def __repr__(self):
        return f'{self.__class__.__name__}(name=\'{self.name}\', level={self.level})'

    def __str__(self):
        return f'{self.name} of level {self.level}'
        # return f'Creature: {self.name} of level {self.level}.'

    def __lt__(self, other):
        return self.level < other.level

    def __le__(self, value):
        return super().__le__(value)

    def __gt__(self, value):
        return super().__gt__(value)

    def fight(self, opponent):
        print(f'{self.name} attacks {opponent.name}!')
        if self > opponent:
            print(f'{self} +1 advantage.')

        self_roll = self.get_defensive_roll()
        self_roll += 1 if self > opponent else 0
        opponent_roll = opponent.get_defensive_roll()

        print(f'{self.name} roll [{self_roll}].')
        print(f'{opponent.name} roll [{opponent_roll}].')

        if self_roll >= opponent_roll:
            print(f'{self.name} has triumphed over {opponent.name}.')
            return True
        else:
            print(f'{self.name} has been DEFEATED!!!')
            return False

    def rest(self):
        print(f'{self.name} needs time to recover...')
        time.sleep(5)
        print(f'{self.name} returns!')

    def attack(self):
        return bool(random.getrandbits(1))

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level * self.modifier


class Wizard(Creature):
    """Wizard actor in Wizard Battle."""

    def __init__(self, name, level, *args, **kwargs):
        super().__init__(name, level, *args, **kwargs)

    def get_defensive_roll(self):
        magic_mod = 100 - (self.level % 100)
        return super().get_defensive_roll() * magic_mod

    def attack(self) -> bool:
        """Wizard Attack method."""
        return super().attack()


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
        return int(base_roll // 2)
