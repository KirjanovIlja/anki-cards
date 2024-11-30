from flask import Flask, request, jsonify
from models.dataset_generator import DatasetGenerator
from models.deck import Deck
from models.words_generator import WordsGenerator
from models.words_translator import WordsTranslator
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)
CORS(
    app,
    resources={
        r"/generate": {
            "origins": "http://127.0.0.1:5500",
            "methods": ["GET", "POST", "OPTIONS"],
        }
    },
)
Talisman(app)

wg = WordsGenerator()
wt = WordsTranslator()
dg = DatasetGenerator()


@app.route("/generate", methods=["POST", "OPTIONS"])
def generate_deck():

    # Allow preflight requests
    if request.method == "OPTIONS":
        return "", 200

    data = request.json

    topic = data.get("topic")
    num_words = data.get("numWords", 100)
    source_lang = data.get("sourceLang", "en")
    target_lang = data.get("targetLang", "es")

    try:
        generated_words = wg.generate_words(topic=topic, n_words=num_words)
        translated_words = wt.translate_words(
            words=generated_words, source_lang=source_lang, target_lang=target_lang
        )
        generated_dataset = dg.generate_dataset(
            words=translated_words, source_lang=source_lang, target_lang=target_lang
        )

        deck = Deck(
            f"{topic}_deck", data=generated_dataset, front=source_lang, back=target_lang
        )
        output_path = f"./decks/{deck.id}/"

        apkg_saved_path = deck.save(output_path=output_path, format="apkg")
        csv_saved_path = deck.save(output_path=output_path, format="csv")

        return (
            jsonify(
                {
                    "status": "success",
                    "deckPath": str(output_path),
                    "csv_deck": str(csv_saved_path),
                    "apkg_deck": str(apkg_saved_path),
                }
            ),
            200,
        )

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
