from transformers import VitsModel, AutoTokenizer  
from functools import lru_cache

MODEL_NAME = "facebook/mms-tts-fra"


@lru_cache(maxsize=1)
def get_model() -> VitsModel:
    return VitsModel.from_pretrained(MODEL_NAME)

@lru_cache(maxsize=1)
def get_tokenizer() -> AutoTokenizer:
    return AutoTokenizer.from_pretrained(MODEL_NAME)

