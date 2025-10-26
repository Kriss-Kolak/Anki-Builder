from transformers import VitsModel, AutoTokenizer
import torch
import scipy
import numpy as np


model = VitsModel.from_pretrained("facebook/mms-tts-fra")
tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-fra")

texts = [
    "Je me lève à sept heures tous les jours.",
    "Je bois du café.",
    "Je vais au travail en voiture."
]

inputs = tokenizer(texts, return_tensors="pt", padding=True)

with torch.no_grad():
    outputs = model(**inputs).waveform  # shape: [3, N]

for i, audio_tensor in enumerate(outputs):
    audio = audio_tensor.cpu().numpy()
    audio_int16 = np.int16(audio / np.max(np.abs(audio)) * 32767)
    scipy.io.wavfile.write(f"fra_{i}.wav", rate=model.config.sampling_rate, data=audio_int16)