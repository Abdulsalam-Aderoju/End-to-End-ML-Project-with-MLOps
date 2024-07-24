# Because PYTHONPATH was set using set PYTHONPATH=%cd%, we had to remove src while importing. I do not understand why yet


from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation_with_mlflow import Evaluation


STAGE_NAME = "Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()    


if __name__=="__main__":
    try:
        print(f"<-----Stage {STAGE_NAME} Started----->")
        obj = ModelEvaluationPipeline()
        obj.main()
        print(F"<--------Stage {STAGE_NAME} Completed")
    except Exception as e:
        raise e
    