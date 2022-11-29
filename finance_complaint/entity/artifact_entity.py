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