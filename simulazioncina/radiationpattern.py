'''array factor:
      sin(Nkd/2 sin a)
AF =  ----------------
      Nsin(kd/2 sin a)
      
      I max può essere 280
      k = '''
import numpy as np

def radiation_pattern(N, d, freq, teta):
    a = np.arange(0, 360, 0.1)
    c = 340
    pattern = []
    k = 2*np.pi / (c/freq)
    for alfa in a:
        alfa_rad = np.deg2rad(alfa)
        x = ((k * d) / 2) * (np.sin(alfa_rad) - np.sin(teta))
        if x == 0:
            af = 1
        else:
            af = np.sin(N*x) / (N*np.sin(x))
        pattern.append(af)
    return pattern

def draw_pattern(canvas, pattern):
    scale = 250
    x = []
    y = []
    alfa = np.deg2rad(np.arange(0, 360, 0.1))
    for alfa, af in zip(alfa, pattern):
        r = abs(af) * scale
        x1 = 280 + r*np.cos(alfa)
        y1 = 280 - r*np.sin(alfa)
        x.append(x1)
        y.append(y1)
    canvas.delete("pattern")
    for i in range(len(x)-1):
        canvas.create_line(x[i], y[i], x[i+1], y[i+1], fill="red", width = 2)