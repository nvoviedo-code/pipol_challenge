import logging
from selenium import webdriver
from selenium.webdriver.common.by import By

from .cache import Cache
from .exceptions import ScraperError

logger = logging.getLogger("Scraper")

class Scraper():
    """
    Class that handles the web scraping of news data from a given URL.
    """
    def __init__(self, url):
        self.url = url
        self.cache = Cache()
        if self.cache.is_available():
            logger.info("Cache available. Loading data from cache.")
            self.__data = self.cache.retrieve_cache_data()
            self.driver = None
        else:
            self.__data = []
            self.driver = self.__init_driver()

    def __init_driver(self):
        try:
            logger.info("Initializing WebDriver.")
            config = webdriver.ChromeOptions()
            config.add_argument("--headless")
            config.add_argument("--no-sandbox")
            config.add_argument("--disable-dev-shm-usage")
            config.add_argument("--disable-gpu")
            web_driver = webdriver.Chrome(options=config)
            web_driver.implicitly_wait(10)
            logger.info("WebDriver initialized.")
            
            logger.info(f"Opening URL: {self.url}")
            web_driver.get(self.url)
            logger.info("URL opened successfully.")
        except Exception as e:
            raise ScraperError(f"Driver initialization failed. {e}")
        return web_driver

    def get_news_data(self):
        """
        Scrapes news data from the website.
        """
        if self.__data:
            logger.info("Using cached data.")
            return self.__data

        logger.info("Scraping news data.")
        if not self.driver:
            raise ScraperError("WebDriver not initialized.")
        try:
            news_items = self.driver.find_elements(By.CLASS_NAME, "contenedor_dato_modulo")
            for new in news_items:
                try:
                    header = new.find_element(By.XPATH, ".//div")
                    title = header.find_element(By.XPATH, ".//h2").text
                    kicker = header.find_element(By.XPATH, ".//div").text
                    link = new.find_element(By.XPATH, ".//a").get_attribute("href")
                    image = new.find_element(By.XPATH, ".//img").get_attribute("src")
                    self.__data.append({
                        "title": title,
                        "kicker": kicker,
                        "image":image,
                        "link": link})
                except Exception as e:
                    logger.warning(f"Error found while scraping news. {str(e)}")
                    continue
            self.driver.quit()
        except Exception as e:
            self.driver.quit()
            raise ScraperError(f"Could not find news data. {str(e)}")
        
        # Save data to cache
        self.cache.save_cache_data(self.__data)
        logger.info("News data scraped successfully.")

        return self.__data