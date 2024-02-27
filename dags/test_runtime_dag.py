import time
from datetime import datetime
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

def test(**context):
    time.sleep(10)

default_args = {
    "owner": 'Airflow',
    "start_date": datetime(2021, 1, 1),
}

dag = DAG(
    dag_id='test_50_task_1',
    schedule_interval="@once",
    default_args=default_args,
    catchup=False
)

with dag:
    for i in range(10):
        task = PythonOperator(
            task_id=f"task_{i}",
            python_callable=test,
            provide_context=True
        )