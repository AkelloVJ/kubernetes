from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Akello',
    'start_date': datetime(year=2024, month=1, day=25),
    'retries': 1,  # Number of retries in case of failure
    'retry_delay': timedelta(minutes=5),  # Delay between retries
}

dag = DAG(
    dag_id='hello_world',
    default_args=default_args,
    schedule_interval=timedelta(days=1),  # Schedule interval
    catchup=False,  # Skip past runs if the DAG was not running
)

t1 = BashOperator(
    task_id='hello_world',
    bash_command='echo "Hello World"',
    dag=dag,
)

t2 = BashOperator(
    task_id='hello_dml',
    bash_command='echo "Hello Data Mastery Lab"',
    dag=dag,
)

t1 >> t2
