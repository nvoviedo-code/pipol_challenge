import logging

from .data_processor.processor import Processor
from .web_scraper.scraper import Scraper
from .constants import URL

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
            logger.info(news_df.head())
            logger.info("Data statistics:")
            logger.info(news_df.info())
            logger.info("Data description:")
            logger.info(news_df.describe())
        else:
            logger.warning("No news data found.")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        return
    logger.info("End processing news data.")


if __name__ == "__main__":
    main()