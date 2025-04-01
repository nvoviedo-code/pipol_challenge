import pytest
from unittest.mock import patch

from src.scraper import Scraper


@pytest.fixture
def scraper():
    url = "https://example.com"
    with patch("src.scraper.webdriver") as mock_webdriver:
        mock_webdriver.Chrome.return_value.get.return_value = None
        mock_webdriver.Chrome.return_value.find_elements.return_value = [
            mock_webdriver.Chrome.return_value
        ]
        mock_webdriver.Chrome.return_value.find_element.return_value = mock_webdriver.Chrome.return_value
        mock_webdriver.Chrome.return_value.find_element.return_value.text = "Test Example"
        mock_webdriver.Chrome.return_value.find_element.return_value.get_attribute.return_value = "https://example.com/test"
        return Scraper(url)


def test_get_data(scraper):
    data = scraper.get_news_data()
    assert data is not None, "Data should not be None"
    assert isinstance(data, list), "Data should be a list"
    assert isinstance(data[0], dict), "List elements should be dictionaries"
    assert data[0]["title"] == "Test Example", "Unexpected title data"
    assert data[0]["kicker"] == "Test Example", "Unexpected kicker data"
    assert data[0]["image"] == "https://example.com/test", "Unexpected image data"
    assert data[0]["link"] == "https://example.com/test", "Unexpected link data"
