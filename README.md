Anki Builder
============

Generate fully voiced Anki decks starting from a simple CSV file. The tool
wraps Hugging Face's `facebook/mms-tts-fra` model to synthesise French audio,
hashes and caches the clips per deck, and packages everything into a ready to
import `.apkg`.

Features
--------
- CSV → Anki pipeline with a single command.
- Automatic TTS synthesis (French) with silence trimming, fade-out and safe
  normalisation.
- Per-deck audio cache (`audio_files/<deck-name>/`) to avoid regenerating clips
  that already exist.
- Media packaging handled by `genanki`, including `[sound:...]` injection on
  every note.
- Simple project structure that is easy to extend (multiple models, more fields,
  etc.).

Requirements
------------
- Python 3.12 or newer.
- `pip` or another installer to fetch project dependencies.
- System packages usually required by SciPy (on Debian/Ubuntu:
  `sudo apt install build-essential libffi-dev libopenblas-dev liblapack-dev`).

Python dependencies:

```bash
pip install genanki torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install transformers scipy numpy
```

> The first call to the builder downloads the Hugging Face model. If you run
> offline, download it beforehand and point `TRANSFORMERS_CACHE` to the
> location that contains `facebook/mms-tts-fra`.

Project Layout
--------------

```
├── config/                 # Runtime paths (output decks, audio cache)
├── src/
│   ├── build_deck.py       # Main pipeline (CSV -> Anki deck)
│   ├── get_audio.py        # Audio synthesis & post-processing
│   ├── Audio_File.py       # Audio metadata + hashing helpers
│   └── services/tts_factory.py  # Lazily loaded TTS singleton
├── source_decks/           # Place input CSV files here
├── audio_files/<deck>/     # Generated audio cache (per deck)
├── build_decks/            # Exported `.apkg` decks
└── main.py                 # CLI entry point
```

Preparing the Environment
-------------------------
1. Clone the repository.
2. (Optional) Create and activate a virtual environment.
3. Install the Python dependencies listed above.
4. Run `python3 main.py --help` to confirm the CLI works and creates the default
   folders defined in `config/config.py`.

CSV Format
----------
The builder expects a semicolon-separated file with three columns:

```
Polish;French;ExampleSentence
wstawać;se lever;Je me lève à sept heures tous les jours.
brać prysznic;se doucher;Il se douche rapidement avant le travail.
```

Headers are optional. When present, the first row **must** match the example
above so it can be skipped automatically.

Usage
-----

```bash
python3 main.py source_decks/la_vie_quotidienne.csv
```

The command will:
1. Prepare `audio_files/la_vie_quotidienne/` with one `.wav` per row.
2. Cache already generated clips so re-running the build is instantaneous.
3. Create `build_decks/la_vie_quotidienne.apkg`, ready to import into Anki.

Importing the Deck
------------------
- Copy the generated `.apkg` to your Anki host (for WSL users you can access the
  repository via `\\wsl$` from Windows Explorer).
- Import the deck in Anki (`File → Import`). Media files are bundled inside, so
  audio will work immediately without manual copying.
- If you replace an existing deck, let Anki update the notes so that fresh audio
  files are unpacked.

Development & Testing
---------------------
- Existing tests live under `tests/`. Expand them as you add new modules.
- `src/services/tts_factory.get_model()` uses a cached singleton; if you tweak
  model settings, remember to clear the cache between runs (e.g. restart the
  interpreter).
- When changing audio post-processing, verify one generated clip with a media
  player to ensure the format remains PCM16.

License
-------
The project is distributed under the MIT License (see `LICENSE`).
