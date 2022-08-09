import httpx

from utils import console

API = "https://randomwordgenerator.com/json/words.php?qty=50&category=extended&first_letter=&last_letter=&word_size_by=number_of_syllables&operator=equals&length="
CLIENT = httpx.Client()

def get_names(amount: int, syllables: int) -> list:
    words = []
    names = []
    
    for word in CLIENT.get(API + str(syllables)).json():
        words.append(word)

    while len(names) < amount:
        response = CLIENT.get(API + str(syllables)).json()
        names.extend(response)

    names = list(set(names))

    if len(names) > amount:
        names = names[:amount]

    return names

def main() -> None:
    console.info("Syllable words generator")
    amount = int(console.user_input("Amount of names: "))
    syllables = int(console.user_input("Syllables: "))
    print()
    
    swears = open("data/swears.txt", "r").read().split("\n")
    names = []
    names.extend(get_names(amount, syllables))

    with open("data/names.txt", "w") as f:
        for name in names:
            if " " in name:
                name = name.replace(" ", "_")
            if len(name) >= 3 and name.lower() not in swears:
                f.write(f"{name}\n")
                console.added(name)
    
    print()
    console.info(f"{len(names)} names generated, saved to data/names.txt")
    console.user_input("Press enter to go back...")