import logging
import pandas_gbq
from google.cloud import bigquery
from ..constants import BIGQUERY_NEWS_TABLE

logger = logging.getLogger("BigQueryClient")

class BigQueryClient:
    """"
    Class that handles the connection to BigQuery.
    """
    def __init__(self, credentials):
        self.project_id = credentials.project_id
        self.dataset_id = credentials.dataset_id

    def insert_dataframe(self, dataframe):
        """
        Inserts DataFrame into BigQuery.
        """
        # Query the last uploaded news to check the date       
        last_upload_date = self.get_last_upload_date()
        if last_upload_date is not None:
            dataframe = dataframe[dataframe['date'] > last_upload_date]
            logger.info(f"Selecting news after {last_upload_date}.")
        else:
            logger.info("No previous upload date found. Inserting all data.")

        
        try:            
            pandas_gbq.to_gbq(dataframe=dataframe,
                              destination_table=f'{self.dataset_id}.{BIGQUERY_NEWS_TABLE}',
                              project_id=self.project_id,
                              if_exists='append')
        except Exception as e:
            logger.error(f"Error found while inserting data: {e}")
        else:
            logger.info("Data inserted successfully.")

    def get_last_upload_date(self):
        """
        Returns the last upload date from news in BigQuery news_data table.
        """
        last_upload_date = None
        client = bigquery.Client(project=self.project_id)
        query = f"SELECT MAX(date) as last_upload_date FROM `{self.dataset_id}.{BIGQUERY_NEWS_TABLE}`"
        result = client.query(query).to_dataframe()
        if not result.empty and result['last_upload_date'][0] is not None:
            last_upload_date = result['last_upload_date'][0]
        return last_upload_date

    def head(self, n=5):
        """
        Returns the first n rows of the table. By default, n=5.
        """
        client = bigquery.Client(project=self.project_id)
        query = f"SELECT * FROM `{self.dataset_id}.{BIGQUERY_NEWS_TABLE}` LIMIT {n}"
        df = client.query(query).to_dataframe()
        return df
    
    def tail(self, n=5):
        """
        Returns the last n rows of the table. By default, n=5.
        """
        client = bigquery.Client(project=self.project_id)
        query = f"SELECT * FROM `{self.dataset_id}.{BIGQUERY_NEWS_TABLE}` ORDER BY created_at DESC LIMIT {n}"
        df = client.query(query).to_dataframe()
        return df
    