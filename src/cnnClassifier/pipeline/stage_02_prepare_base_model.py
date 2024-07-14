from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.prepare_base_model import PrepareBaseModel
from src.cnnClassifier import *


STAGE_NAME = "Prepare Base Model"


class PrepareBaseModelPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model() 


try:
    logger.info(f"<-------Stage {STAGE_NAME} Started------>")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f"<--------Stage {STAGE_NAME} Completed------>")
except Exception as e:
    raise e