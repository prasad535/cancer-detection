from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    data_ingestion_dir: Path
    source_data_url_link: str
    local_data: Path
    data_dir: str


