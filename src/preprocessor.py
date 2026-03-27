import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from src.utils import print_header, ensure_artifacts_dir

def preprocess_data(df, target_col, test_size, random_state, scaler_path):
    print_header("PREPROCESSING DATA")

    df[target_col] = df[target_col].map({-1: 0, 1: 1})

    X = df.drop(target_col, axis=1)
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Create artifacts directory properly
    ensure_artifacts_dir(os.path.dirname(scaler_path))

    # Save scaler
    joblib.dump(scaler, scaler_path)
    print(f"Scaler saved → {scaler_path}")

    return X_train_scaled, X_test_scaled, y_train, y_test




#################################
#######   AWS-compatible code $$$$$$$$$

# import os
# import joblib
# import boto3
# import pandas as pd
# from pathlib import Path
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler

# from src.utils import print_header, ensure_artifacts_dir


# def preprocess_data(df, target_col, test_size, random_state, scaler_filename="scaler.pkl"):
#     print_header("PREPROCESSING DATA")

#     # Convert target values
#     df[target_col] = df[target_col].map({-1: 0, 1: 1})

#     # Split features and labels
#     X = df.drop(target_col, axis=1)
#     y = df[target_col]

#     X_train, X_test, y_train, y_test = train_test_split(
#         X, y,
#         test_size=test_size,
#         random_state=random_state,
#         stratify=y
#     )

#     # Scaling
#     scaler = StandardScaler()
#     X_train_scaled = scaler.fit_transform(X_train)
#     X_test_scaled = scaler.transform(X_test)

#     # -------- Cloud-compatible artifact handling --------

#     # Get artifacts directory from environment variable
#     artifacts_dir = ensure_artifacts_dir()

#     scaler_path = Path(artifacts_dir) / scaler_filename

#     # Save scaler locally (works in Docker / EC2 / CI/CD)
#     joblib.dump(scaler, scaler_path)
#     print(f"Scaler saved locally → {scaler_path}")

#     # Upload to S3 if bucket is provided (production environment)
#     s3_bucket = os.getenv("S3_BUCKET_NAME")
#     s3_path = os.getenv("S3_SCALER_PATH", "models")

#     if s3_bucket:
#         print("Uploading scaler to S3...")

#         s3 = boto3.client("s3")
#         s3.upload_file(str(scaler_path), s3_bucket, f"{s3_path}/{scaler_filename}")

#         print("Scaler uploaded to S3 successfully.")

#     return X_train_scaled, X_test_scaled, y_train, y_test