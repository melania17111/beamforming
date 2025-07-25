import tkinter as tk
import numpy as np
from delaysum import delaysumbeamforming
from delaysum import play_rec
from delaysum import play_bf
from input import get_theta
from input import get_freq
from input import get_d
from input import get_N
from radiationpattern import radiation_pattern
from radiationpattern import draw_pattern
import librosa

N = 5
d = 0.386
height = 560
width = 560
centerX = width / 2
centerY = height / 2
global recorded_sig
global beamformed_sig
fs = 22050
shapes = []
dirs = np.zeros(4)
i = 0

def on_click(event):
    global i
    global shapes
    x, y = float(event.x), float(event.y)
    dirs[i] = np.rad2deg(np.arctan2(centerY-y, x-centerX))
    shapes.append(canvas.create_oval(x-6, y-6, x+6, y+6, fill="red"))
    i += 1

def perform_beamforming():
    global recorded_sig, beamformed_sig
    recorded_sig, beamformed_sig = delaysumbeamforming(dirs, theta, d, N)
    print("Beamforming completato!")
    print(dirs)

def adjust(_=None):
    global theta, freq, d, N
    try:
        freq = float(slider_f.get())
        d = float(slider_d.get())
        N = int(slider_N.get())
        theta = np.deg2rad(slider_dir.get())
        canvas.delete("all")
        display(canvas)
        pattern = radiation_pattern(N, d, freq, theta)
        draw_pattern(canvas, pattern)
        print(f"Aggiornato: teta={theta}, freq={freq}, d={d}, N={N}")
    except ValueError:
        print("Inserisci solo numeri validi.")

def reset():
    global i, dirs
    i = 0
    dirs = np.zeros(4)
    for shape in shapes:
        canvas.delete(shape)
    shapes.clear()
    canvas.bind("<Button-1>", on_click)

def display(canvas):
    arr_length = (N-1)*d*40
    canvas.create_oval(centerX-250, centerY-250, centerX+250, centerY+250, fill="#FFE386")
    for i in range(N):
        x = centerX
        y = centerY - (arr_length//2) + i*d*40
        canvas.create_oval(x-6, y-6, x+6, y+6, fill="#09124D")
    canvas.create_line(centerX, centerY, centerX + 250*np.cos(theta), centerY - 250*np.sin(theta), dash=(5,3), fill="red")

root = tk.Tk()
root.title("Beamforming Array Visualizer")
frame_slider = tk.Frame(root, bg="white")
frame_slider.pack(pady=10)
canvas = tk.Canvas(root, width=width, height=height, bg="#09124D")
canvas.pack(pady=10)
slider_dir = get_theta(frame_slider)
slider_dir.config(command=adjust)
theta = np.deg2rad(slider_dir.get())
slider_f = get_freq(frame_slider)
slider_f.config(command=adjust)
freq = float(slider_f.get())
slider_d = get_d(frame_slider)
slider_d.config(command=adjust)
d = float(slider_d.get())
slider_N = get_N(frame_slider)
slider_N.config(command=adjust)
N = int(slider_N.get())

display(canvas)

canvas.bind("<Button-1>", on_click)
pattern = radiation_pattern(N, d, freq, theta)
print(len(pattern))
draw_pattern(canvas, pattern)

btn_go = tk.Button(root, text="esegui il beamforming", command=perform_beamforming)
btn_go.pack(pady=1)
btn_rec = tk.Button(root, text="audio originale", command = lambda: play_rec(recorded_sig, fs))
btn_rec.pack(pady=1)
btn_bf = tk.Button(root, text="audio beamformed", command = lambda: play_bf(beamformed_sig, fs))
btn_bf.pack(pady=1)
btn_bf = tk.Button(root, text="reset", command = reset)
btn_bf.pack(pady=1)

root.mainloop()