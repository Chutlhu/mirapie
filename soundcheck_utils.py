import os
import glob
import matplotlib.pyplot as plt
import wavio
import numpy as np

import soundfile as sf

from beautifultable 	import BeautifulTable
from scipy.stats.mstats import mquantiles

from utils import wav, stft

window_sec = 0.5 # seconds
hop_size   = 1024 # samples

dims_tab = BeautifulTable()
dims_tab.column_headers = ["FILE", "FS [Hz]", "LEN [sec]", "CHAN"]

def samples_to_seconds_str(n_smpl, fs):
	return str(int((n_smpl/fs)//60)) + ':' + str(int((n_smpl/fs)%60))

def load_wav(path_to_audio_file):
	data, fs = sf.read(path_to_audio_file, dtype='float64')
	# extract infos
	n_smpl, n_chans = data.shape
	name = path_to_audio_file.split('/')[-1]
	# remove dc
	data -= np.mean(data,axis = 0)
	return (name, data, n_smpl, n_chans, fs)

# def compute_gains(energy):
#     gain = mquantiles(energy, prob = 0.05, axis = 0)[:,0]**(1/2)
#     return gain

def soundcheck_preprocess(args):

	## MULTICHANNEL SONG
	# list soundcheck files
	soundcheck_filenames = glob.glob(args['soundcheck_dir'] + '*.wav')
	soundcheck_filenames = sorted(soundcheck_filenames)

	# check input data
	for j, file in enumerate(soundcheck_filenames):
		print("  Processing: ", file.split("/")[-1])
		(name, data, n_smpl, n_chans, fs) = load_wav(file)
		duration = samples_to_seconds_str(n_smpl, fs)
		dims_tab.append_row([name , fs, duration, n_chans])

		if j == 0:
			J = len(soundcheck_filenames) # number of instruments
			I = n_chans # number of microphones
			N = n_smpl	# length of signals in samples

			gains = np.zeros((I,J))
			gains2 = np.zeros((I,J))
			datas = np.zeros((I,J,N))
			names = []

		if n_chans != I:
			print(dims_tab)
			raise ValueError('Number of channels is different')
	
		## estimate gains
		for i in range(I):
			gains[i,j] = np.mean(np.abs(data[:,i])**2) 	# I x J
			datas[i,j,:] = data[:,i]					# I x J x N

		names.append(name)

	print(dims_tab)
	print("I :", I)
	print("J :", J)

	# Lambda matrix initialization from the gains
	L = gains/np.sum(gains,1)[...,None]

	return names, datas, L, gains