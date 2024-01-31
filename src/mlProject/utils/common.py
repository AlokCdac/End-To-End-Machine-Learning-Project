import os
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """read yaml file and return

    Args:
    path_to_yaml(str):path like input
    raises:
    ValueError:if yaml file is Empty
    e:empty file
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml_file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("yaml file is Empty") 
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories:list, verbose=True):
    
    """
    create list of directories

    args:
    path_to_directories(list): list of path of directories
    ignore_log(bool, logs):ignore if multiple directories is created. default to false
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)

        if verbose:
            logger.info(f"created directories at: {path}")
@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path,'w') as f:
        json.dump(data, f, indent=4)

        logger.info(f"json file saved as: {path}")

def load_json(path:Path) -> ConfigBox:
    with open(path) as f:
        content=json.load(f)

        logger.info(f"json file loaded : {path}")
        return ConfigBox(content)

@ensure_annotations
def save_bin(data:any,path:Path):
    joblib.dump(value=data, filename=path)
    logger.info(f'binary file saved on: {path}' )

@ensure_annotations
def load_bin(path:Path) -> Any:
    data=joblib.load(path)
    logger.info(f"binary file loaded from: {path}")


def get_size(path:Path) -> str:
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"
