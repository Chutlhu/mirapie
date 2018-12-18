#!/bin/bash

# data='/home/ddicarlo/Documents/Datasets/MOBILE_MUSIC_RECORDINGS/'
# songs='songs/'
# soundcheck='soundchecks/'
# song='2017-09-14T00.26.11Z-ivanna-musictester67_rec21'
# song='2017-02-07T02.32.40Z-leenlaura_rec9'

# python soundcheck_setup.py $data$songs$song'.wav' $data$soundcheck$song'/'

data='/home/ddicarlo/Documents/Datasets/MOBILE_MUSIC_RECORDINGS/'
songs='songs/'
soundcheck='soundchecks/'
song='2017-09-14T00.26.11Z-ivanna-musictester67_rec21'
song='2017-02-07T02.32.40Z-leenlaura_rec9'

python mirapie.py $data$songs$song $data$songs$song'/'$song'.csv' -l 'soundcheckL.npy' -p 3 -m 1