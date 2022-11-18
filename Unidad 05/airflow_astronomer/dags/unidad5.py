# import the libraries

from datetime import timedelta
from airflow import DAG
from logs import logger
from airflow.utils.dates import days_ago
import pandas as pd

# defining DAG arguments
default_args = {
 'owner': 'Alkemy_Prisma',
 'start_date': days_ago(0),
 'email': ['some@somemail.com'],
 'email_on_failure': False,
 'email_on_retry': False,
 'retries': 1,
 'retry_delay': timedelta(minutes=5),
}


dag = DAG(
 'DAG_Unidad_5',
 default_args=default_args,
 description='My first DAG',
 schedule_interval=timedelta(days=1),
)


# Tasks
@dag.task(task_id="read_top10")
def read_top10():
    """Function that extract sports information from csv file and
    manage it into a xlsx file and process logs.
    """
    logger.info("...Process started...")

    try:
        # Read CSV from web
        url = "http://winterolympicsmedals.com/medals.csv"
        df = pd.read_csv(url)
        logger.info(f"...CSV was readed from online url {url}...")

    except Exception:
        url = "/usr/local/airflow/include/archivos_tmp/modals.csv"
        df = pd.read_csv(url)
        logger.error(
            f"""...online link can't be readed, the CSV
            file was readed from local url {url}...""")

    try:

        df = pd.read_csv(url)

        # Get top 10 countries with most medals
        top_countries = df.NOC.value_counts().sort_values(
            ascending=False).head(10)

        # Convert pandas series to data frame
        to_countries_df = top_countries.to_frame()

        # Save data frame in Excel format - Completar tu propia ubicación
        # para guardar el archivo de salida
        to_countries_df.to_excel(
            '/usr/local/airflow/include/archivos_tmp/top10_medalsGoals.xlsx')

        logger.info("...xls file was created succesfully...")

    except Exception:
        logger.error("...excel file can't be created...", exc_info=True)
        # If you want to make dag fail use the following line and import AirflowFailException
        # raise AirflowFailException("Error Read Top10")


# task pipeline
read_top10()
