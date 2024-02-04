import os

jsut_v1 = [
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

output = ['filelists/']

os.makedirs(output, exist_ok=True)

with open(output+'transctipt_utf8.txt', 'w') as wf:
    for in_path in jsut_v1:
        with open(in_path+'transctipt_utf8.txt', 'r') as rf:
            wf.write(rf.read())