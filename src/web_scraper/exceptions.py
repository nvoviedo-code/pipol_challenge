# Define exceptions for scraper module

class ScraperError(Exception):
    def __init__(self, message):
        self.message = f"[ScraperError] {message}"
        super().__init__(self.message)
