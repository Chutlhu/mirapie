#!/usr/bin/env python3

''' version          = 1.0.0,
    description      = 'Interference removal algorithm for multitrack live recordings via command line',
    long_description = long_description,
    classifiers      = [
        "Development Status :: 4 - Beta"
        "Environment :: Console",
        "Intended Audience :: Sound Engineers",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.5",
        "Topic :: Music Processing",
        "License :: OSI Approved :: GPL3 License",
        ],
    keywords         = 'interference reduction mira source separation python',
    author           = 'Diego Di Carlo',
    author_email     = 'diego.dicarlo89@gmail.com',
    maintainer       = 'Diego Di carlo',
    maintainer_email = 'diego.dicarlo89@gmail.com',
    url              = 'https://github.com/Chutlhu/mirapie',
    license          = 'GPL3    '''

print("\n   [ MIRA | SOUNDCHECK ]\n\n")

################################################################################
#           IMPORTS                                                            #
################################################################################

import os
import argparse     #for command line parser
import sys
import traceback    #for exception handling
import yaml
import numpy as np

from mira import Mira
from soundcheck_utils import soundcheck_preprocess

def load(preset_num):
    #Load preset in preset.yaml
    with open("preset.yml", "r") as file_descriptor:
        presets = yaml.load(file_descriptor)
    return presets[preset_num]

# check input params and add default configuration
def get_instructions(args):
    print('Path to the soundcheck data\n    ' + args['soundcheck_dir'])
    return args

# run che sound check
def run_soundcheck(args):
    params = get_instructions(args)


    # get soundcheck data
    names, datas, L, gains, mixture, fs, mix_name = soundcheck_preprocess(params)

    # estimate INTEFERENCE MATRIX from soundcheck data
    mode     = "soundcheck"
    function = "estim_interfernce"

    mr = Mira(settings   =  load(args["preset"]),
              soundcheck = True,
              filenames  = names,
              waveforms  = datas,
              int_matrix = L,
              function_mode = mode)
    mr.output_folder_path = mr.output_folder_path  + args["output"] + "/"
    if not os.path.exists(mr.output_folder_path):
        os.makedirs(mr.output_folder_path)
    
    L = mr.actions[mode][function](mr) # F x I x J

    # save L to file --- just in case
    np.save("./tmp_estimated_int_matrix.npy", L)

    # remove INTERFERENCE from the target multitrack mixture
    function = "remov_interfernce"
    mr.is_lambda_learning = False
    mr.fs = fs
    mr.actions[mode][function](mr, mixture, L)

    # post processing

def get_parser():
    #MANDATORY ARGS
    parser = argparse.ArgumentParser(description = 'Check and organize soundcheck data')
    parser.add_argument('soundcheck_dir',
                    help    = 'path to the folder containing the multichannel audio files [.wav].',
                    type    = str,
                    metavar = 'soundcheck_dir')
    parser.add_argument('song_path',
                    help    = 'path to the multichannel audio file [.wav].',
                    type    = str,
                    metavar = 'song_path')
    parser.add_argument('-p', '--preset',   help    = 'select one of the possible preset (default: 1)',
                                            type    = int,
                                            default = 1)
    parser.add_argument('-m', '--mode',     help    = 'select one of the possible mode (default: 0)',
                                            type    = int,
                                            default = 1)
    parser.add_argument('-o', '--output',   help    = 'output dir',
                                            type    = str,
                                            default = "song")
    return parser


def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())

    if (not args["soundcheck_dir"]):
        parser.print_help()
        return False

    return run_soundcheck(args)


if __name__ == '__main__':
    command_line_runner()
