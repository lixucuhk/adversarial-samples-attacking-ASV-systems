import librosa
import librosa.filters
import numpy as np
from scipy import signal
from scipy.io import wavfile
import soundfile as sf
import kaldi_io

# def load_wav_snf_scaled(path):
#     wav, sr = sf.read(path, dtype=np.float32)
#     scale = np.max(np.abs(wav))
#     return wav, scale

# def save_wav_snf_scaled(wav, path, scale, sr=16000):
#     wav *= scale / max(0.01, np.max(np.abs(wav)))
#     sf.write(path, wav, sr)
in_path = 'non-target-trials/50_id10270-5r0dWxy17C8-00003_id10273-58VB-LYIoRM-00002.wav'
out_path = 'non-target-trials/50r02_id10270-5r0dWxy17C8-00003_id10273-58VB-LYIoRM-00002.wav'
scale = 0.2

wav, sr = sf.read(in_path, dtype=np.float32)
wav *= scale
sf.write(out_path, wav, sr)
