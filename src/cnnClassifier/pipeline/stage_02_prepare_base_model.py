# Because PYTHONPATH was set using set PYTHONPATH=%cd%, we had to remove src while importing. I do not understand why yet


from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import *


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


if __name__ == "__main__":
    try:
        logger.info(f"<-------Stage {STAGE_NAME} Started------>")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f"<--------Stage {STAGE_NAME} Completed------>")
    except Exception as e:
        raise e