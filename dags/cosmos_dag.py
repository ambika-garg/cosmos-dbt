from datetime import datetime
import os
from cosmos import DbtDag, ProjectConfig, ProfileConfig
from pathlib import Path

# DEFAULT_DBT_ROOT_PATH = Path(__file__).parent.parent / "dags" / "jaffle_shop"

DEFAULT_DBT_ROOT_PATH = "/opt/airflow/git/cosmos-dbt.git/dags/jaffle_shop"

DBT_ROOT_PATH = Path(os.getenv("DBT_ROOT_PATH", DEFAULT_DBT_ROOT_PATH))

profile_config = ProfileConfig(
    profile_name="jaffle_shop",
    target_name="fabric-dev",
    profiles_yml_filepath=DBT_ROOT_PATH / "profiles.yml",
)

dbt_fabric_dag = DbtDag(
    project_config=ProjectConfig(DBT_ROOT_PATH,),
    operator_args={"install_deps": True},
    profile_config=profile_config,
    schedule_interval="@daily",
    start_date=datetime(2023, 9, 10),
    catchup=False,
    dag_id="dbt_fabric_dag",
)
