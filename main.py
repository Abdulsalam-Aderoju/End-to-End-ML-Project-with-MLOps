# This file will be our endpoint, more like a central file for the entire project

from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f"<------Stage {STAGE_NAME} Started------>")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f"<-------Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e