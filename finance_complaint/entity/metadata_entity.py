from finance_complaint.exception import exception
from finance_complaint.logger import logger
from finance_complaint.utils import read_yaml_file, write_yaml_file
import os,sys
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionMetaDataConfig:
    from_date: str
    to_date : str
    data_file_path: str