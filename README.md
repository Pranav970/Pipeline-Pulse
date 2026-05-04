# 🚀 AI Pipeline Assistant v2  
### ⚡ Enterprise-Grade AI + Data Engineering Platform

<p align="center">
  <img src="https://img.shields.io/badge/Kafka-Streaming-black?style=for-the-badge&logo=apachekafka"/>
  <img src="https://img.shields.io/badge/Spark-Processing-orange?style=for-the-badge&logo=apachespark"/>
  <img src="https://img.shields.io/badge/Databricks-Lakehouse-red?style=for-the-badge&logo=databricks"/>
  <img src="https://img.shields.io/badge/Snowflake-Cloud-blue?style=for-the-badge&logo=snowflake"/>
  <img src="https://img.shields.io/badge/OpenAI-AI-green?style=for-the-badge&logo=openai"/>
  <img src="https://img.shields.io/badge/Kubernetes-Deployment-blue?style=for-the-badge&logo=kubernetes"/>
</p>

---

## 🌟 What is this?

> 🧠 An AI-powered assistant that **automatically detects, diagnoses, and fixes data pipeline failures**

This project simulates a **real enterprise data platform** where:
- Logs flow through streaming pipelines 📡  
- Data is validated and processed ⚙️  
- AI detects issues and suggests fixes 🤖  
- Everything is monitored and production-ready 📊  

---

## ✨ Key Features

🔥 **Real-Time Streaming**
- Kafka-based pipeline log ingestion  
- Spark Structured Streaming processing  

🧠 **AI Root Cause Analysis**
- Uses OpenAI to detect failure causes  
- Suggests fixes + prevention strategies  

📊 **Data Quality & Validation**
- Great Expectations checks  
- Schema drift detection  

📦 **Modern Data Stack**
- Databricks-ready notebooks  
- Snowflake ingestion layer  

📈 **Observability**
- Grafana dashboards  
- Failure tracking  

🧬 **ML + Intelligence**
- Anomaly detection using Isolation Forest  
- Log pattern learning  

🔎 **RAG + Vector Search**
- ChromaDB vector store  
- Semantic search on historical logs  

⚙️ **Production Ready**
- Airflow orchestration  
- Kubernetes deployment  
- CI/CD with GitHub Actions  

---

## 🧩 Architecture (Workflow)

```mermaid
flowchart LR

A[Kafka Log Stream 📡] --> B[Spark Streaming ⚡]
B --> C[Validation Layer ✅]
C --> D[AI Analysis 🤖]
D --> E[Vector DB 🔎]
E --> F[Snowflake ❄️]

B --> G[ML Anomaly Detection 🧠]
G --> D

F --> H[Grafana Dashboard 📊]

subgraph Orchestration
I[Airflow DAG ⚙️]
end

I --> A
