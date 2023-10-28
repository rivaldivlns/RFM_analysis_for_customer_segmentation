from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
import pandas as pd
import psycopg2 as db
from sqlalchemy import create_engine
from airflow.hooks.postgres_hook import PostgresHook


def clean_data():
    df = pd.read_csv('/opt/airflow/data/ecommerce.csv')

    df.columns = [column.lower() for column in df.columns]
    df.columns = df.columns.str.replace(' ', '_')

    # drop columns and rows
    df = df.dropna()
    df = df.drop('segment', axis=1)

    # type change to date
    date_columns = ["order_date", "ship_date"]
    df[date_columns] = df[date_columns].apply(pd.to_datetime)

    # Ship mode cleaning
    df = df[df ['ship_mode']!= ('45788') ]

    # Sales cleaning
    df['sales'] = df['sales'].str.replace('$',"")
    df['sales'] = df['sales'].str.replace('.',"")
    df = df[df.sales != ("0xf")]
    df = df[df.sales != ('0.5.26')]
    df['sales'] = df['sales'].str.slice(stop=-2)
    df['sales'] = df['sales'].str.slice(stop=-1)
    df['sales'] = df['sales'].astype(int)

    # Discount cleaning
    df = df[df.discount != ('xxx')] 
    df = df[df.discount != ('test')]
    df['discount'] = df['discount'].astype(float)
    df['discount'] = df['discount'] * 100

    # Shipping_cost cleaning
    df['shipping_cost'] = df['shipping_cost'].str.replace('$',"")
    df = df[df ['shipping_cost']!= ('test') ]
    df['shipping_cost'] = df['shipping_cost'].astype(float)

    # Profit cleaning
    df['profit'] = df['profit'].str.replace('$',"")
    df['profit'] = df['profit'].astype(float)

    # Quantity cleaning
    df = df[df.quantity != ("abc")] 
    df['quantity'] = df['quantity'].astype(float)

    # Dtype to integer
    type_float = ['aging', 'quantity', 'discount', 'profit', 'shipping_cost']
    for column in type_float:
        df[column] = df[column].astype(int)

    df.to_csv('/opt/airflow/dags/ecommerce_data_cleaned1.csv', index=False)

def push_postgres ():
    # Memanggil fungsi cleaning_data untuk membersihkan dataframe
    df_cleaned = pd.read_csv('/opt/airflow/dags/ecommerce_data_cleaned1.csv') # import csv clean
    # Database connection parameters
    db_params = {
        "user": "airflow",
        "password": "airflow",
        "host": "postgres",
        "port": "5434",
        "database": "airflow",
    }

    # Create an SQLAlchemy engine
    engine = create_engine(f"postgresql+psycopg2://{db_params['user']}:{db_params['password']}@{db_params['host']}/{db_params['database']}")
    table_name = "ecommerce_final_project"
    # Push the DataFrame to PostgreSQL
    df_cleaned.to_sql(table_name, engine, if_exists="replace", index=False)


# Define your Airflow DAG
default_args = {
    'owner': 'Maulana',
    'start_date': datetime(2023, 9, 29)
}

with DAG(
    "ecommerce_final_project",
    description='ecommerce_final_project',
    schedule_interval='@yearly',
    default_args=default_args,
    catchup=False
) as dag:

    # Task to clean the data
    clean_data = PythonOperator(
        task_id='clean_data',
        python_callable=clean_data,
        provide_context=True  # Pass the context to access the output of the previous task
    )

    # Task 2
    push_postgres = PythonOperator(
        task_id='push_postgres',
        python_callable=push_postgres

    )
clean_data >> push_postgres
