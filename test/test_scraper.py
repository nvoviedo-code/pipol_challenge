import pytest
from unittest.mock import Mock, patch

from src.web_scraper.exceptions import ScraperError
from src.web_scraper.scraper import Scraper

URL = "https://example.com"
EXAMPLE_LINK = "https://example.com/link"

def init_scraper(cache = False):
    with (patch("src.web_scraper.scraper.webdriver") as mock_webdriver,
        patch("src.web_scraper.scraper.Cache") as mock_cache):
        mock_webdriver.Chrome.return_value.get.return_value = None
        mock_webdriver.Chrome.return_value.find_elements.return_value = [
            mock_webdriver.Chrome.return_value
        ]
        mock_webdriver.Chrome.return_value.find_element.return_value = mock_webdriver.Chrome.return_value
        mock_webdriver.Chrome.return_value.find_element.return_value.text = "Test Example"
        mock_webdriver.Chrome.return_value.find_element.return_value.get_attribute.return_value = EXAMPLE_LINK
        
        mock_cache.return_value.is_available.return_value = cache
        mock_cache.return_value.retrieve_cache_data.return_value = [
            {
                "title": "Cache Example",
                "kicker": "Cache Example",
                "image": EXAMPLE_LINK,
                "link": EXAMPLE_LINK
            }
        ]       
        return Scraper(URL)
    
@pytest.fixture
def scraper_ok():
    return init_scraper()

@pytest.fixture
def scraper_cache_available():
    return init_scraper(cache=True)

@pytest.fixture
def scraper_web_driver_error():
    with (patch("src.web_scraper.scraper.webdriver") as mock_webdriver,
        patch("src.web_scraper.scraper.Cache") as mock_cache):
        mock_webdriver.Chrome.side_effect = Exception("WebDriver error")
        mock_cache.return_value.is_available.return_value = False
        return Scraper(URL)
    
@pytest.fixture
def scraper_find_elements_error():
    with (patch("src.web_scraper.scraper.webdriver") as mock_webdriver,
        patch("src.web_scraper.scraper.Cache") as mock_cache):
        mock_webdriver.Chrome.return_value.find_elements.side_effect = Exception("no such element")
        mock_cache.return_value.is_available.return_value = False
        return Scraper(URL)
    
@pytest.fixture
def scraper_find_elemets_empty():
    with (patch("src.web_scraper.scraper.webdriver") as mock_webdriver,
        patch("src.web_scraper.scraper.Cache") as mock_cache):
        mock_webdriver.Chrome.return_value.find_elements.return_value = []
        mock_cache.return_value.is_available.return_value = False
        return Scraper(URL)
    
@pytest.fixture
def scraper_find_element_error():
    find_element_mock = Mock()
    find_element_mock.find_element.side_effect = Exception("no such element")
    with (patch("src.web_scraper.scraper.webdriver") as mock_webdriver,
          patch("src.web_scraper.scraper.Cache") as mock_cache):
        mock_webdriver.Chrome.return_value.find_elements.return_value = [
            find_element_mock,
        ]
        mock_cache.return_value.is_available.return_value = False
        return Scraper(URL)

def test_init_driver_error():
    with (patch("src.web_scraper.scraper.webdriver") as mock_webdriver,
        patch("src.web_scraper.scraper.Cache") as mock_cache):
        mock_webdriver.Chrome.side_effect = Exception("WebDriver error")
        mock_cache.return_value.is_available.return_value = False
        with pytest.raises(Exception) as exception_raised:
            Scraper(URL)
        assert exception_raised.type == ScraperError, "Unexpected Exception type"
        expected_message = "[ScraperError] Driver initialization failed. WebDriver error"
        assert str(exception_raised.value) == expected_message, "Unexpected error message"

def test_get_data(scraper_ok):
    data = scraper_ok.get_news_data()
    assert data is not None, "Data should not be None"
    assert isinstance(data, list), "Data should be a list"
    assert isinstance(data[0], dict), "List elements should be dictionaries"
    assert data[0]["title"] == "Test Example", "Unexpected title data"
    assert data[0]["kicker"] == "Test Example", "Unexpected kicker data"
    assert data[0]["image"] == EXAMPLE_LINK, "Unexpected image data"
    assert data[0]["link"] == EXAMPLE_LINK, "Unexpected link data"

def test_get_news_error(scraper_find_elements_error):
    with pytest.raises(Exception) as exception_raised:
        scraper_find_elements_error.get_news_data()
    assert exception_raised.type == ScraperError, "Unexpected Exception type"
    expected_message = "[ScraperError] Could not find news data. no such element"
    assert str(exception_raised.value) == expected_message, "Unexpected error message"

def test_get_news_data_empty(scraper_find_elemets_empty):  
        data = scraper_find_elemets_empty.get_news_data()
        assert data == [], "Data should be an empty list"

def test_get_news_details_error(scraper_find_element_error, caplog):
    with caplog.at_level("WARNING"):
        scraper_find_element_error.get_news_data()
    assert "Error found while scraping news. no such element" in caplog.text

def test_get_news_data_cache(scraper_cache_available):
    data = scraper_cache_available.get_news_data()
    assert data is not None, "Data should not be None"
    assert data[0]["title"] == "Cache Example", "Unexpected title data"
    assert data[0]["kicker"] == "Cache Example", "Unexpected kicker data"
    assert data[0]["image"] == EXAMPLE_LINK, "Unexpected image data"
    assert data[0]["link"] == EXAMPLE_LINK, "Unexpected link data"
