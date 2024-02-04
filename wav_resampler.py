import os
import librosa
import soundfile as sf 

#path 
jsut_wavs = [
    'jsut_ver1.1/basic5000/',
    'jsut_ver1.1/countersuffix26/',
    'jsut_ver1.1/loanword128/',
    'jsut_ver1.1/onomatopee300/',
    'jsut_ver1.1/precedent130/',
    'jsut_ver1.1/repeat500/',
    'jsut_ver1.1/travel1000/',
    'jsut_ver1.1/utparaphrase512/',
    'jsut_ver1.1/voiceactress100/'
]

output = 'wav/'

os.makedirs(output, exist_ok=True)

# 48KHz → 22KHz
def convert(path):
    fns = os.listdir(path+'wav/')
    for fn in fns:
        print(path+'wav/'+fn)
        y, sr = librosa.core.load(path+'wav'+fn, sr=22050, mono=True)
        sf.write(output+'kasukasu/'+fn, y, sr, subtype="PCM_16")
for jsut_wav in jsut_wavs:
    convert(jsut_wav)