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
import math
 
# Spectrogram Conversion of train videos
spec_list = list(train_df['Participant_ID'])
traini_df = pd.DataFrame(columns = train_df.columns)
for path, directories, files in os.walk('D:\RC_Data'):
    for audio in files:
        if audio in spec_list:
            gen = train_df.loc[train_df['Participant_ID'] == audio, 'Gender'].iloc[0] 
            phq = train_df.loc[train_df['Participant_ID'] == audio, 'PHQ8_Binary'].iloc[0]
            sample_rate, samples = wavfile.read(os.path.join(path,audio))
            for i in range(1,math.floor(len(samples)/(30*sample_rate))):
                frequencies, times, spectrogram = signal.spectrogram(samples[30*(i - 1)*sample_rate:30*i*sample_rate], sample_rate)
                plt.pcolormesh(times, frequencies, np.log(spectrogram))
                plt.savefig(os.path.join(path,"{}_{}.png".format(audio,i)), bbox_inches='tight')
                traini_df.loc[len(traini_df.index)] = ["{}_{}.png".format(audio,i), gen, phq]

# Spectrogram Conversion of dev videos
spec_list = list(dev_df['Participant_ID'])
devi_df = pd.DataFrame(columns = dev_df.columns)
for path, directories, files in os.walk('D:\RC_Data'):
    for audio in files:
        if audio in spec_list:
            gen = dev_df.loc[dev_df['Participant_ID'] == audio, 'Gender'].iloc[0] 
            phq = dev_df.loc[dev_df['Participant_ID'] == audio, 'PHQ8_Binary'].iloc[0]
            sample_rate, samples = wavfile.read(os.path.join(path,audio))
            for i in range(1,math.floor(len(samples)/(30*sample_rate))):
                frequencies, times, spectrogram = signal.spectrogram(samples[30*(i - 1)*sample_rate:30*i*sample_rate], sample_rate)
                plt.pcolormesh(times, frequencies, np.log(spectrogram))
                plt.savefig(os.path.join(path,"{}_{}.png".format(audio,i)), bbox_inches='tight')
                devi_df.loc[len(devi_df.index)] = ["{}_{}.png".format(audio,i), gen, phq]                

# Spectrogram Conversion of test videos
spec_list = list(test_df['Participant_ID'])
testi_df = pd.DataFrame(columns = test_df.columns)
for path, directories, files in os.walk('D:\RC_Data'):
    for audio in files:
        if audio in spec_list:
            gen = test_df.loc[test_df['Participant_ID'] == audio, 'Gender'].iloc[0] 
            phq = test_df.loc[test_df['Participant_ID'] == audio, 'PHQ8_Binary'].iloc[0]
            sample_rate, samples = wavfile.read(os.path.join(path,audio))
            for i in range(1,math.floor(len(samples)/(30*sample_rate))):
                frequencies, times, spectrogram = signal.spectrogram(samples[30*(i - 1)*sample_rate:30*i*sample_rate], sample_rate)
                plt.pcolormesh(times, frequencies, np.log(spectrogram))
                plt.savefig(os.path.join(path,"{}_{}.png".format(audio,i)), bbox_inches='tight')
                testi_df.loc[len(testi_df.index)] = ["{}_{}.png".format(audio,i), gen, phq]
