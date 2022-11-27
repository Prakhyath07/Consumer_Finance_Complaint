import shutil
import yaml
from typing import List
from finance_complaint.exception import FinanceException
from finance_complaint.logger import logger
import os, sys


def write_yaml_file(file_path: str, data: dict =None):
    """
    Create yaml file 
    file_path: str
    data: dict
    """
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok= True)
        with open(file_path,"w") as yaml_file:
            if data is not None:
                yaml.dump(data, yaml_file)
                logger.info(f"data written to yaml file {file_path}")
    except Exception as e:
        raise FinanceException(e, sys)


def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns the contents as a dictionary.
    file_path: str
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            logger.info(f"reading yaml file {file_path}")
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise FinanceException(e, sys) from e



def create_directories(directories_list: List[str], new_directory=False):
    try:

        for dir_path in directories_list:
            if dir_path.startswith("s3"):
                continue
            if os.path.exists(dir_path) and new_directory:
                shutil.rmtree(dir_path)
                logger.info(f"Directory removed: {dir_path}")
            os.makedirs(dir_path, exist_ok=True)
            logger.info(f"Directory created: {dir_path}")
    except Exception as e:
        raise FinanceException(e, sys)