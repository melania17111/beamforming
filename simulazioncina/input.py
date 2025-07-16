import tkinter as tk
import numpy as np

# direzione main lobe (alfa)
def get_teta(root):
    frame = tk.Frame(root)
    tk.Label(frame, text="Direzione (°):").pack()
    slider = tk.Scale(frame, from_=0, to=360, orient="horizontal")
    slider.set(30)  # valore iniziale
    slider.pack()
    frame.pack(side="left", padx = 5)
    return slider

# frequenza di lavoro
def get_freq(root):
    frame = tk.Frame(root)
    tk.Label(frame, text="Frequenza (Hz):").pack()
    entry_freq = tk.Scale(frame, from_=0, to=1000, orient="horizontal")
    entry_freq.set(400)  # valore iniziale
    entry_freq.pack()
    frame.pack(side="left", padx = 5)
    return entry_freq

# distanza tra mic
def get_d(root):
    frame = tk.Frame(root)
    tk.Label(frame, text="distanza tra mic (m):").pack()
    entry_d = tk.Scale(frame, from_=0, to=1, resolution=0.01, orient="horizontal")
    entry_d.set(0.3)  # valore iniziale
    entry_d.pack()
    frame.pack(side="left", padx = 5)
    return entry_d

# n mic
def get_N(root):
    frame = tk.Frame(root)
    tk.Label(frame, text="numero di mic:").pack()
    entry_N = tk.Scale(frame, from_=0, to=10, orient="horizontal")
    entry_N.set(5)  # valore iniziale
    entry_N.pack()
    frame.pack(side="left", padx = 5)
    return entry_N