from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator # type: ignore
from airflow.operators.python import PythonOperator # type: ignore

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def print_hello():
    print("Hello World!")

with DAG(
    'example_dag',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 6, 5),
    catchup=False,
) as dag:

    start = DummyOperator(
        task_id='start'
    )

    task1 = PythonOperator(
        task_id='task1',
        python_callable=print_hello
    )

    task2 = PythonOperator(
        task_id='task2',
        python_callable=print_hello
    )

    task3 = PythonOperator(
        task_id='task3',
        python_callable=print_hello
    )

    task4 = PythonOperator(
        task_id='task4',
        python_callable=print_hello
    )

    task5 = PythonOperator(
        task_id='task5',
        python_callable=print_hello
    )

    end = DummyOperator(
        task_id='end'
    )

    # Define the dependencies
    start >> task1 >> task2 >> task3 >> task4 >> task5 >> end
