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
git clone https://github.com/suman520-git/ecomm-prod-assistant.git
cd ecomm-prod-assistant

# Create virtual environment
conda create -p venv python==3.10 -y
conda activate venv/ 

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

```bash
# Create environment file
.env

# Edit .env with your API keys
# Required:
# - ASTRA_DB_API_ENDPOINT="xxx"
# - ASTRA_DB_APPLICATION_TOKEN="xxx"
# - ASTRA_DB_KEYSPACE="default_keyspace"
# - GOOGLE_API_KEY="xxxx"
# - OPENAI_API_KEY="xxxx"
```

### 3. API Usage

```bash
# For web scraping(Decoupled,Independent of Main RAG pipeline)
step.1 streamlit run /ecomm_prod_assistant/scrapper_ui.py



```
## Streamlit UI
![image alt](https://github.com/suman520-git/ecomm-prod-assistant/blob/main/Streamlit_ui.png?raw=true)

```bash
#Steps to the run the application(from root folder):

# first run the MCP server
step.1 python  .\ecomm-prod-assistant\prod_assistant\mcp_servers\product_search_server.py



# start the FastAPI server for the app to start 
step.2 uvicorn prod_assistant.router.main:app --reload --port 8000
# Visit http://localhost:8000



```
## Application UI
![image alt](https://github.com/suman520-git/ecomm-prod-assistant/blob/main/Application_UI.png?raw=true)


### 4.  Dockerization
```bash
# Build Docker Image
step.1 docker build -t prod-assistant .

#Run Docker Container
step.2 docker run -d -p 8000:8000 --name product-assistant prod-assistant

```

## 🆘 Support

For issues and questions:
1. Review the configuration settings
2. Ensure all API keys are properly set
3. Verify network connectivity to external services

---

