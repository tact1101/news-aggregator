import logging
import logging.config
import os
import json

# Create a reusable logging configuration
LOG_FILE = "logs.log"

def setup_logger(name, log_level=logging.INFO):
    """
    Set up a logger with a specified name and log level.
    Logs are written to a centralized JSON file.
    """
    with open(LOG_FILE, 'w') as f:
        f.write("")

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Avoid adding duplicate handlers if logger is reused
    if not logger.handlers:
        file_handler = logging.FileHandler(LOG_FILE)
        formatter = logging.Formatter(
           '{"timestamp": "%(asctime)s", "level": "%(levelname)s", "module": "%(module)s", '
            '"function": "%(funcName)s", "line": "%(lineno)d", "message": "%(message)s"}',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
