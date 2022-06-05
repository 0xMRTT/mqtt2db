"""Main module."""

from pathlib import Path

MQTT2DB_CONFIG_FILE = Path("~/.config/mqtt2db.toml").expanduser()
import toml
import logging

logger = logging.getLogger("mqtt2db")


def config_get(key: str) -> None:
    """Get value from the config file"""
    with MQTT2DB_CONFIG_FILE.open("r") as config_file: # Open the config file
        logger.info(f"Open {MQTT2DB_CONFIG_FILE}")
        config_dict: dict = toml.load(config_file) # Load the file and parse the content with toml
        try: # Try to get the key
            get = config_dict[key]
        except KeyError as e: # If there is no key return False and log the error
            logger.error(f"Unable to found key {e}")
            return False
        else: # Else, return the value and log the value
            logger.info(f"{key} -> {get}")
            return get
