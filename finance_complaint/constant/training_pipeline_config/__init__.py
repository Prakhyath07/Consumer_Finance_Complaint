from finance_complaint.constant.training_pipeline_config.data_ingestion import *
from finance_complaint.constant.training_pipeline_config.data_validation import *
from finance_complaint.constant.training_pipeline_config.data_transformation import *
from finance_complaint.constant.training_pipeline_config.model_trainer import *
import os

PIPELINE_NAME = "finance-complaint"
PIPELINE_ARTIFACT_DIR = os.path.join(os.getcwd(), "finance_artifact")