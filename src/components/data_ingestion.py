import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation


class DataIngestionConfig:
    def __init__(self):
        self.train_data_path = os.path.join("artifacts", "train.csv")
        self.test_data_path = os.path.join("artifacts", "test.csv")
        self.raw_data_path = os.path.join("artifacts", "data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """
        Reads raw dataset, splits into train/test, and saves them
        """
        logging.info("Entered Data Ingestion")

        try:
            df = pd.read_csv("notebook/data/stud.csv")

            logging.info("Dataset loaded successfully")

            os.makedirs("artifacts", exist_ok=True)

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Raw data saved")

            # Train-test split
            train_set, test_set = train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )

            train_set.to_csv(self.ingestion_config.train_data_path, index=False)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False)

            logging.info("Train-test split completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    logging.info("Pipeline started")

    obj = DataIngestion()

    train_data, test_data = obj.initiate_data_ingestion()

    logging.info("Starting data transformation")

    data_transformation = DataTransformation()

    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(
        train_data, test_data
    )

    logging.info("Pipeline completed successfully")

    print("✅ Full pipeline executed successfully")