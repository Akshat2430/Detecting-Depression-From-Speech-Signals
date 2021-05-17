# Detecting-Depression-From-Speech-Signals

## Motivation

Depression is a common illness worldwide, with more than 264 million people affected[1]. At its core, depression is a mental health disorder characterised by persistently depressed mood or loss of interest in activities. Although there are known, effective treatments for such mental disorders, between 76% and 85% of people in low- and middle-income countries receive no treatment for their disorder[2].  

This lack of treatment stems from a lack of resources and a lack of trained medical professionals (besides the obvious social stigma attached to these conditions). However, perhaps one of the most major barriers is inaccurate assessment. People who are depressed are often not correctly diagnosed.

Most laboratory tests are useless when it comes to diagnosing depression. In fact, talking with the patient remains the main tool of diagnosing depression. Doctors use a series of standard questions to screen for depression. However, a diagnosis is often difficult to make because clinical depression can manifest in so many different ways. Only in a few rare cases does depression present itself as an obvious outcome. Therefore, establishing objective parameters becomes of paramount importance during diagnosis.

One such objective parameter is speech. Speech is attractive since it can be  measured cheaply, remotely, non-invasively and non-intrusively. However, it is very communicative and contains much variability[3]. Depressed patients demonstrate prosodic speech issues, such as reduced variation in loudness, repetitious pitch inflections and stress patterns, and monotonous pitch and loudness [4]. This method of diagnosis could also simply be implemented in a mobile phone application or a wearable device as well, limiting the probability of inaccurate assessment and lowering social stigma.

## Literature Review

The 2018 Interspeech Conference witnessed the first instances of diagnosing depression through speech alone, given that previous machine learning methods had been multimodal in nature (considering text, video, audio etc.) . Afshan et al. [5] focused on the effectiveness of voice quality features in detecting depression. They used voice quality features (F0, F1, F2, F3, H1-H2, H2-H4, H4-H2k, A1, A2, A3 and CPP), inspired by a psychoacoustic model of voice quality, in addition to Mel-frequency cepstral coefficients (MFCCs). The results were optimistic with an accuracy of 77% with test utterances were as short as 10 s. The accuracy was as high as 95% when the test utterances were 1.8 minutes long. 

Hanai et al. [6] presented a depression detection model based on sequences of audio and text transcriptions. They evaluated a regularized logistic regression model (context-free and weighted), and a long short-term memory (LSTM) model (using the sequences of responses, and without context of the questions). Their findings showed that context-free modelling based on text features performed better than audio features when classifying for a binary outcome (depressed vs. non-depressed). However, audio features were more accurate in determining the multi-class depression score. As expected, the multi-modal model yielded the best performance. 

This project aims to propose a method for speech-based diagnosis of depression using convolutional neural networks.

## Data

The data will be drawn from the Distress Analysis Interview Corpus (DAIC) (7), that contains clinical interviews designed to support the diagnosis of psychological distress conditions such as anxiety, depression, and post-traumatic stress disorder. These interviews were collected as part of a larger effort to create a computer agent that interviews people and identifies verbal and nonverbal indicators of mental illness (8). 

Data collected include audio and video recordings and extensive questionnaire responses; this part of the corpus includes the Wizard-of-Oz interviews, conducted by an animated virtual interviewer called Ellie, controlled by a human interviewer in another room. Data has been transcribed and annotated for a variety of verbal and non-verbal features. This dataset includes 189 sessions of interactions ranging between 7-33min (with an average of 16min). Each session includes transcript of the interaction, participant audio files, and facial features.

## Objectives

1.Audio Pre-processing (Planning to use pyAudioAnalysis and Sox/RubberBand)
- [x] Noise Reduction - Removal of background hissing, humming and buzzing sounds
- [x] Speech Diarization - Splitting session recordings to remove the voice of the virtual interviewer, since that’s essentialy noise
- [x] Speech Recombination - Combining speech segments of same speaker
- [x] Data Augmentation - Since non-depressed samples is thrice the depressed samples and data is limited, generating artificial samples becomes important

2.Data Preparation (Planning to use scikit-learn)
- [x] Spectrogram Conversion - Convertiing audio samples to spectrogram images
- [x] Data Normalization - Normalizing image tensors
- [x] Data Splitting - A standard train-dev-test split

3.Model Training (Planning to use Keras)
- [x] Defining model architecture
- [x] Deciding ideal metric - F1 Score encapsulates precision and recall, making it an ideal choice
- [ ] Training

## References

1. GBD 2017 Disease and Injury Incidence and Prevalence Collaborators. (2018). Global, regional, and national incidence, prevalence, and years lived with disability for 354 diseases and injuries for 195 countries and territories, 1990–2017: a systematic analysis for the Global Burden of Disease Study 2017. The Lancet. DOI.

2. Wang et al. Use of mental health services for anxiety, mood, and substance disorders in 17 countries in the WHO world mental health surveys. The Lancet. 2007; 370(9590):841-50.

5.Cummins, Nicholas & Epps, Julien & Breakspear, Michael & Goecke, Roland. (2011). An Investigation of Depressed Speech Detection: Features and Normalization.. Proc. Interspeech. 2997-3000. 

6.Darby, J. K., “Speech and voice parameters of depression: A pilot study”, J. Commun. Disord., 17, 1984, pp. 75-85.

5.Afshan, Amber, Jinxi Guo, Soo Jin Park, Vijay Ravi, Jonathan Flint, and Abeer Alwan (2018) “Effectiveness of voice quality features in detecting depression.” In Proc. Interspeech (pp. 1676-1680)

6.Al Hanai, Tuka, Mohammad Ghassemi, and James Glass (2018) “Detecting depression with audio/text sequence modeling of interviews.” In Proc. Interspeech (pp. 1716-1720).

7.Gratch J, Artstein R, Lucas GM, Stratou G, Scherer S, Nazarian A, Wood R, Boberg J, DeVault D, Marsella S, Traum DR. The Distress Analysis Interview Corpus of human and computer interviews. InLREC 2014 May (pp. 3123-3128)

8.DeVault, D., Artstein, R., Benn, G., Dey, T., Fast, E., Gainer, A., Georgila, K., Gratch, J., Hartholt, A., Lhommet, M., Lucas, G., Marsella, S., Morbini, F., Nazarian, A., Scherer, S., Stratou, G., Suri, A., Traum, D., Wood, R., Xu, Y., Rizzo, A., and Morency, L.-P. (2014). “SimSensei kiosk: A virtual human interviewer for healthcare decision support”. In Proceedings of the 13th International Conference on Autonomous Agents and Multiagent Systems (AAMAS’14), Paris
