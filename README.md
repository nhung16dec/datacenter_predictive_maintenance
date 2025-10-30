# Data Center Predictive Maintenance

A personal data engineering + ML project for predictive maintenance in data centers.

A complete end-to-end **ETL and predictive maintenance pipeline** for NASA Turbofan Engine datasets.  
The goal of this project is to build a data engineering workflow that extracts, transforms, and loads (ETL) sensor data from NASA’s public datasets, stores it in a PostgreSQL database, and prepares it for machine learning models that predict Remaining Useful Life (RUL) of engines.


## Project Overview
- This project simulates a real-world data center predictive maintenance pipeline, including:
- Dockerized PostgreSQL database for structured data storage  
- ETL pipeline written in Python (extract, transform, load)  
- Logging & error handling for reliability and traceability  
- Data from NASA’s Turbofan Engine Degradation Simulation (C-MAPSS)

**Future work**
- Train a predictive maintenance model
- Serve predictions via FastAPI
- Add automated EDA (Exploratory Data Analysis) module
- Integrate Machine Learning model for RUL prediction
- Schedule ETL jobs using Apache Airflow
- Build dashboard visualization with Streamlit or Dash
- Add unit tests & CI/CD pipeline

## Project structure
datacenter_predictive_maintenance/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── data/
│ ├── FD001_train.txt
│ ├── FD001_test.txt
│ ├── RUL_FD001.txt
│ └── ...
├── src/
│ └── etl/
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│ ├── main_etl.py
│ └── logger.py
└── README.md

## Stack
Python, Pandas, FastAPI, PostgreSQL, SQLAlchemy, Docker

## ETL Pipeline Steps

### Extract  
Reads NASA turbofan engine datasets (train, test, and RUL) from local files and loads them into pandas DataFrames.

### Transform  
- Cleans and structures data  
- Renames columns ('engine_id', 'cycle', 'setting1-3', 'engine_1–21')  
- Adds dataset type labels (train/test)  
- Prepares unified schema for loading  

### Load  
- Creates PostgreSQL tables dynamically  
- Loads processed data into tables ('nasa_train', 'nasa_test')  
- Includes error handling and connection logging  

---

## Run with Docker

### Build & run containers
```bash
docker compose up --build
```
### Run only the ETL container
```bash
docker compose up etl
```
### Verify containers
```bash
docker compose ps
```
