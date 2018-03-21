import logging
from importlib import import_module

from telethon import TelegramClient

import secrets

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger("main")

client = TelegramClient('the_game', secrets.api_id, secrets.api_hash, update_workers=1, spawn_read_thread=False)
client.start()

plugins = ("misc", "re", "snippets")

for p in plugins:
    import_module(f"plugins.{p}")

client.idle()
