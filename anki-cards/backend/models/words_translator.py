from deep_translator import GoogleTranslator
import aiohttp
import asyncio


class WordsTranslator:

    def translate_words(
        self, words: list[str], source_lang: str = "en", target_lang: str = "de"
    ) -> dict:

        translator = GoogleTranslator(source=source_lang, target=target_lang)
        translated_words = {}

        for word in words:
            try:
                translated_words[word] = translator.translate(word)
            except Exception as e:
                print(f"Failed to translate word {word} - {e}")

        return translated_words
