from transformers import VitsModel, AutoTokenizer
import torch
import scipy
import numpy as np
import os

from config.config import BUILD_AUDIO_FILES_PATH
from src.Audio_File import get_Audio_Files_list






def create_audio(content_list: list[str]) -> None:
    model = VitsModel.from_pretrained("facebook/mms-tts-fra")
    tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-fra")

    Audio_Files = get_Audio_Files_list(content_list)

    sr = int(model.config.sampling_rate)

    for audio_file in Audio_Files:
        
        if audio_file.is_created:
            continue

        # 1) bez batcha i bez paddingu
        inputs = tokenizer(audio_file.content, return_tensors="pt")
        with torch.no_grad():
            out = model(**inputs).waveform

        # 2) mono 1D
        audio = np.asarray(out.squeeze().cpu().numpy(), dtype=np.float32).reshape(-1)

        # 3) agresywne przycięcie taila ramkami 20 ms do pierwszego "nie-cichego" fragmentu
        win = int(0.02 * sr)            # 20 ms
        th = 10 ** (-55 / 20)           # ≈ -55 dBFS
        end = len(audio)
        while end - win > 0 and np.sqrt(np.mean(audio[end - win:end]**2)) < th:
            end -= win
        audio = audio[:max(end, 0)]

        # 4) dłuższy fade-out 50 ms, żeby zabić klik/metaliczny ogon
        fade = int(0.05 * sr)
        if fade > 0 and len(audio) > fade:
            audio[-fade:] *= np.linspace(1.0, 0.0, fade, dtype=audio.dtype)

        # 5) bezpieczna normalizacja z marginesem
        peak = float(np.max(np.abs(audio))) if audio.size else 0.0
        if peak > 0:
            audio *= (0.90 / peak)

        # 6) ZAPIS: na test zapisz float32 (eliminuje artefakty kwantyzacji)
        out_path = os.path.join(BUILD_AUDIO_FILES_PATH, f"{audio_file.file_path}.wav")
        scipy.io.wavfile.write(out_path, rate=sr, data=audio.astype(np.float32))

        # Jeśli MUSISZ mieć int16, odkomentuj te 3 linie (po teście):
        # audio_i16 = np.int16(np.clip(audio, -1.0, 1.0) * 32767)
        # scipy.io.wavfile.write(out_path, rate=sr, data=audio_i16)
