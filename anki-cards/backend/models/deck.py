import random
import genanki
import pandas as pd
from typing import List
import os
import sys
from pathlib import Path
from typing import Optional
from utils.utils import generate_int_id
from utils.note_models import note_model_with_image, note_model_without_image


class Deck:

    def __init__(
        self,
        name: str,
        data: pd.DataFrame,
        front: str,
        back: str,
        image: Optional[str] = None,
    ) -> int:
        self.name = name
        self.data = data
        self.front = front
        self.back = back
        self._id = generate_int_id()
        self.deck = genanki.Deck(self.id, self.name)
        self.output_deck_name = ""

        if image:
            self.image = image
            self.model = note_model_with_image
            self._create_notes_with_image()
        else:
            self.model = note_model_without_image
            self._create_notes_without_image()

    def _generate_image_tag(self, row) -> str:

        if pd.notna(row[self.image]):
            return f"<img src='{row[self.image]}'>"
        else:
            return ""

    def _create_notes_with_image(self) -> None:

        for _, row in self.data.iterrows():
            front = row[self.front]
            back = row[self.back]
            image = self._generate_image_tag(row)

            note = genanki.Note(model=self.model, fields=[front, back, image])

            self.deck.add_note(note)

    def _create_notes_without_image(self) -> None:

        for _, row in self.data.iterrows():
            front = row[self.front]
            back = row[self.back]

            note = genanki.Note(model=self.model, fields=[front, back])

            self.deck.add_note(note)

    @property
    def notes(self) -> List[genanki.Note]:
        return self.deck.notes

    @property
    def id(self) -> int:
        return self._id

    def save(
        self,
        output_path: Optional[str] = None,
        output_deck_name: Optional[str] = None,
        format: str = "apkg",
    ) -> None:

        if output_deck_name:
            self.output_deck_name = output_deck_name
        else:
            self.output_deck_name = f"{self.name}_{self.front}_{self.back}_{self.id}"

        if not output_path:
            cwd = os.path.abspath(os.path.dirname(sys.argv[1]))
            output_path = os.path.join(cwd, "decks")

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        output_deck_file_name = f"{self.output_deck_name}.{format}"

        self.output_file = os.path.join(output_path, output_deck_file_name)

        if format == "csv":

            self.data.to_csv(self.output_file, index=False, header=False)
        else:
            genanki.Package(self.deck).write_to_file(self.output_file)

        print(f"Deck {self.name} is saved to {output_path}")

        return Path(self.output_file)
