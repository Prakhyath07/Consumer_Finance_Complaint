from dataclasses import dataclass

@dataclass(frozen = True)
class DataIngestionArtifact:
    feature_store_file_path: str
    metadata_file_path: str
    download_dir: str

@dataclass(frozen=True)
class DataValidationArtifact:
    accepted_file_path: str
    rejected_dir: str


@dataclass(frozen=True)
class DataTransformationArtifact:
    transformed_train_file_path: str
    exported_pipeline_file_path: str
    transformed_test_file_path: str