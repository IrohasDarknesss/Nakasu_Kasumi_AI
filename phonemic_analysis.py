import matplotlib.pyplot as plt 
from scipy.io import wavfile
import numpy as np
import glob
import pygame
import time

pygame.init()
pygame.mixer.init()

file_lists = glob.glob('./train/*wav')

for i, file in enumerate(file_lists):
    rate, data = wavfile.read(file)
    
    if len(data.shape) > 1:
        data = data[:,0]
    times = np.arange(len(data)) / float(rate)

    plt.figure(figsize=(15,5))
    plt.fill_between(times, data, color='skyblue')
    plt.xlim(times[0], times[-1])
    plt.xlabel('Times(s)')
    plt.ylabel('Amplitude')
    plt.title(f'Phenemic Analysis: {file}')
    plt.draw()
    plt.pause(0.1)

    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    time.sleep(5)
    plt.close('all')

    if i >= 3:
        break

pygame.quit()