from web_scraper.scraper import Scraper

def main():
    try:
        news_url = "https://www.yogonet.com/international/"
        scrapper = Scraper(news_url)
        news_data = scrapper.get_news_data()
    except Exception as e:
        print(f"Error occurred: {e}")
        return

if __name__ == "__main__":
    main()