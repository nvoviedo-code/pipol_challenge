import logging
import pandas as pd


logger = logging.getLogger("Processor")


class Processor:
    def __init__(self, data):
        self.data = data

    def calculate_word_count(self, title):
        return len(title.split())

    def calculate_character_count(self, title):
        return len(title.strip())

    def list_capitalized_words(self, title):
        words = title.split()
        return [word for word in words if word[0].isupper()]

    def process(self):
        # Create a DataFrame from the scraped data
        df = pd.DataFrame(self.data)

        # Add new features
        df['title_word_count'] = df['title'].apply(self.calculate_word_count)
        df['title_character_count'] = df['title'].apply(
            self.calculate_character_count)
        df['capitalized_words'] = df['title'].apply(
            self.list_capitalized_words)

        return df
