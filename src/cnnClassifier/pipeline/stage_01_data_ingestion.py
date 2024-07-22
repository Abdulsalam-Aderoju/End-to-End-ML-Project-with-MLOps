# Because PYTHONPATH was set using set PYTHONPATH=%cd%, we had to remove src while importing. I do not understand why yet

from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger


STAGE_NAME = "Data Ingestion"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_files()
        data_ingestion.extract_zip_file()



if __name__ == "__main__":
    try:
        logger.info(f"<------Stage {STAGE_NAME} Started------>")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f"<-------Stage {STAGE_NAME} Completed------>")
    except Exception as e:
        logger.exception(e)
        raise e