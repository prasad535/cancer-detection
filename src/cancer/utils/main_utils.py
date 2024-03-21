import os
import yaml
from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError

from cancer import logger


def read_yaml_file(path: Path) -> ConfigBox:
    try:
        with open(path) as file:
            content = yaml.safe_load(file)
            logger.info(f"Loaded yaml file {path} successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise BoxValueError("YAML file is empty")



