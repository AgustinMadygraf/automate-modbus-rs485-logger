"""
Path: src/shared/config.py
"""

import os
import logging
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("config")


def get_config():
    "Carga la configuración desde variables de entorno y devuelve un diccionario con los valores."
    config = {}

    # LOG_MESSAGE_MAX_LENGTH (opcional)
    raw_max_length = os.getenv("LOG_MESSAGE_MAX_LENGTH", "120")
    try:
        max_length = int(raw_max_length)
        if max_length <= 0:
            raise ValueError
    except (ValueError, TypeError):
        logger.warning("LOG_MESSAGE_MAX_LENGTH inválido, usando 120.")
        max_length = 120
    config["LOG_MESSAGE_MAX_LENGTH"] = max_length

    # LOG_LEVEL (opcional)
    log_level = os.getenv("LOG_LEVEL", "INFO")
    config["LOG_LEVEL"] = log_level

    # MODBUS_PORT (opcional)
    modbus_port = os.getenv("MODBUS_PORT", "COM3")
    config["MODBUS_PORT"] = modbus_port

    # MODBUS_SLAVE_ID (opcional)
    try:
        modbus_slave_id = int(os.getenv("MODBUS_SLAVE_ID", "1"))
    except ValueError:
        logger.warning("MODBUS_SLAVE_ID inválido, usando 1.")
        modbus_slave_id = 1
    config["MODBUS_SLAVE_ID"] = modbus_slave_id

    # MODBUS_BAUDRATE (opcional)
    try:
        modbus_baudrate = int(os.getenv("MODBUS_BAUDRATE", "9600"))
    except ValueError:
        logger.warning("MODBUS_BAUDRATE inválido, usando 9600.")
        modbus_baudrate = 9600
    config["MODBUS_BAUDRATE"] = modbus_baudrate

    # MODBUS_PARITY (opcional)
    modbus_parity = os.getenv("MODBUS_PARITY", "E")
    config["MODBUS_PARITY"] = modbus_parity

    # MODBUS_STOPBITS (opcional)
    try:
        modbus_stopbits = int(os.getenv("MODBUS_STOPBITS", "1"))
    except ValueError:
        logger.warning("MODBUS_STOPBITS inválido, usando 1.")
        modbus_stopbits = 1
    config["MODBUS_STOPBITS"] = modbus_stopbits

    # MODBUS_TIMEOUT (opcional)
    try:
        modbus_timeout = float(os.getenv("MODBUS_TIMEOUT", "0.5"))
    except ValueError:
        logger.warning("MODBUS_TIMEOUT inválido, usando 0.5.")
        modbus_timeout = 0.5
    config["MODBUS_TIMEOUT"] = modbus_timeout

    logger.debug(
        "Config cargada | LOG_LEVEL=%s | LOG_MESSAGE_MAX_LENGTH=%s | MODBUS_PORT=%s | "
        "MODBUS_SLAVE_ID=%s | MODBUS_BAUDRATE=%s | MODBUS_PARITY=%s | MODBUS_STOPBITS=%s | "
        "MODBUS_TIMEOUT=%s",
        config["LOG_LEVEL"],
        config["LOG_MESSAGE_MAX_LENGTH"],
        config["MODBUS_PORT"],
        config["MODBUS_SLAVE_ID"],
        config["MODBUS_BAUDRATE"],
        config["MODBUS_PARITY"],
        config["MODBUS_STOPBITS"],
        config["MODBUS_TIMEOUT"],
    )
    return config


__all__ = ["get_config"]
