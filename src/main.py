import logging
from web_scraper.scraper import Scraper

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Main")

def main():
    logger.info("Start processing news data.")
    try:
        news_url = "https://www.yogonet.com/international/"
        scrapper = Scraper(news_url)
        news_data = scrapper.get_news_data()
        if news_data:
            logger.info(f"{len(news_data)} news data retrieved successfully.")
        else:
            logger.warning("No news data found.")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        return

if __name__ == "__main__":
    main()