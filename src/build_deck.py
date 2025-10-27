import genanki
import os
import random


from src.get_data import get_data_from_csv
from config.config import BUILD_OUTPUT_PATH
from src.get_audio import create_audio
from src.Audio_File import get_Audio_Files_list, get_Audio_Files_paths

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
        fields=[{"name":"Front"},{"name":"Back"},{"name":"Example"},{"name":"MyMedia"}],
        templates=[{
            "name":"PL->FR",
            "qfmt":"<b>{{Front}}</b>",                 # PL na przodzie
            "afmt":"{{FrontSide}}<hr id='answer'>{{Back}}<br><i>{{Example}}</i><br>{{MyMedia}}"  # FR + przykład + dźwięk
        }],
    )

    # Vocabulary list with examples
    vocab = get_data_from_csv(file_path)

    vocab = vocab[1:]

    example_list = [row[2] for row in vocab]

    audio_list = get_Audio_Files_list(example_list)

    create_audio(audio_list)


    # Add notes to deck
    index = 0
    for fr, pl, ex in vocab:
        audio_filename = os.path.basename(audio_list[index].file_path)
        audio_field_value = f"[sound:{audio_filename}]"
        note = genanki.Note(
            model=model,
            fields=[pl, fr, ex, audio_field_value]
        )
        deck.add_note(note)
        index += 1
    # Create package
    package = genanki.Package(deck)
    package.media_files = get_Audio_Files_paths(audio_list)
    output_path = os.path.join(BUILD_OUTPUT_PATH, file_name.replace('csv','apkg'))
    package.write_to_file(output_path)
