# This module provides general-purpose functions like loading configurations, displaying styled output, and managing directories.
python
# utils/helpers.py

import yaml
import os

def load_config(config_path="model/config.yaml"):
    """
    Load YAML configuration file and return dictionary.
    """
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config

def ensure_dir(path):
    """
    Create directory if it doesn't exist.
    """
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"📁 Created directory: {path}")

def print_banner(message):
    """
    Nicely formatted banner for logs or scripts.
    """
    print("\n" + "="*50)
    print(f"{message.upper()}")
    print("="*50 + "\n")
