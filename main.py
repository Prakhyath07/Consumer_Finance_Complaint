import os
from finance_complaint.constant.environment.variable_key import AWS_ACCESS_KEY_ID_ENV_KEY,AWS_SECRET_ACCESS_KEY_ENV_KEY
from dotenv import load_dotenv
load_dotenv()
access_key_id = os.getenv(AWS_ACCESS_KEY_ID_ENV_KEY, )
secret_access_key = os.getenv(AWS_SECRET_ACCESS_KEY_ENV_KEY, )
#print(access_key_id,secret_access_key)
import argparse
from finance_complaint.exception import FinanceException
from finance_complaint.pipeline import TrainingPipeline
from finance_complaint.logger import logger
from finance_complaint.config.pipeline.training import FinanceConfig
import sys



def start_training(start=False):
    try:
        if not start:
            return None
        print("Training Running")
        TrainingPipeline(FinanceConfig()).start()
        
    except Exception as e:
        raise FinanceException(e, sys)

def main():
    try:

        start_training(start=True)
    except Exception as e:
        raise FinanceException(e, sys)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        pass
        logger.exception(FinanceException(e, sys))