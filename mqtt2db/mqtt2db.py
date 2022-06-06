"""Main module."""

import logging
from pathlib import Path

import toml

MQTT2DB_CONFIG_FILE = Path("~/.config/mqtt2db.toml").expanduser()

logger = logging.getLogger("mqtt2db")

with MQTT2DB_CONFIG_FILE.open(
    "r", encoding="UTF-8"
) as config_file:  # Open the config file
    CONFIG: dict = toml.load(
        config_file
    )  # Load the file and parse the content with toml

LOG_LEVEL = CONFIG["logging"]["level"]
LOG_PATH = CONFIG["logging"]["path"]
LOG_FILEMOD = CONFIG["logging"]["filemod"]

logging.basicConfig(filename=LOG_PATH, filemode=LOG_FILEMOD, level=LOG_LEVEL)
