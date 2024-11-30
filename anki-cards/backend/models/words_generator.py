import requests
from typing import Dict, List, Optional


API_ENDPOINT = "https://api.datamuse.com/words"


class WordsGenerator:
    def generate_words(
        self, topic: str, language: str = "English", n_words: int = 100
    ) -> List[str]:

        self.fetched_words = []

        try:
            self.fetched_words = self._fetch_words(topic=topic, n_words=n_words)

        except Exception as e:
            print(f"Failed to generate words on topic {topic} - {e}")

        return self.fetched_words

    def _fetch_words(self, topic: str, n_words: int) -> List[str]:

        url = f"https://api.datamuse.com/words?rel_jjb={topic}&max={n_words}&topics={topic}"

        response = requests.get(url)
        if response.status_code == 200:
            generated_words = [word["word"] for word in response.json()]
            return generated_words
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")
