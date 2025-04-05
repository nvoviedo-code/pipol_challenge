import logging
import pandas_gbq
from google.cloud import bigquery


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
        try:            
            pandas_gbq.to_gbq(dataframe=dataframe,
                              destination_table=f'{self.dataset_id}.news_data',
                              project_id=self.project_id,
                              if_exists='fail')
        except Exception as e:
            logger.error(f"Error found while inserting data: {e}")
        else:
            logger.info("Data inserted successfully.")

    def head(self, n=5):
        """
        Returns the first n rows of the table. By default, n=5.
        """
        client = bigquery.Client(project=self.project_id)
        query = f"SELECT * FROM `{self.dataset_id}.news_data` LIMIT {n}"
        df = client.query(query).to_dataframe()
        return df
    
    def tail(self, n=5):
        """
        Returns the last n rows of the table. By default, n=5.
        """
        client = bigquery.Client(project=self.project_id)
        query = f"SELECT * FROM `{self.dataset_id}.news_data` ORDER BY created_at DESC LIMIT {n}"
        df = client.query(query).to_dataframe()
        return df
    
