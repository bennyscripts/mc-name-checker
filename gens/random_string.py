import string
import random

from utils import console

def main() -> None:
    console.info("Random strings generator")
    amount = int(console.user_input("Amount of names: "))
    length = int(console.user_input("Length of each name: "))
    numbers = console.user_input("Include numbers? (y/n): ")
    lowercase = console.user_input("Make names lowercase? (y/n): ")
    names = []

    print()
    for i in range(amount):
        name = ""
        
        for j in range(length):
            if numbers == "y":
                name += random.choice(string.ascii_letters + string.digits)
            else:
                name += random.choice(string.ascii_letters)

        if lowercase == "y":
            name = name.lower()

        names.append(name)
        console.added(name)

    with open("data/names.txt", "w") as f:
        for name in names:
            f.write(f"{name}\n")

    print()
    console.info(f"{len(names)} names generated, saved to data/names.txt")
    console.user_input("Press enter to go back...")