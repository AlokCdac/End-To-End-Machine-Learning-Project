from mlProject import logger
from mlProject.pipeline.Stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.Stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.Stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.Stage_04_model_trainer import ModelTrainerTrainingPipeline

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


STAGE_NAME="Data Transformation"
try:
        logger.info(f">>>>>>>> stage{STAGE_NAME}startd <<<<<<<< ")
        data_transformation=DataTransformationTrainingPipeline()
        data_transformation.main()

        logger.info(f">>>>>>>>stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    raise e


STAGE_NAME="Model_training"

try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        Model_training = ModelTrainerTrainingPipeline()
        Model_training.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
