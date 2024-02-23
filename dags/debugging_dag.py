from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from pathlib import Path

DEFAULT_DBT_ROOT_PATH = Path(__file__).parent.parent / "dags" / "jaffle_shop"
SAMPLE = "ambika"

with DAG(
    dag_id="hello-world",
    start_date=datetime(2023, 8, 15),
    schedule="@once",
    tags=["tutorial"]
) as dag:
    # Tasks are represented as operators
    task1 = BashOperator(task_id="task1", bash_command="pwd")

    task2 = BashOperator(task_id="task2", bash_command="echo $DEFAULT_DBT_ROOT_PATH")

    task3 = BashOperator(task_id="task3", bash_command="echo $SAMPLE")

    task4 = BashOperator(task_id="task4", bash_command="echo task4")

    # Set dependencies between tasks
    task1 >> task2 >> task3 >> task4