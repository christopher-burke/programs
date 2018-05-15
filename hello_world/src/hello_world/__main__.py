"""Main application entry point.

    python -m hello_world  ...

"""


def main():
    """Execute the application."""
    print("""Hello World Application.""")
    print("""--------------------------------""")

    user_text = input("What is your name? ")
    greeting = f'Nice to meet you {user_text}.'

    print(greeting)


# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())
