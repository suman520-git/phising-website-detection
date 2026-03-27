import joblib
import mlflow
import mlflow.sklearn
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report
from src.utils import print_header


def train_ann(X_train, X_test, y_train, y_test, params, save_path):
    print_header("TRAINING ANN MLPClassifier (MLflow Enabled)")

    # FIX: config compatibility
    params = params.copy()
    if "hidden_layers" in params:
        params["hidden_layer_sizes"] = tuple(params["hidden_layers"])
        del params["hidden_layers"]

    with mlflow.start_run(run_name="ANN_MLP_Phishing"):

        # 🔹 Log hyperparameters
        mlflow.log_params(params)

        ann = MLPClassifier(**params)
        ann.fit(X_train, y_train)

        preds = ann.predict(X_test)

        acc = accuracy_score(y_test, preds)
        report = classification_report(y_test, preds, output_dict=True)

        # 🔹 Log metrics
        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("precision", report["1"]["precision"])
        mlflow.log_metric("recall", report["1"]["recall"])
        mlflow.log_metric("f1_score", report["1"]["f1-score"])

        # 🔹 Save locally
        joblib.dump(ann, save_path)

        # 🔹 Log model to MLflow
        mlflow.sklearn.log_model(ann, artifact_path="ann_model")

        print("ANN Accuracy:", acc)
        print("Report:\n", classification_report(y_test, preds))
        print(f"ANN model saved → {save_path}")

###################################################################

        ## AWS-compatible version of your code

# import os
# import joblib
# import boto3
# import mlflow
# import mlflow.sklearn
# from io import BytesIO
# from pathlib import Path
# from sklearn.neural_network import MLPClassifier
# from sklearn.metrics import accuracy_score, classification_report

# from src.utils import print_header


# def train_ann(X_train, X_test, y_train, y_test, params, model_filename="ann_model.pkl"):
#     print_header("TRAINING ANN MLPClassifier (MLflow Enabled - AWS Compatible)")

#     # -------- Fix config compatibility --------
#     params = params.copy()
#     if "hidden_layers" in params:
#         params["hidden_layer_sizes"] = tuple(params["hidden_layers"])
#         del params["hidden_layers"]

#     # -------- MLflow remote tracking support --------
#     # Set via environment variables in AWS
#     # Example:
#     # MLFLOW_TRACKING_URI = http://<ec2-ip>:5000
#     # or s3://mlflow-artifacts-bucket
#     mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", "mlruns"))

#     with mlflow.start_run(run_name="ANN_MLP_Phishing"):

#         # Log hyperparameters
#         mlflow.log_params(params)

#         # -------- Train model --------
#         ann = MLPClassifier(**params)
#         ann.fit(X_train, y_train)

#         preds = ann.predict(X_test)

#         acc = accuracy_score(y_test, preds)
#         report = classification_report(y_test, preds, output_dict=True)

#         # -------- Log metrics --------
#         mlflow.log_metric("accuracy", acc)
#         mlflow.log_metric("precision", report["1"]["precision"])
#         mlflow.log_metric("recall", report["1"]["recall"])
#         mlflow.log_metric("f1_score", report["1"]["f1-score"])

#         # -------- Save model locally (works in Docker/CI/CD) --------
#         artifacts_dir = Path(os.getenv("ARTIFACTS_DIR", "artifacts"))
#         artifacts_dir.mkdir(parents=True, exist_ok=True)

#         model_path = artifacts_dir / model_filename
#         joblib.dump(ann, model_path)

#         print(f"Model saved locally → {model_path}")

#         # -------- Upload model to AWS S3 --------
#         bucket = os.getenv("S3_BUCKET_NAME")
#         s3_model_path = os.getenv("S3_MODEL_PATH", "models")

#         if bucket:
#             print("Uploading model to S3...")

#             s3 = boto3.client("s3")
#             s3.upload_file(str(model_path), bucket, f"{s3_model_path}/{model_filename}")

#             print("Model uploaded to S3 successfully.")

#         # -------- Log model to MLflow (remote storage supported) --------
#         mlflow.sklearn.log_model(ann, artifact_path="ann_model")

#         print("ANN Accuracy:", acc)
#         print("Report:\n", classification_report(y_test, preds))        