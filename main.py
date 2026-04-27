import pandas as pd
import yaml

def read_config():
    CONFIG_DIR = "./config.yaml"
    with open(CONFIG_DIR , "r") as file:
        config = yaml.safe_load(file)

    return config


