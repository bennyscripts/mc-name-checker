import random

from utils import console

WORDS = open("data/words.txt", "r").read().split("\n")
SWEARS = open("data/swears.txt", "r").read().split("\n")

def get_names(amount: int, lengths: list) -> list:
    names = []

    while len(names) < amount:
        name = random.choice(WORDS)

        if len(name) in lengths and name.lower() not in SWEARS:
            names.append(name)
            console.added(name)

    return names

def main() -> None:
    console.info("Random word generator")
    amount = int(console.user_input("Amount of names: "))
    multipleLengths = console.user_input("Multiple lengths? (y/n): ")
    if multipleLengths == "y":
        lengths = console.user_input("Lengths for each word (split with space): ").split(" ")
        lengths = [int(length) for length in lengths]
        print()
        names = get_names(amount, lengths)
    else:
        length = int(console.user_input("Length of each name: "))
        print()
        names = get_names(amount, [length])

    with open("data/names.txt", "w") as f:
        for name in names:
            f.write(f"{name}\n")

    print()
    console.info(f"{len(names)} names generated, saved to data/names.txt")
    console.user_input("Press enter to go back...")