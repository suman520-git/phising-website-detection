import yaml
from pprint import pprint

def load_config(path="config.yaml"):
    """Load configuration from a YAML file.
    Args:
        path (str): Path to the YAML configuration file.
    """

    with open(path, "r") as file:
        config= yaml.safe_load(file)

    return config

if __name__=="__main__":
    config=load_config("config.yaml")

    # print(config)    
    pprint(config)



####################################
##  AWS and Local compatible code

# import os
# import yaml
# import boto3
# from io import StringIO
# from typing import Dict, Any


# def load_config(
#     local_path: str = "config.yaml",
#     env_path_var: str = "CONFIG_PATH",
#     s3_bucket_var: str = "S3_CONFIG_BUCKET",
#     s3_key_var: str = "S3_CONFIG_KEY",
# ) -> Dict[str, Any]:

#     # 1. Load using environment variable path
#     config_path = os.getenv(env_path_var)
#     if config_path and os.path.exists(config_path):
#         print("Loading config from environment path...")
#         return _load_yaml_file(config_path)

#     # 2. Load local file (works in Docker also)
#     if os.path.exists(local_path):
#         print("Loading config from local file...")
#         return _load_yaml_file(local_path)

#     # 3. Load from S3 (AWS production)
#     bucket = os.getenv(s3_bucket_var)
#     key = os.getenv(s3_key_var)

#     if bucket and key:
#         print("Loading config from S3...")
#         return _load_yaml_from_s3(bucket, key)

#     raise FileNotFoundError("No configuration source found.")


# def _load_yaml_file(path: str) -> Dict[str, Any]:
#     with open(path, "r") as file:
#         return yaml.safe_load(file)


# def _load_yaml_from_s3(bucket: str, key: str) -> Dict[str, Any]:
#     s3 = boto3.client("s3")
#     obj = s3.get_object(Bucket=bucket, Key=key)

#     return yaml.safe_load(StringIO(obj["Body"].read().decode("utf-8")))