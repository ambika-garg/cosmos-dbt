from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

# Define the DAG
dag = DAG(
    'hello_world',
    description='A simple tutorial DAG',
    schedule_interval=None,
    start_date=datetime(2023, 3, 22),
    catchup=False
)

# Define the BashOperator task
print_current_pwd = BashOperator(
    task_id='print_current_pwd',
    bash_command='echo ${pwd}',
    dag=dag
)

# airflow_home = BashOperator(
#     task_id='airflow_home',
#     bash_command='printenv AIRFLOW_HOME',
#     dag=dag
# )

list_airflow_home = BashOperator(
    task_id='list_airflow_home',
    bash_command='ls ${AIRFLOW_HOME}',
    dag=dag
)

list_requirements = BashOperator(
    task_id = "list_requirements",
    bash_command = "pip freeze"
)

# Define the task dependencies
print_current_pwd >> list_airflow_home >> list_requirements
# airflow_home >>