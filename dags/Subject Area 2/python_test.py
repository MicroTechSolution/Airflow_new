from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
import test
import sys
import os

val = Variable.get("Path")

dag = DAG('hello_world', description='Hello World DAG',
schedule_interval='0 12 * * *',
start_date=datetime(2017, 3, 20), catchup=False)


first_task = PythonOperator(
task_id='first',
python_callable=val,
dag=dag)




first_task
