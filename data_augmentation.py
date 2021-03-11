# Importing relevant libraries
import subprocess
import os
from os import walk
import csv
import shutil
import numpy as np
import cv2
from scipy.io import wavfile
import librosa
import scipy

# Getting an idea of the data imbalance
print("The old number of non-depressed people is",train_df['PHQ8_Binary'].value_counts()[0])
print("The old number of depressed people is",train_df['PHQ8_Binary'].value_counts()[1])

# Speed tuning for audio augmentation
af = train_df[train_df['PHQ8_Binary'] == 1]
af_list = list(af['Participant_ID'])
i = 493
newauds = []
for path, directories, files in os.walk('D:\RC_Data'):
    for audio in files:
        if audio in af_list:
            i = i + 1
            speed_rate = np.random.uniform(0.7,1.3) 
            aud, fs = librosa.load(os.path.join(path,audio))
            aud_tuned = librosa.effects.time_stretch(aud, speed_rate)
            scipy.io.wavfile.write(os.path.join(path, "{}_AUDIO_final.wav".format(i)), fs, aud_tuned)
            newauds.append("{}_AUDIO_final.wav".format(i))

# Making changes in the dataframes
bf = pd.DataFrame(newauds, columns = ['Participant_ID'])
bf.reset_index(drop=True, inplace=True)
af.reset_index(drop=True, inplace=True)
newf = pd.concat([bf,af[['Gender','PHQ8_Binary']]], ignore_index=True, axis = 1)
newf = newf.dropna()
newf = newf.rename(columns = {0:'Participant_ID', 1:'Gender', 2:'PHQ8_Binary'})
train_df = train_df.append(newf)

# Getting an idea of the data imbalance
print("The new number of non-depressed people is",train_df['PHQ8_Binary'].value_counts()[0])
print("The new number of depressed people is",train_df['PHQ8_Binary'].value_counts()[1])
