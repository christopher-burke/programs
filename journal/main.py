#!/usr/bin/env python3

"""Journal App"""


def event_loop():
    """Program loop."""
    print('What do you want to journal?')
    cmd = None

    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()
        if cmd == 'l':
            print('listing...')
        elif cmd == 'a':
            print('adding...')
        elif cmd != 'x':
            print(f"[{cmd}] command not found.")

    print("Done, thank you.")


def list_entries(data):
    """List journal entries."""
    print(data)


def add_entry(data):
    """Add journal entries."""
    text = input('Enter your entry: ')
    data.append(text)


def main():
    """Journal Main function."""
    event_loop()


if __name__ == "__main__":
    main()
