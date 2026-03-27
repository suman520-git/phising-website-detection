import pandas as pd
from pprint import pprint

from src.utils import print_header

def load_dataset(path: str)-> pd.DataFrame:
    """Load dataset from a CSV file.
    Args:
        path (str): Path to the CSV file.
    """

    print_header("LOADING DATASET")

    df=pd.read_csv(path)

    print(f"Dataset loaded with shape: {df.shape}")
    return df


if __name__== "__main__":
    df=load_dataset("data/phising.csv") 

    pprint(df.head())   

#######################################

#   AWS cloud  and  Local Compatible Code

# import os
# from io import StringIO
# from pprint import pprint

# import pandas as pd
# import boto3

# from src.utils import print_header


# def load_dataset(local_path: str = "data/phising.csv") -> pd.DataFrame:
#     """
#     Load dataset from:
#         1. S3 (if environment variables exist)
#         2. Local file (fallback)

#     Environment variables used:
#         S3_BUCKET_NAME
#         S3_FILE_KEY
#     """

#     print_header("LOADING DATASET")

#     bucket_name = os.getenv("S3_BUCKET_NAME")
#     file_key = os.getenv("S3_FILE_KEY")

#     # Case 1: Load from S3
#     if bucket_name and file_key:
#         print("Loading dataset from S3...")

#         s3 = boto3.client("s3")
#         obj = s3.get_object(Bucket=bucket_name, Key=file_key)

#         df = pd.read_csv(StringIO(obj["Body"].read().decode("utf-8")))

#     # Case 2: Load locally
#     else:
#         print("Loading dataset from local path...")
#         df = pd.read_csv(local_path)

#     print(f"Dataset loaded successfully. Shape: {df.shape}")
#     return df


# if __name__ == "__main__":
#     df = load_dataset()
#     pprint(df.head())