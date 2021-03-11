# Importing relevant libraries
import subprocess
import os
from os import walk
import csv
from pydub import AudioSegment
import pandas as pd

# Speech recombination
for path, directories, files in os.walk('D:\RC_Data'):
    k = 0
    for audio in files:
        if audio.endswith("_cleaned.wav"):
            participant = audio.replace("_cleaned.wav", "_final.wav")
        if audio.endswith("_SPLIT.wav"):
            audio = AudioSegment.from_wav(os.path.join(path,audio))
            if k == 0:
                combined = audio
                k = 1
            else:
                combined = combined + audio
    combined.export(os.path.join(path,participant), format="wav")
