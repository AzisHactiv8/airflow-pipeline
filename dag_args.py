#Import the libraries
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

# Task 1.1 - Define DAG arguments
default_args = {
    'owner':'Azis Muslim',
    'start_date':days_ago(0),
    'email':['azis.reihan@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries':1,
    'retry_delay':timedelta(minutes = 5)
}

