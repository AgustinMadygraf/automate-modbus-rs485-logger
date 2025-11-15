"""
Path: src/shared/logger_cli_v0.py
"""

import logging
import coloredlogs
from src.shared.config import get_config



class TruncatingColoredFormatter(coloredlogs.ColoredFormatter):
    "Formateador de logs con colores y truncado de mensajes largos. Inspirado en Rasa CLI, pero con un estilo visual propio."
    def __init__(self, *args, max_length: int = None, **kwargs):
        self.max_length = max_length
        super().__init__(*args, **kwargs)

    def format(self, record: logging.LogRecord) -> str:
        "Formatea el mensaje de log, truncándolo si excede la longitud máxima."
        original_msg, original_args = record.msg, record.args
        if self.max_length and self.max_length > 0:
            message = record.getMessage()
            if isinstance(message, str) and len(message) > self.max_length:
                ellipsis = "..."
                cutoff = max(self.max_length - len(ellipsis), 1)
                record.msg = f"{message[:cutoff].rstrip()}{ellipsis}"
                record.args = ()
        try:
            return super().format(record)
        finally:
            record.msg, record.args = original_msg, original_args



def get_logger(name: str = "modbus-logger") -> logging.Logger:
    "Configura y devuelve un logger con formato de colores y truncado de mensajes largos."
    try:
        config = get_config()
    except (ImportError, FileNotFoundError, ValueError, KeyError):
        config = {}
    logger = logging.getLogger(name)
    raw_max_length = config.get("LOG_MESSAGE_MAX_LENGTH", 120)
    raw_level = config.get("LOG_LEVEL", "INFO")
    try:
        max_length = int(raw_max_length)
    except (TypeError, ValueError):
        max_length = 120
    if max_length <= 0:
        max_length = None
    level = str(raw_level).upper() if isinstance(raw_level, str) else "INFO"
    # Estilo visual propio: colores más vivos y formato diferente
    fmt = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    datefmt = "%H:%M:%S"
    custom_level_styles = {
        'info':    {'color': 'green', 'bold': True},
        'debug':   {'color': 'blue'},
        'warning': {'color': 'yellow', 'bold': True},
        'error':   {'color': 'red', 'bold': True},
        'critical':{'color': 'magenta', 'bold': True},
    }
    custom_field_styles = {
        'asctime': {'color': 'cyan'},
        'levelname': {'color': 'white', 'bold': True},
        'name': {'color': 'blue'},
    }
    if not logger.handlers:
        coloredlogs.install(
            level=level,
            logger=logger,
            fmt=fmt,
            datefmt=datefmt,
            isatty=True,
        )
        formatter = TruncatingColoredFormatter(
            fmt=fmt,
            datefmt=datefmt,
            level_styles=custom_level_styles,
            field_styles=custom_field_styles,
            max_length=max_length,
        )
        for handler in logger.handlers:
            handler.setFormatter(formatter)
        logger.propagate = False
    else:
        for handler in logger.handlers:
            formatter = getattr(handler, "formatter", None)
            if isinstance(formatter, TruncatingColoredFormatter):
                formatter.max_length = max_length
    logger.setLevel(level)
    return logger
