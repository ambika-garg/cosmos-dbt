from datetime import datetime
import os
from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping
from pathlib import Path

# dbt_project_path = Path("/Users/ambikagarg/repositories/local-cosmos-dbt/dags/dbt/cosmosproject")

DEFAULT_DBT_ROOT_PATH = Path(__file__).parent.parent / "dags" / "jaffle_shop"
DBT_ROOT_PATH = Path(os.getenv("DBT_ROOT_PATH", DEFAULT_DBT_ROOT_PATH))

# Database Profile
# profile_config = ProfileConfig(
#     profile_name="default",
#     target_name="dev",
#     profile_mapping=SnowflakeUserPasswordProfileMapping(
#         conn_id="snowflake_default",
#         profile_args={
#             "database": "DEMO_DBT",
#             "schema": "PUBLIC"
#         },
#     )
# )

profile_config = ProfileConfig(
    profile_name="jaffle_shop",
    target_name="fabric-dev",
    profiles_yml_filepath=DBT_ROOT_PATH / "profiles.yml",
)

dbt_fabric_dag = DbtDag(
    project_config=ProjectConfig(DBT_ROOT_PATH,),
    operator_args={"install_deps": True},
    profile_config=profile_config,
    # execution_config=ExecutionConfig(
    #     dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt",
    # ),
    schedule_interval="@daily",
    start_date=datetime(2023, 9, 10),
    catchup=False,
    dag_id="dbt_fabric_dag",
)
