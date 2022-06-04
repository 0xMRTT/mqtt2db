"""Main module."""

from pathlib import Path
MQTT2DB_CONFIG_FILE: Path = Path("~/.config/mqtt2db.toml").expanduser()
import toml
import click

def config_set(key:str, value:str) -> None:
    with MQTT2DB_CONFIG_FILE.open("a") as config_file:
        config_dict:dict = toml.load(config_file)
        try:
            config_dict[key] = value
        except Exception as e:
            return False
        else:
            toml.dump(config_dict, config_file)
            return True


def config_get(key:str) -> None:
    with MQTT2DB_CONFIG_FILE.open("r") as config_file:
        config_dict:dict = toml.load(config_file)
        try:
            get = config_dict[key]
        except Exception as e:
            return False
        else:
            return get
