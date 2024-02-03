from mlProject import logger
from mlProject.pipeline.Stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME="Data Ingestion Stage"
logger.info(f">>>>>>>> stage{STAGE_NAME}startd <<<<<<<< ")
data_ingestion=DataIngestionTrainingPipeline()
data_ingestion.main()

logger.info(f">>>>>>>>stage {STAGE_NAME} completed <<<<<<<")

