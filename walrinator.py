from telethon import TelegramClient

import secrets

client = TelegramClient('the_game', secrets.api_id, secrets.api_hash, update_workers=1, spawn_read_thread=False)
client.start()
