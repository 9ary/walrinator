import random
import re

from telethon import events

from walrinator import client

@client.on(events.NewMessage(incoming=True, pattern=re.compile(r"(?i)(am|are|is) trash$")))
def trash(event):
    event.reply("and so am i")

@client.on(events.NewMessage(incoming=True, pattern=re.compile(r"(?i)^(-\d+|bad bot)$")))
def downvote(event):
    if random.randrange(5) == 0:
        event.reply("-1")
