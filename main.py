
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))


from Gistgen.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

from Gistgen.logging import logger


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



