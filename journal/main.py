#!/usr/bin/env python3

"""Journal App."""

import journal


def event_loop():
    """Program loop."""
    print('What do you want to journal?')
    cmd = None
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x':
            print(f"[{cmd}] command not found.")

    print("Done, thank you.")
    journal.save(journal_name, journal_data)


def list_entries(data):
    """List journal entries."""
    entries = reversed(data)
    for idx, entry in enumerate(entries, 1):
        print(f'* [{idx}] {entry}')


def add_entry(data):
    """Add journal entries."""
    text = input('Enter your entry: ')
    journal.add_entry(text, data)


def main():
    """Journal Main function."""
    event_loop()


if __name__ == "__main__":
    main()
