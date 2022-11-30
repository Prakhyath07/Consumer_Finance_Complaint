from finance_complaint.entity.config_entity import (DataIngestionConfig, TrainingPipelineConfig,
DataValidationConfig, DataTransformationConfig, ModelTrainerConfig)
from finance_complaint.constant.training_pipeline_config import *
from finance_complaint.constant import TIMESTAMP
from finance_complaint.logger import logger
from finance_complaint.exception import FinanceException
from datetime import datetime
from finance_complaint.entity import metadata_entity

class FinanceConfig:

    def __init__(self, pipeline_name = PIPELINE_NAME, timestamp =TIMESTAMP):
        """
        prepares timestamp, pipeline name and other training pipeline related config
        
        """
        self.timestamp = timestamp
        self.pipeline_name = pipeline_name
        self.pipeline_config = self.get_pipeline_config()


    def get_pipeline_config(self)-> TrainingPipelineConfig:
        """
        This will return TrainingPipelineConfig
        
        """
        try:
            artifact_dir = PIPELINE_ARTIFACT_DIR
            pipeline_config = TrainingPipelineConfig(pipeline_name = self.pipeline_name,
                                                    artifact_dir = artifact_dir)
            
            logger.info(f"Pipeline configuration: {pipeline_config}")

            return pipeline_config

        except Exception as e:
            raise FinanceException(e, sys)

    
    def get_data_ingestion_config(self, from_date = DATA_INGESTION_MIN_START_DATE, to_date= None) \
        -> DataIngestionConfig:

        """
        from date can not be less than min start date

        if to_date is not provided automatically current date will become to date

        """

        min_start_date = datetime.strptime(DATA_INGESTION_MIN_START_DATE, "%Y-%m-%d")
        from_date_obj = datetime.strptime(from_date, "%Y-%m-%d")
        if from_date_obj < min_start_date:
            from_date = DATA_INGESTION_MIN_START_DATE
        if to_date is None:
            to_date = datetime.now().strftime("%Y-%m-%d")

        """
        master directory for data ingestion
        we will store metadata information and ingested file to avoid redundant download
        """
        data_ingestion_master_dir = os.path.join(self.pipeline_config.artifact_dir,
                                                DATA_INGESTION_DIR)

        # time based directory for each run
        data_ingestion_dir = os.path.join(data_ingestion_master_dir,
                                        self.timestamp)

        metadata_file_path = os.path.join(data_ingestion_master_dir, DATA_INGESTION_METADATA_FILE_NAME)

        data_ingestion_metadata = metadata_entity.Information_meta(metadata_file_path=metadata_file_path)

        if data_ingestion_metadata.is_metadata_file_present:
            metadata_info = data_ingestion_metadata.get_metadata_info()
            from_date = metadata_info.to_date

        data_ingestion_config = DataIngestionConfig(
            from_date=from_date,
            to_date=to_date,
            data_ingestion_dir=data_ingestion_dir,
            download_dir=os.path.join(data_ingestion_dir, DATA_INGESTION_DOWNLOADED_DATA_DIR),
            file_name=DATA_INGESTION_FILE_NAME,
            feature_store_dir=os.path.join(data_ingestion_master_dir, DATA_INGESTION_FEATURE_STORE_DIR),
            failed_dir=os.path.join(data_ingestion_dir, DATA_INGESTION_FAILED_DIR),
            metadata_file_path=metadata_file_path,
            datasource_url=DATA_INGESTION_DATA_SOURCE_URL

        )
        logger.info(f"Data ingestion config: {data_ingestion_config}")
        return data_ingestion_config


    def get_data_validation_config(self) -> DataValidationConfig:
        """
        Returns DataValidationConfig
        """
        try:
            data_validation_dir = os.path.join(self.pipeline_config.artifact_dir,
                                               DATA_VALIDATION_DIR, self.timestamp)

            accepted_data_dir = os.path.join(data_validation_dir, DATA_VALIDATION_ACCEPTED_DATA_DIR)
            rejected_data_dir = os.path.join(data_validation_dir, DATA_VALIDATION_REJECTED_DATA_DIR)

            data_validation_config = DataValidationConfig(
                accepted_data_dir=accepted_data_dir,
                rejected_data_dir=rejected_data_dir,
                file_name=DATA_VALIDATION_FILE_NAME,
                missing_value_threshold= MISSING_VALUE_THRESHOLD
            )

            logger.info(f"Data preprocessing config: {data_validation_config}")

            return data_validation_config
        except Exception as e:
            raise FinanceException(e, sys)


    def get_data_transformation_config(self) -> DataTransformationConfig:
        try:
            data_transformation_dir = os.path.join(self.pipeline_config.artifact_dir,
                                                   DATA_TRANSFORMATION_DIR, self.timestamp)

            transformed_train_data_dir = os.path.join(
                data_transformation_dir, DATA_TRANSFORMATION_TRAIN_DIR
            )
            transformed_test_data_dir = os.path.join(
                data_transformation_dir, DATA_TRANSFORMATION_TEST_DIR
            )

            export_pipeline_dir = os.path.join(
                data_transformation_dir, DATA_TRANSFORMATION_PIPELINE_DIR
            )
            data_transformation_config = DataTransformationConfig(
                export_pipeline_dir=export_pipeline_dir,
                transformed_test_dir=transformed_test_data_dir,
                transformed_train_dir=transformed_train_data_dir,
                file_name=DATA_TRANSFORMATION_FILE_NAME,
                test_size=DATA_TRANSFORMATION_TEST_SIZE,
            )

            logger.info(f"Data transformation config: {data_transformation_config}")
            return data_transformation_config
        except Exception as e:
            raise FinanceException(e, sys)
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        try:
            model_trainer_dir = os.path.join(self.pipeline_config.artifact_dir,
                                             MODEL_TRAINER_DIR, self.timestamp)
            trained_model_file_path = os.path.join(
                model_trainer_dir, MODEL_TRAINER_TRAINED_MODEL_DIR, MODEL_TRAINER_MODEL_NAME
            )
            label_indexer_model_dir = os.path.join(
                model_trainer_dir, MODEL_TRAINER_LABEL_INDEXER_DIR
            )
            model_trainer_config = ModelTrainerConfig(base_accuracy=MODEL_TRAINER_BASE_ACCURACY,
                                                      trained_model_file_path=trained_model_file_path,
                                                      metric_list=MODEL_TRAINER_MODEL_METRIC_NAMES,
                                                      label_indexer_model_dir=label_indexer_model_dir
                                                      )
            logger.info(f"Model trainer config: {model_trainer_config}")
            return model_trainer_config
        except Exception as e:
            raise FinanceException(e, sys)




