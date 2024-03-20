import os
import sys
import logging

LOGGING_STR = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

LOG_DIR = "logs"
log_file_path = os.path.join(LOG_DIR,"history_logs.log")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format= LOGGING_STR,

    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cancerLogger")