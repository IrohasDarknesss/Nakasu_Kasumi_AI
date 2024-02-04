from moviepy.editor import *
import os

mov_dir = './kasumin_voice/'
wav_dir = './train/'

if not os.path.exists(wav_dir):
    os.makedirs(wav_dir)
for i, fn in os.listdir(mov_dir):
    if fn.endswith(".MOV"):
        before_path = os.path.join(mov_dir, fn)
        output = os.path.splitext(fn)[0] + '.wav'
        op = os.path.join(wav_dir, output)
        load_mov = VideoFileClip(before_path)
        load_mov.audio.write_audiofile(op)
        print(f"{i}: Converted {fn} to wav file.")