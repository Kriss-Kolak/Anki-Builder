BUILD_OUTPUT_PATH = "build_decks"
BUILD_INPUT_PATH = "source_decks"
BUILD_AUDIO_FILES_PATH = "audio_files"

NECESSARY_FOLDERS = [BUILD_OUTPUT_PATH, BUILD_INPUT_PATH, BUILD_AUDIO_FILES_PATH]

import os

def initialize_folders() -> None:
    """Create necessary folders if they do not exist."""
    current_path = os.getcwd()
    for folder in NECESSARY_FOLDERS:
        whole_path = os.path.join(current_path, folder)
        print(whole_path)
        if not os.path.exists(whole_path):
            os.mkdir(whole_path)

def create_environment() -> None:
    """Set up the environment by initializing necessary folders."""
    initialize_folders()