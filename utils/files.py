import zipfile
import os
import httpx

def get_swears():
    url = "https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/master/en"
    res = httpx.get(url)
    return res.text.split("\n")

def get_words():
    url = "https://www.mit.edu/~ecprice/wordlist.100000"
    res = httpx.get(url)
    return res.text.split("\n")

def check_files():
    if not os.path.isdir("output"):
        os.mkdir("output")

    if not os.path.isdir("data"):
        os.mkdir("data")
    
    if not os.path.isfile("data/names.txt"):
        with open("data/names.txt", "w") as f:
            f.write("")

    if not os.path.isfile("data/swears.txt"):
        with open("data/swears.txt", "w", encoding="UTF-8") as f:
            for swear in get_swears():
                f.write(f"{swear}\n")

    if not os.path.isdir("data/words.txt"):
        with open("data/words.txt", "w") as f:
            for word in get_words():
                f.write(f"{word}\n")

def archive_dir(directory) -> str:
    # create a zip of the given dir and return the path
    zip_path = f"output/archive.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zip:
        for root, dirs, files in os.walk(directory):
            for file in files:
                zip.write(os.path.join(root, file))
    return zip_path

def save_lists(date, available_names, unavailable_names) -> None:
    with open(f"output/{date}/available_names.txt", "w") as f:
        for name in available_names:
            f.write(f"{name}\n")

    with open(f"output/{date}/unavailable_names.txt", "w") as f:
        for name in unavailable_names:
            f.write(f"{name}\n")