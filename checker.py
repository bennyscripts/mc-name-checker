import time
import os
import signal

from utils import config
from utils import files

config.create_config()
files.check_files()

from utils import webhooks as webhook
from utils import checker
from utils import console

archive_name = ""
checked = 0
available_names = []
unavailable_names = []

def on_exit(signal, frame):
    if len(available_names) > 0 or len(unavailable_names) > 0:
        date = time.strftime("%Y-%m-%d_%H-%M-%S")
        if not os.path.isdir("output"): os.mkdir("output")
        if not os.path.isdir(f"output/{date}"): os.mkdir(f"output/{date}")

        print()
        console.info(f"Finished checking {checked} names")
        console.info(f"Saved lists to output/{date}")

        if config.get_updates_webhook() != "":
            webhook.send_final_update(checked, available_names, unavailable_names)
        
        if config.get_archives_webhook() != "":
            archive = files.archive_dir(f"output/{date}")
            webhook.send_archive(archive_name, archive, date,available_names, unavailable_names)
            os.remove(archive)
    
    else:
        print()
        console.info("Exiting...")

    exit(0)

def main() -> None:
    global archive_name, checked, available_names, unavailable_names

    console.clear()
    console.resize(65, 40)
    console.set_title("MC Name Checker")
    files.check_files()
    console.clear()
    console.checker_banner()

    if config.get_archives_webhook() != "":
         archive_name = console.user_input("Name for archive webhook: ")

    fast = console.user_input("Fast mode? Could ratelimit webhooks (y/n): ")

    if fast == "y":
        console.info("Fast mode enabled. Use a VPN to prevent IP blocking.")

    console.user_input("Press enter to start checking...")

    console.clear()
    console.checker_banner()

    names = open("data/names.txt", "r").read().split("\n")

    if len(names) == 0:
        console.error("No names found")
        return

    console.info(f"{len(names)} names loaded")
    console.info(f"started check, press ctr+c to stop")
    print()

    for name in names:
        if not checker.is_valid(name):
            console.error(f"{name} has a cuss word or is invalid. skipping...")
            continue

        available = checker.is_available(name)
        
        if available:
            console.available(name)
            available_names.append(name)
            if config.get_available_webhook() != "":
                webhook.send_available(name)
        else:
            console.unavailable(name)
            unavailable_names.append(name)

        console.set_title(f"Available: {len(available_names)} - Unavailable: {len(unavailable_names)} - Checked: {checked}")
        checked += 1

        if checked % 50 == 0:
            if config.get_updates_webhook() != "":
                webhook.send_update(checked, available_names, unavailable_names)
            
        if fast.lower() == "y":
            time.sleep(0.01)
        else:
            time.sleep(1)

    date = time.strftime("%Y-%m-%d_%H-%M-%S")
    if not os.path.isdir("output"): os.mkdir("output")
    if not os.path.isdir(f"output/{date}"): os.mkdir(f"output/{date}")

    files.save_lists(date, available_names, unavailable_names)

    print()
    console.info(f"Finished checking {checked} names")
    console.info(f"Saved lists to output/{date}")

    if config.get_updates_webhook() != "":
        webhook.send_final_update(checked, available_names, unavailable_names)
    
    if config.get_archives_webhook() != "":
        archive = files.archive_dir(f"output/{date}")
        webhook.send_archive(archive_name, archive, date,available_names, unavailable_names)
        os.remove(archive)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, on_exit)
    main()
    console.user_input("Press enter to exit...")