from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
with DAG('pipeline_assistant',start_date=datetime(2025,1,1),schedule='@daily',catchup=False) as dag:
    BashOperator(task_id='run_producer',bash_command='python producer/log_producer.py')
