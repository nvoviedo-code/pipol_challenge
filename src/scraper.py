from selenium import webdriver
from selenium.webdriver.common.by import By

class Scraper():

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)

    def get_news_data(self):
        data = []
        news_items = self.driver.find_elements(By.CLASS_NAME, "contenedor_dato_modulo")
        for new in news_items:
            try:
                header = new.find_element(By.CLASS_NAME, 'volanta_titulo')
                title = header.find_element(By.XPATH, f".//h2").text
                kicker = header.find_element(By.XPATH, f".//div").text
                link = new.find_element(By.XPATH, f".//a").get_attribute("href")
                image = new.find_element(By.XPATH, f".//img").get_attribute("src")
                data.append({
                    "title": title,
                    "kicker": kicker,
                    "image":image,
                    "link": link})
            except Exception as e:
                print(f"Error: {e}")
        self.driver.quit()

        return data