from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage1_data_ingestion_pipeline import DataIngestionPipeline
from src.textSummarizer.pipeline.stage2_data_transformation_pipeline import DatatransformationPipeline
from src.textSummarizer.pipeline.stage3_model_trainer_pipeline import ModelTrainerTrainingPipeline

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f"Stage : {STAGE_NAME} Initiated")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_indgestion()
    logger.info(f"Stage : {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Transformation"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_transformation_pipeline= DatatransformationPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Trainer stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    model_trainer_pipeline=ModelTrainerTrainingPipeline()
    model_trainer_pipeline.initiate_model_trainer()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e