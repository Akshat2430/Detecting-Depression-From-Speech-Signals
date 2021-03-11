# Importing relevant libraries
import subprocess
import os
from os import walk
import csv
from pydub import AudioSegment
import pandas as pd

# Using speech transcripts for speech diarisation
for path, directories, files in os.walk('D:\RC_Data'):
    k = 0
    for audio in files:
        if audio.endswith("_TRANSCRIPT.csv"):
            df = pd.read_csv(os.path.join(path,audio), sep= '\t')
            df = df[df.speaker == 'Participant']
            k = k + 1
        if audio.endswith("_cleaned.wav"):  
            tempaudio = AudioSegment.from_wav(os.path.join(path,audio))
            k = k + 1
        if k == 2:
            for index, row in df.iterrows():
                t1 = row['start_time'] * 1000 
                t2 = row['stop_time'] * 1000
                newaudio = tempaudio[t1:t2]
                newaudio.export(os.path.join(path, '{}_{}_SPLIT.wav'.format(t1,t2)), format="wav")
