import httpx

http = httpx.Client()
swears = open("data/swears.txt", "r").read().split("\n")
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"

def is_in_swears(name):
    return name in swears

def is_alpha(name):
    for char in name:
        if char not in alphabet:
            return False
    return True

def is_valid(name):
    return not is_in_swears(name) and " " not in name and len(name) >= 3 and is_alpha(name)

def is_available(name):
    res = http.get(
        f"https://api.mojang.com/users/profiles/minecraft/{name}",
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    )

    if res.status_code == 200:
        return False
    elif res.status_code == 204:
        return True