"""Main module."""

import logging
from pathlib import Path

import toml

MQTT2DB_CONFIG_FILE = Path("~/.config/mqtt2db.toml").expanduser()

logger = logging.getLogger("mqtt2db")


def config_get(key: str) -> None:
    """Get value from the config file"""
    with MQTT2DB_CONFIG_FILE.open(
        "r", encoding="UTF-8"
    ) as config_file:  # Open the config file
        config_dict: dict = toml.load(
            config_file
        )  # Load the file and parse the content with toml
        try:  # Try to get the key
            get = config_dict[key]
        except KeyError:  # If there is no key return False
            return False
        else:  # Else, return the value
            return get
