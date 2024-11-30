import pandas as pd


class DatasetGenerator:
    def generate_dataset(
        self, source_lang, target_lang, words: dict = {}
    ) -> pd.DataFrame:

        dataframe = pd.DataFrame(words.items(), columns=[source_lang, target_lang])

        return dataframe
