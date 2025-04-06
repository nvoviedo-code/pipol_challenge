import pytest
from src.data_processor.processor import Processor

@pytest.fixture
def processor():
    data = [
        {'title': 'GLI names Sangeeta Reddy as Vice President of new Innovation division',
         'kicker': 'FORMER VP OF ENGINEERING',
         'image': 'https://test/data/imagenes/2025/04/01/74192/1743521964-gli-sangeeta-reddy-vp-innovation.jpg',
         'link': 'https://test/news/2025/04/02/100136-gli-names-sangeeta-reddy-as-vice-president-of-new-innovation-division'},
         {'title': 'Zitro to showcase Concept cabinet line, new games at GAT Expo 2025 ',
          'kicker': 'APRIL 28 TO 30, BOOTH A21',
          'image': 'https://test/data/imagenes/2025/04/03/74266/1743692206-zitro-gat-expo-cartagena-2025.jpg',
          'link': 'https://test/news/2025/04/04/100352-zitro-to-showcase-concept-cabinet-line-new-games-at-gat-expo-2025'}
    ]
    return Processor(data)

def test_calculate_word_count(processor):
    title = "Breaking News: Testing processor word count"
    result = processor.calculate_word_count(title)
    assert result == 6

def test_calculate_character_count(processor):
    title = "Breaking News: Testing processor character count"
    result = processor.calculate_character_count(title)
    assert result == 48

def test_list_capitalized_words(processor):
    title = "Breaking News: Testing processor Capitalized words"
    result = processor.list_capitalized_words(title)
    assert result == ["Breaking", "News:", "Testing", "Capitalized"]

def test_process(processor):
    df = processor.process()

    assert "title_word_count" in df.columns
    assert "title_character_count" in df.columns
    assert "capitalized_words" in df.columns

    assert df["title_word_count"].iloc[0] == 11
    assert df["title_character_count"].iloc[0] == 69
    assert df["capitalized_words"].iloc[0] == '["GLI", "Sangeeta", "Reddy", "Vice", "President", "Innovation"]'

    # Check dataframe structure
    assert df.shape[0] == 2, "DataFrame should have 2 rows"
    assert df.shape[1] == 8, "DataFrame should have 8 columns"

    assert isinstance(df["title"].iloc[0], str)
    assert isinstance(df["kicker"].iloc[0], str)
    assert isinstance(df["image"].iloc[0], str)
    assert isinstance(df["link"].iloc[0], str)
