from genanki import Model, Deck, Note
import random
import pandas as pd

class AnkiDeck:

    def __init__(self, 
                 name: str, 
                 model: Model, 
                 data: pd.DataFrame,
                 front: str,
                 back: str,
                 image: str = "Image"
                ) -> None:
        self.name = name
        self.model = model
        self.data = data
        self.front = front
        self.back = back
        self.image = image
        self.deck_id = self.generate_id()
        self.deck = Deck(self.deck_id, self.name)
        self.create_notes()

    def generate_id(self) -> str:

        id = random.randint(1_000_000_000, 2_147_483_647)
        
        return f"{name}_{front}_{back}_{id}"
    
    def generate_image_tag(self) -> str:
        
        if pd.notna(row[self.image]):
            return f"<img src='{row[self.image]}'>"
        else:
            return ""

    def create_notes(self) -> None: 

        for _, row in self.data.iterrows():
            front = row[self.front]
            back = row[self.back]
            image = self.generate_image_tag()
            
            note = Note(
                model = self.model,
                fields=[front, back, image]
            )
            
            self.deck.add_note(note)
            
        
        