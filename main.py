from mlProject import logger
from mlProject.pipeline.Stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.Stage_02_data_validation import DataValidationTrainingPipeline


STAGE_NAME="Data Ingestion Stage"
try:

    logger.info(f">>>>>>>> stage{STAGE_NAME}startd <<<<<<<< ")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()

    logger.info(f">>>>>>>>stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Validation"
try:
    logger.info(f">>>>>>>> stage{STAGE_NAME}startd <<<<<<<< ")
    data_validation=DataValidationTrainingPipeline()
    data_validation.main()

    logger.info(f">>>>>>>>stage {STAGE_NAME} completed <<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e




