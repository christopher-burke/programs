#!/usr/bin/env python3

"""Journal App"""


def event_loop():
    """Program loop."""
    print('What do you want to journal?')
    cmd = None
    journal_data = []

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


def list_entries(data):
    """List journal entries."""
    entries = reversed(data)
    for entry in entries:
        print(entry)


def add_entry(data):
    """Add journal entries."""
    text = input('Enter your entry: ')
    data.append(text)


def main():
    """Journal Main function."""
    event_loop()


if __name__ == "__main__":
    main()
