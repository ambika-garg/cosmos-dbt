from pendulum import datetime
from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from pathlib import Path

DEFAULT_DBT_ROOT_PATH = Path(__file__).parent.parent / "dags" / "jaffle_shop"
# PATH_TO_DBT_VENV = "<path to your venv activate binary>"


@dag(
    start_date=datetime(2023, 3, 23),
    schedule="@daily",
    catchup=False,
    dag_id="Run_DBT_in_one_go",
)
def simple_dbt_dag():

    # && dbt run --models

    dbt_run = BashOperator(
        task_id="dbt_run",
        # bash_command="source $PATH_TO_DBT_VENV && dbt run --models .",
        bash_command="cd $DEFAULT_DBT_ROOT_PATH && dbt --version",
        env={"DEFAULT_DBT_ROOT_PATH": str(DEFAULT_DBT_ROOT_PATH)},
        # env={"PATH_TO_DBT_VENV": PATH_TO_DBT_VENV},
        cwd=DEFAULT_DBT_ROOT_PATH,
    )

    print_pwd = BashOperator(
        task_id="print_pwd",
        bash_command="pwd",
    )

    dbt_run >> print_pwd


simple_dbt_dag()