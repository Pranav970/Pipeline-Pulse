# AI-Powered Pipeline Assistant

An AI-assisted data engineering platform that:
- Reads failed Spark / SQL / ETL logs
- Detects root causes
- Suggests fixes using ChatGPT/OpenAI
- Streams logs using Kafka
- Processes logs using Spark + Scala
- Stores analytics in Snowflake-ready schema

## Stack
- Kafka
- Spark Structured Streaming
- Scala
- Databricks-ready architecture
- FastAPI
- OpenAI API
- Docker

## Run

### 1. Start Kafka
```bash
docker-compose up -d
```

### 2. Run Log Producer
```bash
python producer/log_producer.py
```

### 3. Run AI Assistant API
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 4. Run Spark Streaming Job
```bash
spark-submit spark_jobs/log_processor.py
```

## CV Bullet
Developed an AI-assisted data engineering platform using Kafka, Spark, Scala, Databricks concepts, and ChatGPT APIs to diagnose ETL pipeline failures and auto-generate remediation suggestions.