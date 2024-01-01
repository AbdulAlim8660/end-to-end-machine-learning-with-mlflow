from src.krishnaikproject import logger
from src.krishnaikproject.pipeline.stage_01_data_ingestion import (DataIngestionTrainingPipeline)
from src.krishnaikproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.krishnaikproject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.krishnaikproject.pipeline.stage_04_model_trainer import   ModelTrainingPipeline


STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f">>>>>>>>stage {STAGE_NAME} started<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
    logger.exception(e)


STAGE_NAME = 'Data Validation Stage'

try:
    logger.info(f">>>>>>>stage{STAGE_NAME}started<<<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>>stage {STAGE_NAME} completed<<<<<<<<<<")

except Exception as e:
    raise e


STAGE_NAME = 'Data Transformation Stage'

try:
    logger.info(f">>>>>>>stage{STAGE_NAME}started<<<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>>>stage {STAGE_NAME} completed<<<<<<<<<<")

except Exception as e:
    raise e

STAGE_NAME = 'Model Training'

try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started<<<<<<<<<<<<")
    modeltraining = ModelTrainingPipeline
    ModelTrainingPipeline.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed<<<<<<<<<<<")

except Exception as e:
    raise e