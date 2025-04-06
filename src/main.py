import logging
import os

from dotenv import load_dotenv

from .data_processor.processor import Processor
from .web_scraper.scraper import Scraper
from .bigquery_client.client import BigQueryClient
from .bigquery_client.credentials_parser import Credentials
from .constants import URL

load_dotenv(override=True)
CREDENTIALS_PATH = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Main")


def main():
    logger.info("Start processing news data.")
    try:
        news_url = URL
        scrapper = Scraper(news_url)
        news_data = scrapper.get_news_data()
        if news_data:
            logger.info(f"{len(news_data)} news data retrieved successfully.")
            news_df = Processor(news_data).process()
            logger.info("Data processing completed.")

            logger.info("Getting credentials for BigQuery.")
            credentials = Credentials(CREDENTIALS_PATH)
            
            logger.info("Start inserting data into BigQuery.")
            bigquery_client = BigQueryClient(credentials)
            bigquery_client.insert_dataframe(news_df)
            logger.info("Data inserted into BigQuery successfully.")
        else:
            logger.warning("No news data found.")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        return
    logger.info("End processing news data.")


if __name__ == "__main__":
    main()