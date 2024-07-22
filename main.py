# This file will be our endpoint, more like a central file for the entire project

from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from src.cnnClassifier.pipeline.stage_03_model_trainer import ModelTrainerPipeline
from src.cnnClassifier.pipeline.stage_04_model_evaluation_with_mlflow import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f"<------Stage {STAGE_NAME} Started------>")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f"<-------Stage {STAGE_NAME} Completed------>")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f"<-------Stage {STAGE_NAME} Started------>")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f"<--------Stage {STAGE_NAME} Completed------>")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Model Trainer"

try:
    logger.info(f"<------ Stage {STAGE_NAME} Started------>")
    obj = ModelTrainerPipeline()
    obj.main()
    logger.info(f"<------Stage {STAGE_NAME} Completed------>")
except Exception as e:
    logger.exception(e)
    raise e 




STAGE_NAME = "Model Evaluation"

try:
   print(f"<-----Stage {STAGE_NAME} Started----->")
   obj = ModelEvaluationPipeline()
   obj.main()
   print(F"<--------Stage {STAGE_NAME} Completed------>")
except Exception as e:
   logger.exception(e)
   raise e
    