import yaml
import os

def create_config():
    if not os.path.exists("config.yml"):
        config = {
            "available_webhook": "",
            "updates_webhook": "",
            "archives_webhook": ""
        }
        with open("config.yml", 'w') as f:
            yaml.dump(config, f)

def get_config():
    if not os.path.exists("config.yml"):
        create_config()
    with open("config.yml", 'r') as f:
        return yaml.load(f, Loader=yaml.FullLoader)

def get_available_webhook():
    config = get_config()
    hook = config["available_webhook"]
    if hook == "" or hook == None:
        return ""
    return hook

def get_updates_webhook():
    config = get_config()
    hook = config["updates_webhook"]
    if hook == "" or hook == None:
        return ""
    return hook

def get_archives_webhook():
    config = get_config()
    hook = config["archives_webhook"]
    if hook == "" or hook == None:
        return ""
    return hook