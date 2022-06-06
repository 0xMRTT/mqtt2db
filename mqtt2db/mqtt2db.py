"""Main module."""

import datetime
import logging
import logging.config
import re
import sqlite3
import threading
import time
from pathlib import Path
from queue import Queue

import paho.mqtt.client as mqtt_client
import toml

MQTT2DB_CONFIG_FILE = Path("~/.config/mqtt2db.toml").expanduser()

logger = logging.getLogger("mqtt2db")

with MQTT2DB_CONFIG_FILE.open(
    "r", encoding="UTF-8"
) as config_file:  # Open the config file
    CONFIG: dict = toml.load(
        config_file
    )  # Load the file and parse the content with toml

try:
    LOG_LEVEL = CONFIG["logging"]["level"]  # Get the log level from the config
    LOG_PATH = CONFIG["logging"]["path"]  # Get the log path from the config
    LOG_FILEMOD = CONFIG["logging"]["filemod"]  # Get the log filemod from the config
except KeyError:
    logging.basicConfig(filename="mqtt2db.log", level=logging.INFO, filemode="w")
    logger = logging.getLogger("mqtt2db")
    logger.warning(
        "No logging configuration found in config file. Using default logging configuration."
    )
else:
    logging.basicConfig(filename=LOG_PATH, filemode=LOG_FILEMOD, level=LOG_LEVEL)
    logger = logging.getLogger("mqtt2db")
    logger.info("Logging configuration loaded from config file.")
finally:
    logger.info("Logging configuration loaded.")


class QueuedMessage:
    """Class to store a message received from MQTT broker."""

    __slots__ = [
        "receive_time",
        "topic",
        "payload",
        "sub_handler",
        "qos",
        "timeserie_sub_handlers",
    ]

    def __init__(
        self,
        receive_time,
        topic,
        payload,
        qos,
        sub_handler,
        timeserie_sub_handlers=None,
    ):
        self.receive_time = receive_time
        self.topic = topic
        self.payload = payload
        self.qos = qos
        self.sub_handler = sub_handler
        self.timeserie_sub_handlers = timeserie_sub_handlers
