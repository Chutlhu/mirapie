import os
import glob
import logging
import matplotlib.pyplot as plt
import wavio
import numpy as np
import librosa as lr
import soundfile as sf

from utils.gcc_phat 	import gcc_phat
from beautifultable 	import BeautifulTable
from scipy.stats.mstats import mquantiles

from utils import wav, stft

window_sec = 0.5 # seconds
hop_size   = 1024 # samples

log = logging.getLogger("soundcheck")
dims_tab = BeautifulTable()
dims_tab.column_headers = ["FILE", "FS [Hz]", "LEN [sec]", "CHAN", "WIDTH [bit/sec]"]

def load_wav(path_to_audio_file):
	song = wavio.read(path_to_audio_file)
	# extract infos
	data = song.data
	data, fs = sf.read(path_to_audio_file)
	n_smpl, n_chans = data.shape
	fs = song.rate
	sample_width = song.sampwidth
	name = path_to_audio_file.split('/')[-1]
	return (name, data, n_smpl, n_chans, fs, sample_width)

def compute_gains(energy):
    gain = mquantiles(energy, prob = 0.05, axis = 0)[:,0]**(1/2)
    print(gain)
    return gain

def load_and_resample(path_to_audio_file, fs, max_duration):
	wav, fs = sf.read(path_to_audio_file)
	wav = wav - np.mean(wav, 0)
	return wav

def soundcheck_preprocess(args):

	## MULTICHANNEL SONG
	# check input data
	(name, data, n_smpl, n_chans, fs, sample_width) = load_wav(args['path_to_song'])
	duration = str(int((n_smpl/fs)//60)) + ':' + str(int((n_smpl/fs)%60))
	dims_tab.append_row([name, fs, duration, n_chans, sample_width])

	## SOUNDCHECK FILES
	soundcheck_filenames = glob.glob(args['path_to_soundcheck'] + '*.wav')
	soundcheck_filenames = sorted(soundcheck_filenames)
	for file in soundcheck_filenames:
		(name, data, new_n_smpl, new_n_chans, new_fs, new_sample_width) \
				= load_wav(file)
		duration = str(int((new_n_smpl/new_fs)//60)) + ':' + str(int((new_n_smpl/new_fs)%60))
		dims_tab.append_row([name , new_fs, duration, new_n_chans, new_sample_width])
		if fs != new_fs or n_chans != new_n_chans or sample_width != new_sample_width:
			raise ValueError('Waveform information is different among in the soundcheck')
		(fs, n_chans, n_smpl, sample_width) = (new_fs, new_n_chans, new_n_smpl, new_sample_width)

	I = n_chans # number of microphones
	J = len(soundcheck_filenames) # number of sources
	
	print(dims_tab)
	print("I :", I)
	print("J :", J)

	## from recording_per_instr to recording_per_mic
	subdir = 'mics/'
	instr_list = [load_wav(soundcheck_filenames[j]) for j in range(J)]
	(_, _, N, _, fs, _) = instr_list[0]
	for i in range(I):

		mic_wav = np.zeros((N,J))

		for j in range(J):
			mic_wav[:,j] = instr_list[j][1][:,i]

		save_as = args['path_to_soundcheck'] + subdir + 'mic_' + str(i) + '.wav'
		sf.write(save_as, mic_wav, fs)
	
	sound_check_mics_filenames = glob.glob(args['path_to_soundcheck'] + subdir)
	return I, J