import genanki
import os
import random


from src.get_data import get_data_from_csv
from config.config import BUILD_OUTPUT_PATH

def build_deck(file_path: str):

    if not file_path:
        raise Exception("File path was not provided !")
    if not os.path.exists(file_path):
        raise Exception("Provided file path does not exist!")
    if not os.path.isfile(file_path):
        raise Exception("Provided file path is not a file!")
    if not file_path.endswith(".csv"):
        raise Exception("Provided file is not a csv file!")
    
    file_name = os.path.basename(file_path)
    

    deck = genanki.Deck(
        #TODO ZMIANA NUMERU
        random.randint(1,1000000000),
        file_name
    )

    # Model for the cards
    model = genanki.Model(
        1607392319,
        "Simple Model PL->FR",
        fields=[{"name":"Front"},{"name":"Back"},{"name":"Example"}],
        templates=[{
            "name":"PL->FR",
            "qfmt":"<b>{{Front}}</b>",                 # PL na przodzie
            "afmt":"{{FrontSide}}<hr id='answer'>{{Back}}<br><i>{{Example}}</i>"  # FR + przykład
        }],
    )

    # Vocabulary list with examples
    vocab = get_data_from_csv(file_path)

    # Add notes to deck
    for fr, pl, ex in vocab:
        note = genanki.Note(
            model=model,
            fields=[pl, fr, ex]
        )
        deck.add_note(note)

    # Create package
    package = genanki.Package(deck)
    output_path = os.path.join(BUILD_OUTPUT_PATH, file_name.replace('csv','apkg'))
    package.write_to_file(output_path)
