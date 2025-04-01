from scraper import Scraper

def main():
    news_url = "https://www.yogonet.com/international/"
    scrapper = Scraper(news_url)
    news_data = scrapper.get_news_data()
    print(news_data)


if __name__ == "__main__":
    main()