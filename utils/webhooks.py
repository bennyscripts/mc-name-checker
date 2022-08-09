import json
import httpx
import easy_discord_webhooks

from . import config

http = httpx.Client()
try:
    if config.get_available_webhook() != "": webhook = easy_discord_webhooks.Webhook(config.get_available_webhook())
except Exception as e:
    print(e)
    webhook = ""
try:
    if config.get_updates_webhook() != "": updates_webhook = easy_discord_webhooks.Webhook(config.get_updates_webhook())
except Exception as e:
    print(e)
    updates_webhook = ""
if config.get_archives_webhook() != "": lists_webhooks = config.get_archives_webhook()

def send_available(name):
    webhook.send("", embed=easy_discord_webhooks.Embed(title="", description=f"**{name}** is available.\nhttps://namemc.com/search?q={name}", color="#3AA55D"))

def send_update(checked, available, unavailable):
    updates_webhook.send("", embed=easy_discord_webhooks.Embed(title="", description=f"Currently have checked **{checked}** names.\n\n**-** Available: **{len(available)}**\n**-** Unavailable: **{len(unavailable)}**", color="#2F3136"))

def send_final_update(checked, available, unavailable):
    updates_webhook.send("", embed=easy_discord_webhooks.Embed(title="", description=f"Finished checking at total of **{checked}** names!\n\n**-** Available: **{len(available)}**\n**-** Unavailable: **{len(unavailable)}**", color="#3AA55D"))

def send_archive(archive_name, archive, date, available, unavailable):
    http.post(lists_webhooks, json={"content": "", "embeds": [dict(easy_discord_webhooks.Embed(title="", description=f"New archive available for `{archive_name}`.\n\n**-** Available: **{len(available)}**\n**-** Unavailable: **{len(unavailable)}**", color="#2F3136"))]})
    http.post(lists_webhooks, files=[('file', (f'{date}.zip', open(archive,'rb'), 'application/zip'))], data={"payload_json": json.dumps({"content": ""})})