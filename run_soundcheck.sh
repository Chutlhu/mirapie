#!/bin/bash

# data='/home/ddicarlo/Documents/Datasets/MOBILE_MUSIC_RECORDINGS/'
# songs='songs/'
# soundcheck='soundchecks/'
# song='2017-09-14T00.26.11Z-ivanna-musictester67_rec21'
# song='2017-02-07T02.32.40Z-leenlaura_rec9'

# python soundcheck_setup.py $data$songs$song'.wav' $data$soundcheck$song'/'

source venv/bin/activate

data='/home/ddicarlo/Documents/Datasets/MOBILE_MUSIC_RECORDINGS_ALIGN/'
songs='songs/'
soundcheck='soundchecks/'
song='2017-02-07T22.00.30Z-blanco2_rec31'
song='2017-02-07T02.32.40Z-leenlaura_rec9'

# echo "processing: $song"
# python soundcheck.py $data$soundcheck$song'/' $data$songs$song'.wav' -p 2 -o $song

for song in 2016-12-27T02.42.27Z-Vocal_rec43 \
			2017-02-06T16.18.40Z-iliminal_rec45 \
			Artronerock_Song2 dlblive_Loveseat_song6_all_mics \
			dlblive_take2onlyApple \
			fabiola21_rec21 \
			2017-02-06T19.45.54Z-theGLOVE_rec36 \
			2017-02-06T20.44.59Z-natedviau_rec17 \
			2017-02-07T02.32.40Z-leenlaura_rec9 \
			2017-02-07T18.00.30Z-JMB_rec33 \
			2017-02-07T19.19.33Z-layth_rec13 \
			2017-02-07T21.32.08Z-blanco_rec22 \
			2017-02-07T22.00.30Z-blanco2_rec25 \
			2017-02-07T22.00.30Z-blanco2_rec31 \
			2017-02-11T23.43.00Z-thevitals_rec16 \
			2017-02-11T23.43.00Z-thevitals_rec21 \
			2017-04-08T22.20.54Z-NamoradosDaLua_rec81 \
			2017-06-10T19.46.34Z-Harde-musictester2_rec19 \
			2017-07-05T22.24.04Z-Stonerock-musictester53_rec13 \
			2017-07-07T15.34.28Z-Postiance-musictester54_rec45 \
			2017-07-07T15.34.28Z-Postiance-musictester54_rec49 \
			2017-07-07T15.34.28Z-Postiance-musictester54_rec53 \
			2017-07-07T15.34.28Z-Postiance-musictester54_rec65 \
			2017-09-12T18.52.02Z-giulia2-musictester66_rec10 \
			2017-09-12T18.52.02Z-giulia2-musictester66_rec7 \
			2017-09-14T00.26.11Z-ivanna-musictester67_rec21 \
			2017-09-14T00.26.11Z-ivanna-musictester67_rec26 \
			2017-09-14T00.26.11Z-ivanna-musictester67_rec31 \
			2017-09-14T00.26.11Z-ivanna-musictester67_rec36 \
			2017-09-14T00.26.11Z-ivanna-musictester67_rec41 \
			2017-09-14T00.26.11Z-ivanna-musictester67_rec46 \
			2017-09-14T00.26.11Z-ivanna-musictester67_rec51 \
			2017-09-14T22.27.01Z-olivia-musictester68_rec13 \
			2017-09-14T22.27.01Z-olivia-musictester68_rec9 \
			2017-09-15T22.07.20Z-sarah-musictester69_rec13 \
			2017-09-15T22.07.20Z-sarah-musictester69_rec9 \
			2017-09-18T20.13.10Z-ben-musictester70_rec13 \
			2017-09-18T20.13.10Z-ben-musictester70_rec17 \
			2017-09-18T20.13.10Z-ben-musictester70_rec9 \
			2017-09-18T20.32.57Z-ben1-musictester70_rec13 \
			2017-09-18T20.32.57Z-ben1-musictester70_rec17 \
			2017-09-18T20.32.57Z-ben1-musictester70_rec9 \
			2017-09-20T20.00.08Z-jon-musictester71_rec7 \
			2017-09-20T20.14.34Z-jon1-musictester71_rec7 \
			2017-09-22T20.15.00Z-ana1-musictester72_rec10
do
		echo "processing: $song"
		python soundcheck.py $data$soundcheck$song'/' $data$songs$song'.wav' -p 3 -o $song
done
