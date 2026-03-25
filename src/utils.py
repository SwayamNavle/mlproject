import os
import sys
import dill

from src.exception import CustomException


def save_object(file_path, obj):
    """
    Save any Python object as a binary file using dill
    """
    try:
        dir_path = os.path.dirname(file_path)

        if dir_path != "":
            os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    """
    Load any Python object from file
    """
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)