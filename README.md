# Phising-website-detection

Detection of given url wheather Legit website or Phishing website.

##  Project Overview
# FEATURES OF THE DATASET.
![image alt](https://github.com/suman520-git/phising-website-detection/blob/main/data/features_1.png?raw=true)
![image alt](https://github.com/suman520-git/phising-website-detection/blob/main/data/features_2.png?raw=true)


1.Dataset have  30 independent features of URL which are used to predict , and 1 dependent feature to be predicted as legit or phishing website.

2.Data cleaning like removing null values ,duplicate rows have removed , EDA has done on the data.

4.Data preprocessing has done.

3.Two  models have been trained on the training dataset and tested models on the testing dataset.

4.During inference pipeline ,for the given URL , features same as 30 features from the dataset have been extracted from the given URL and passed to trained Models to get prediction like Legit or Phishing website

## Project Structure
```
phising-website-detection                       
├─ api                                          
│  ├─ templates                                 
│  │  ├─ index.html                             
│  │  └─ index_archive.html                     
│  ├─ main.py                                   
│  └─ main_archive.py                           
├─ artifacts                                    
│  ├─ ann_mlp_model.pkl                         
│  ├─ scaler.pkl                                
│  └─ xgb_model.pkl                             
├─ backend                                      
│  ├─ app.py                                    
│  └─ app__.py                                  
├─ data                                         
│  ├─ features_1.png                            
│  ├─ features_2.png                            
│  └─ phising.csv                               
├─ inference                                    
│  ├─ predictor.py                              
│  └─ __init__.py                               
├─ mlruns                                       
│  └─ 1                                         
│     └─ models                                 
│        ├─ m-ce3d2e63bdca4680b8cdfa1e4ae54004  
│        │  └─ artifacts                        
│        │     ├─ conda.yaml                    
│        │     ├─ MLmodel                       
│        │     ├─ model.pkl                     
│        │     ├─ python_env.yaml               
│        │     └─ requirements.txt              
│        └─ m-f1ca879033834835a8d7dbb8041e2d87  
│           └─ artifacts                        
│              ├─ conda.yaml                    
│              ├─ MLmodel                       
│              ├─ model.pkl                     
│              ├─ python_env.yaml               
│              └─ requirements.txt              
├─ notebook                                     
│  ├─ EDA.ipynb                                 
│  ├─ exp.ipynb                                 
│  └─ phising.csv                               
├─ src                                          
│  ├─ config_loader.py                          
│  ├─ data_loader.py                            
│  ├─ pipeline.py                               
│  ├─ preprocessor.py                           
│  ├─ train_ann.py                              
│  ├─ train_xgboost.py                          
│  ├─ utils.py                                  
│  ├─ website_feature_extraction.py             
│  └─ __init__.py                               
├─ templates                                    
│  └─ index.html                                
├─ config.yaml                                  
├─ Dockerfile                                   
├─ mlflow.db                                    
├─ pyproject.toml                               
├─ README.md                                    
├─ requirements.txt                             
├─ run_pipeline.py                              
└─ setup.py                                     

```

## 🚀 Quick Start

### 1. Environment Setup

```bash
# Clone the repository
git clone https://github.com/suman520-git/phising-website-detection.git
cd phising-website-detection

# Create virtual environment
conda create -p venv python==3.11 -y
conda activate venv/ 

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuring the MLFLOW in the project

```bash
# commnds 
step.1  pip install  mlflow
step.2  mlflow ui

visit for mlflow ui : 127.0.0.1:5000
```

## MLFLOW UI
![image alt](https://github.com/suman520-git/phising-website-detection/blob/main/MLflow-1.png?raw=true)


### 3. Training ML models

```bash
# For training the models on the dataset
step.1  python -m run_pipeline

```

### 4. API Usage

```bash
# For running the application through Fastapi(command for running the ml application)
step.1  uvicorn api.main:app --reload

```
## ML Application UI
![image alt](https://github.com/suman520-git/phising-website-detection/blob/main/ML-UI.png?raw=true)



### 5.  Dockerization
```bash
# Build Docker Image
step.1 docker build -t test .

#Run Docker Container
step.2 docker run --rm -p 8000:8005 test

```

### 6. Deployment to AWS APP Runner
```bash
Repository secrets

1. AWS_ACCESS_KEY_ID = "xxxxx"
2. AWS_SECRET_ACCESS_KEY = "xxxxx"
3. AWS_REGION = "xxxxx"
4. ECR_REPO = "xxxxx"

Create ECR repo copy the URI and keep it to ECR_REPO
Create a IAM user a provide this permission: AdministratorAccess

```
###########################################################################################

# Phising-website-detection(LLM Powered)

## Gen-AI Application UI
![image alt](https://github.com/suman520-git/phising-website-detection/blob/main/Gen_UI.png?raw=true)


### 1. Create environment file (Edit .env with your API keys)


```bash
1. GROQ_API_KEY = "xxxxx"
2. GROQ_MODEL= "xxxxx"

```
### 2. API Usage

```bash
# For running the application through Fastapi(command for running the Gen AI application)
step.1  uvicorn backend.app:app --reload

```