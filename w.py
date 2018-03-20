import logging
from importlib import import_module

from walrinator import client

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger("main")

plugins = ("misc", "re")

for p in plugins:
    import_module(f"plugins.{p}")

client.idle()
