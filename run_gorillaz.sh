#!/bin/bash

source venv/bin/activate
rm mira.log

data='/home/ddicarlo/Documents/Datasets/LIVE_MUSIC_AND_SPORTS/Gorillaz/'
songs='song1/'
initL='initL.csv'
python mirapie.py $data$songs $data$songs$initL -p 3 -m 1