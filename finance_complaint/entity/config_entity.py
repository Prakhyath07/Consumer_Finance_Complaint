from dataclasses import dataclass

@dataclass(frozen=True)
class TrainingPipelineConfig:
    pipeline_name: str
    artifact_dir: str

@dataclass(frozen=True)
class DataIngestionConfig:
    from_date: str
    to_date: str
    data_ingestion_dir: str
    download_dir: str
    file_name: str
    feature_store_dir: str
    failed_dir: str
    metadata_file_path: str
    datasource_url: str


@dataclass(frozen=True)
class DataValidationConfig:
    accepted_data_dir: str
    rejected_data_dir: str
    file_name: str
    missing_value_threshold: float





