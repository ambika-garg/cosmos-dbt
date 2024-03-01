from pendulum import datetime
from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from pathlib import Path

PATH_TO_DBT_PROJECT = Path(__file__).parent.parent / "dags" / "jaffle_shop"
# PATH_TO_DBT_VENV = "<path to your venv activate binary>"


@dag(
    start_date=datetime(2023, 3, 23),
    schedule="@daily",
    catchup=False,
    dag_id="Run_DBT_in_one_go",
)
def simple_dbt_dag():
    dbt_run = BashOperator(
        task_id="dbt_run",
        # bash_command="source $PATH_TO_DBT_VENV && dbt run --models .",
        bash_command="",
        # env={"PATH_TO_DBT_VENV": PATH_TO_DBT_VENV},
        cwd=PATH_TO_DBT_PROJECT,
    )

    dbt_run


simple_dbt_dag()