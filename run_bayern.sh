#!/bin/bash

source venv/bin/activate
rm mira.log

data='/home/ddicarlo/Documents/Datasets/LIVE_MUSIC_AND_SPORTS/INRIA_Buli_Bayern_V_TSG_18-09-07/Audio_Files/'
songs='01/'
initL='initL.csv'
python mirapie.py $data$songs $data$songs$initL -p 5 -m 1