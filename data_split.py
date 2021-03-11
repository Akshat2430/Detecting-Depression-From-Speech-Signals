# Importing relevant libraries
import subprocess
import os
from os import walk
import csv
import shutil

# Splitting audio files in train, dev and test
for path, directories, files in os.walk('D:\RC_Data'):
    for audio in files:
        if audio == "train_split_Depression_AVEC2017.csv":
            train_df = pd.read_csv(os.path.join(path,audio))
            train_df = train_df[['Participant_ID','Gender','PHQ8_Binary']]
            train_df['Participant_ID'] = train_df['Participant_ID'].map(lambda x: str(x) + '_AUDIO_final.wav')
        if audio == "dev_split_Depression_AVEC2017.csv":
            dev_df = pd.read_csv(os.path.join(path,audio))
            dev_df = dev_df[['Participant_ID','Gender','PHQ8_Binary']]
            dev_df['Participant_ID'] = dev_df['Participant_ID'].map(lambda x: str(x) + '_AUDIO_final.wav')
        if audio == "test_split_Depression_AVEC2017.csv":
            test_df = pd.read_csv(os.path.join(path,audio))
            test_df['participant_ID'] = test_df['participant_ID'].map(lambda x: str(x) + '_AUDIO_final.wav')
train_path = "D:\\RC_Data\\train\\"
dev_path = "D:\\RC_Data\\dev\\"
test_path = "D:\\RC_Data\\test\\"
train_list = list(train_df['Participant_ID'])
dev_list = list(dev_df['Participant_ID'])
test_list = list(test_df['participant_ID'])
for path, directories, files in os.walk('D:\RC_Data'):
    for audio in files:
        if audio.endswith("_final.wav"):
            if audio in train_list:
                shutil.move(os.path.join(path,audio), train_path) 
            if audio in dev_list:
                shutil.move(os.path.join(path,audio), dev_path)
            if audio in test_list:
                shutil.move(os.path.join(path,audio), test_path)     
