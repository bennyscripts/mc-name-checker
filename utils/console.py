from turtle import color
import colorama
import os, sys

def set_title(text):
    if sys.platform == "win32":
        os.system(f"title {text}")
    else:
        sys.stdout.write("\x1b]2;" + text + "\x07")
        sys.stdout.flush()

def clear():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def resize(columns, rows):
    if sys.platform == "win32":
        os.system(f"mode con cols={columns} lines={rows}")
    else:
        os.system(f"echo '\033[8;{rows};{columns}t'")

def checker_banner():
    print(colorama.Fore.LIGHTBLUE_EX + colorama.Style.BRIGHT)
    print("""     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                        """)
    print(" >" + "—" * 61 + "< ")
    print(colorama.Style.RESET_ALL)

def generator_banner():
    width = 64
    banner = """ ██████╗ ███████╗███╗   ██╗
██╔════╝ ██╔════╝████╗  ██║
██║  ███╗█████╗  ██╔██╗ ██║
██║   ██║██╔══╝  ██║╚██╗██║
╚██████╔╝███████╗██║ ╚████║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝"""

    print(colorama.Fore.LIGHTBLUE_EX + colorama.Style.BRIGHT)
    
    for line in banner.split("\n"):
        print(" " + line.center(width, " "))

    print()
    print(" >" + "—" * 64 + "< ")
    print(colorama.Style.RESET_ALL)

def info(text):
    print(f" {colorama.Fore.LIGHTBLUE_EX}{colorama.Style.BRIGHT}[INFO]{colorama.Style.RESET_ALL} {text}")

def error(text):
    print(f" {colorama.Fore.LIGHTRED_EX}{colorama.Style.BRIGHT}[ERROR]{colorama.Style.RESET_ALL} {text}")

def warning(text):
    print(f" {colorama.Fore.LIGHTYELLOW_EX}{colorama.Style.BRIGHT}[WARNING]{colorama.Style.RESET_ALL} {text}")

def available(text):
    print(f" {colorama.Fore.LIGHTGREEN_EX}{colorama.Style.BRIGHT}[AVAILABLE]{colorama.Style.RESET_ALL} {text}")

def unavailable(text):
    print(f" {colorama.Fore.LIGHTRED_EX}{colorama.Style.BRIGHT}[UNAVAILABLE]{colorama.Style.RESET_ALL} {text}")

def user_input(text):
    return input(f" {colorama.Fore.BLUE}{colorama.Style.BRIGHT}[USER]{colorama.Fore.RESET}{colorama.Style.RESET_ALL} {text}")

def added(text):
    print(f" {colorama.Fore.LIGHTGREEN_EX}{colorama.Style.BRIGHT}[+]{colorama.Style.RESET_ALL} {text}")

def option(option, description):
    print(f"   {colorama.Fore.LIGHTYELLOW_EX}{colorama.Style.BRIGHT}{option}:{colorama.Style.RESET_ALL} {description}")