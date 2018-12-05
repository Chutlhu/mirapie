#!/bin/bash

data='/home/ddicarlo/Documents/Datasets/MOBILE_MUSIC_RECORDINGS/'
songs='songs/'
soundcheck='soundchecks/'
song='2017-09-14T00.26.11Z-ivanna-musictester67_rec21'

python soundcheck_setup.py $data$songs$song'.wav' $data$soundcheck$song'/'