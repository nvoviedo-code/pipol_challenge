from selenium import webdriver
from selenium.webdriver.common.by import By

from .exceptions import ScraperError

class Scraper():

    def __init__(self, url):
        self.url = url
        self.driver = self.__init_driver()

    def __init_driver(self):
        try:
            config = webdriver.ChromeOptions()
            config.add_argument("--headless")

            web_driver = webdriver.Chrome(options=config)
            web_driver.get(self.url)
            web_driver.implicitly_wait(10)
            return web_driver 
        except Exception as e:
            raise ScraperError(f"Driver initialization failed. {e}")

    def get_news_data(self):
        data = []
        try:
            news_items = self.driver.find_elements(By.CLASS_NAME, "contenedor_dato_modulo")
            for new in news_items:
                header = new.find_element(By.CLASS_NAME, "volanta_titulo")
                title = header.find_element(By.XPATH, f".//h2").text
                kicker = header.find_element(By.XPATH, f".//div").text
                link = new.find_element(By.XPATH, f".//a").get_attribute("href")
                image = new.find_element(By.XPATH, f".//img").get_attribute("src")
                data.append({
                    "title": title,
                    "kicker": kicker,
                    "image":image,
                    "link": link})
            self.driver.quit()
        except Exception as e:
            self.driver.quit()
            raise ScraperError(f"Error found while scraping. {e}")

        return data