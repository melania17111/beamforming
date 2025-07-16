import librosa
import numpy as np

def load_audio(i):
    path = 'audio/'
    names = ['vivian.mp3', 'andrea.mp3', 'edo.wav', 'ila.mp3']
    signal, sr = librosa.load(path + names[i])
    print(sr)
    if(len(signal) > 100000):
        signal = signal[:100000]
    else:
        pad_width = 100000 - len(signal)
        signal = np.pad(signal, (0, pad_width), mode='constant')
    return signal