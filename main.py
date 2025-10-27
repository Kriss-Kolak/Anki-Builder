from src.build_deck import build_deck
from config.config import create_environment
import argparse


def main():

    create_environment()

    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="input file path", type=str)

    args = parser.parse_args()

    file_path = args.input_file
    
    if file_path:
        build_deck(file_path)

if __name__ == "__main__":
    main()
    
