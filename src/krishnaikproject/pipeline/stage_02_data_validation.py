from src.krishnaikproject.constants import *
from src.krishnaikproject.utils.common import read_yaml, create_directories
from src.krishnaikproject.config.configuration import ConfigurationManager
from src.krishnaikproject.components.data_validation import DataValidation
from src.krishnaikproject import logger 


STAGE_NAME = 'Data Validation Stage'

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        
        config= ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config= data_validation_config)
        data_validation.validate_all_columns()
            
            

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>stage{STAGE_NAME}started<<<<<<<<<")
        data_validation = DataValidationTrainingPipeline()
        data_validation.main()
        logger.info(f">>>>>>>>>stage {STAGE_NAME} completed<<<<<<<<<<")

    except Exception as e:
        raise e

