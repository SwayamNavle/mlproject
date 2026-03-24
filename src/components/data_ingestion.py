import os
import sys
import pandas as pd
import logging
from sklearn.model_selection import train_test_split

# Make sure these are properly defined in your project
from src.exception import CustomException
from src.logger import logging


class DataIngestionConfig:
    def __init__(self):
        self.train_data_path = os.path.join("artifacts", "train.csv")
        self.test_data_path = os.path.join("artifacts", "test.csv")
        self.raw_data_path = os.path.join("artifacts", "data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered Data ingestion method or component")

        try:
            # ✅ Correct file path
            df = pd.read_csv("notebook/data/stud.csv")
            logging.info("Dataset read successfully")

            # ✅ FIXED syntax (missing comma earlier)
            os.makedirs(
                os.path.dirname(self.ingestion_config.train_data_path),
                exist_ok=True
            )

            # ✅ Save raw data
            df.to_csv(
                self.ingestion_config.raw_data_path,
                index=False,
                header=True
            )

            logging.info("Train-Test Split initiated")

            train_set, test_set = train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )

            # ✅ FIXED: Save both train & test correctly
            train_set.to_csv(
                self.ingestion_config.train_data_path,
                index=False,
                header=True
            )

            test_set.to_csv(
                self.ingestion_config.test_data_path,
                index=False,
                header=True
            )

            logging.info("Data ingestion completed successfully")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.error(f"Error occurred: {e}")
            raise CustomException(e, sys)


# ✅ Ensure execution happens
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()