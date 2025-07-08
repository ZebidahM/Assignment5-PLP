# utils/logger.py

import logging
import os

def setup_logger(log_file="logs/app.log", level=logging.INFO):
    """
    Set up logging configuration.
    """
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logging.basicConfig(
        level=level,
        format="%(asctime)s — %(levelname)s — %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger("readmission_logger")
