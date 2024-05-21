from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from pathlib import Path
import os

DEFAULT_DBT_ROOT_PATH = Path(__file__).parent.parent / "dags" / "jaffle_shop"
DBT_ROOT_PATH = Path(os.getenv("DBT_ROOT_PATH", DEFAULT_DBT_ROOT_PATH))

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 5, 1),
    'email_on_failure': False,
    'email_on_retry': False,
}

# Instantiate the DAG object
with DAG(
    'hello_world_dag',
    default_args=default_args,
    description='A simple Hello World DAG',
    schedule_interval=None,
    catchup=False
) as dag:

    # Define the tasks
    hello_task = BashOperator(
        task_id='dbt_run',
        bash_command=f"dbt run  --profiles-dir {DBT_ROOT_PATH} --project-dir {DBT_ROOT_PATH}"
    )

    dbt_debug = BashOperator(
      task_id='dbt_debug',
      bash_command=f'dbt debug  --profiles-dir {DBT_ROOT_PATH} --project-dir {DBT_ROOT_PATH}'
    )

    # Set the task dependencies
    hello_task >> dbt_debug