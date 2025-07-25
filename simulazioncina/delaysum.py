import numpy as np
import sounddevice as sd
import librosa
""" delay-and-sum
prima simulazione:
main lobe a 60 gradi
1 segnale vocale nel main lobe
3 segnali rumore da altre direzioni
in imput dalla GUI: 4 angoli di direzione
array progettato per amplificare dalla direzione 60 gradi """
from input import get_freq
from audios import load_audio

def delaysumbeamforming(dirs, theta, d, N):
    # N num microfoni
    # d  distanza tra mic
    # alfa direzione main lobe
    n_sig = 4 # 1 voce, 3 rumori
    n_sample = 100000
    sig = np.zeros([n_sig, n_sample])
    for i in range(n_sig):
        voice = load_audio(i)
        sig[i, :] = voice.tolist()
    c = 340 # vel suono (m/s)

    fs = 22050 # freq di campionamento
    pos_mic = np.array([[0, n*d] for n in range(N)])
    delays = np.array([(n*d*np.sin(theta))/c for n in range(N)])
    delays = delays * fs # ritardi in campioni

    t = np.arange(n_sample) / fs
    #voice = np.sin(2*np.pi*440 * t)
    #noise = np.random.normal(0, 0.1, n_sample) # rumore bianco
    #noise = np.sin(2*np.pi*100 * t)
    #sig = np.array([voice, noise, noise, noise])

    recorded_sig = np.zeros(n_sample)
    beamformed_sig = np.zeros(n_sample)

    # segnale registrato e segnale beamformed
    for i in range(n_sig):
        signal = sig[i]
        dir = np.deg2rad(dirs[i])
        for n in range(N):
            tau = (n*d*np.sin(dir))/c
            tau = tau * fs
            recorded_sig += shiftsig(signal, tau)
            beamformed_sig += shiftsig(signal, tau - delays[n])

    beamformed_sig /= N
    return recorded_sig, beamformed_sig

def play_rec(recorded_sig, fs):
    sd.play(recorded_sig, fs)
    sd.wait

def play_bf(beamformed_sig, fs):
    sd.play(beamformed_sig, fs)
    sd.wait

def shiftsig(sig, tau):
    shifted = np.zeros_like(sig)
    tau = int(tau)
    if tau >= 0:
        if tau < len(sig):
            shifted[tau:] = sig[:len(sig)-tau]
    else:
        tau = abs(tau)
        if tau < len(sig):
            lunghezza = len(sig) - tau
            shifted[:lunghezza] = sig[tau:]
    return shifted