# Because PYTHONPATH was set using set PYTHONPATH=%cd%, we had to remove src while importing. I do not understand why yet


from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_trainer import Training
from cnnClassifier import *


STAGE_NAME = "Model Trainer"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config = training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()


if __name__ == "__main__":
    try:
        logger.info(f"<------ Stage {STAGE_NAME} Started------>")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f"<------Stage {STAGE_NAME} Completed------>")
    except Exception as e:
        raise e