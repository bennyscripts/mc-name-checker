import names as gen

from utils import console

def main() -> None:
    console.info("Fake names generator")
    amount = int(console.user_input("Amount of names to generate: "))
    multipleLengths = console.user_input("Generate multiple lengths? (y/n): ")
    lengths_ = []
    names = []

    if multipleLengths == "y":
        lengths = console.user_input("Lengths to generate (separated by commas): ").split(",")
        for length in lengths:
            lengths_.append(int(length.strip()))
    else:
        length = int(console.user_input("Length of each name: "))
        lengths_.append(length)

    print()
    
    while len(names) < amount:
        name = gen.get_first_name()

        if " " not in name and len(name) in lengths_:
            if name not in names:
                names.append(name)
                console.added(name)

    with open("data/names.txt", "w") as f:
        for name in names:
            f.write(f"{name}\n")

    print()
    console.info(f"{len(names)} names generated, saved to data/names.txt")
    console.user_input("Press enter to go back...")