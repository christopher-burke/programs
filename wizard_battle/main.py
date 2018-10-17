#!/usr/bin/env python3

"""Wizard Battle Program."""


def main():
    game_loop()


def game_loop():
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
