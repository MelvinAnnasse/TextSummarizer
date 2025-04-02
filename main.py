from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage1_data_ingestion_pipeline import DataIngestionPipeline

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f"Stage : {STAGE_NAME} Initiated")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_indgestion()
    logger.info(f"Stage : {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e