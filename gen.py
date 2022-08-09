import signal

from utils import console
from utils import files

files.check_files()

from gens import fake_names
from gens import random_string
from gens import syllable_words
from gens import random_words

options = [
    {
        "name": "Fake names",
        "description": "Generates X fake names",
        "function": fake_names.main
    },
    {
        "name": "Random strings",
        "description": "Generates X random strings",
        "function": random_string.main
    },
    {
        "name": "Syllable words",
        "description": "Generates X words with specific syllable count",
        "function": syllable_words.main
    },
    {
        "name": "Random words",
        "description": "Generates X random words",
        "function": random_words.main
    }
]

def on_exit(signal, frame, empty_space=True):
    if empty_space:
        print()
    console.info("Exiting...")
    exit(0)

def select_menu():
    console.resize(68, 40)
    console.set_title("MC Name Generator")
    console.clear()
    console.generator_banner()

    console.info("Options:")
    for option in options:
        console.option(option["name"], option["description"])
    print()
    chosen_option = console.user_input("What do you want to generate (q to exit)? ")

    if chosen_option.lower() == "q":
        on_exit(None, None, empty_space=False)

    return chosen_option

def main():
    global in_gen

    while True:
        chosen_option = select_menu()

        for option in options:
            if option["name"].lower() == chosen_option:
                console.clear()
                console.generator_banner()
                console.set_title("MC Name Generator - " + option["name"])
                option["function"]()
                break
        else:
            console.error("Invalid option")
            console.user_input("Press enter to start over...")
            console.clear()
            console.generator_banner()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, on_exit)
    main()