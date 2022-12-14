from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen = True)
class DataIngestionArtifact:
    feature_store_file_path: str
    metadata_file_path: str
    download_dir: str

    def to_dict(self):
        return self.__dict__

@dataclass(frozen=True)
class DataValidationArtifact:
    accepted_file_path: str
    rejected_dir: str

    def to_dict(self):
        return self.__dict__


@dataclass(frozen=True)
class DataTransformationArtifact:
    transformed_train_file_path: str
    exported_pipeline_file_path: str
    transformed_test_file_path: str

    def to_dict(self):
        return self.__dict__

@dataclass(frozen=True)
class PartialModelTrainerRefArtifact:
    trained_model_file_path: str
    label_indexer_model_file_path: str

    def _asdict(self):
        return self.__dict__

@dataclass(frozen=True)
class PartialModelTrainerMetricArtifact:
    f1_score: float
    precision_score: float
    recall_score: float

    def _asdict(self):
        return self.__dict__

class ModelTrainerArtifact:

    def __init__(self, model_trainer_ref_artifact: PartialModelTrainerRefArtifact,
                 model_trainer_train_metric_artifact: PartialModelTrainerMetricArtifact,
                 model_trainer_test_metric_artifact: PartialModelTrainerMetricArtifact
                 ):
        self.model_trainer_ref_artifact = model_trainer_ref_artifact
        self.model_trainer_train_metric_artifact = model_trainer_train_metric_artifact
        self.model_trainer_test_metric_artifact = model_trainer_test_metric_artifact

    def _asdict(self):
        try:
            response = dict()
            response['model_trainer_ref_artifact'] = self.model_trainer_ref_artifact._asdict()
            response['model_trainer_train_metric_artifact'] = self.model_trainer_train_metric_artifact._asdict()
            response['model_trainer_test_metric_artifact'] = self.model_trainer_test_metric_artifact._asdict()
            return response
        except Exception as e:
            raise e


class ModelEvaluationArtifact:

    def __init__(self, model_accepted, changed_accuracy, trained_model_path, best_model_path, active):
        self.model_accepted = model_accepted
        self.changed_accuracy = changed_accuracy
        self.trained_model_path = trained_model_path
        self.best_model_path = best_model_path
        self.active = active
        self.created_timestamp = datetime.now()

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return str(self.to_dict())

@dataclass(frozen=True)
class ModelPusherArtifact:
    model_pushed_dir: str

    def to_dict(self):
        return self.__dict__