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

import argparse     #for command line parser
import sys
import logging      #for printing managing
import traceback    #for exception handling
import yaml
import numpy as np

from mira import Mira
from soundcheck import soundcheck_preprocess

#LOGGER
log = logging.getLogger("soundcheck")
log.setLevel(logging.DEBUG)
#standard output logger
formatter      = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
handler_stream = logging.StreamHandler()
handler_stream.setFormatter(formatter)
handler_stream.setLevel(logging.DEBUG)
log.addHandler(handler_stream)
#file soundcheck.log logger
handler_file = logging.FileHandler("soundcheck.log")
handler_file.setFormatter(formatter)
handler_file.setLevel(logging.DEBUG)
log.addHandler(handler_file)

def load(preset_num):
    #Load preset in preset.yaml
    with open("preset.yml", "r") as file_descriptor:
        presets = yaml.load(file_descriptor)
    try:
        return presets[preset_num]
    except Exception:
        log.critical("Wrong preset number")
    return False

# check input params and add default configuration
def get_instructions(args):

    try:
        log.info('Path to the multichannel track\n    ' + args['path_to_song'])
        log.info('Path to the soundcheck data\n    ' + args['path_to_soundcheck'])

        return args
    except Exception:
        log.critical(traceback.format_exc())
    return False

# run che sound check
def run_soundcheck(args):
    try:
        params = get_instructions(args)

        I, J = soundcheck_preprocess(params)
        preset_num = 2

        # MIRA on soundcheck
        for j in range(J):
            mr = Mira(   settings           = load(preset_num),
                         input_folder_path  = args["path_to_soundcheck"],
                         function_mode      = 4)
            Lj = mr.actions[4](mr,j)
            print(np.mean(Lj,0))
            if j == 0:
                F, I, _ = Lj.shape
                L = np.zeros((F,I,J))
            L[:,:,j] = Lj.squeeze()

        L0 = np.mean(L,0)
        np.save('soundcheckL.npy', L)

        # # MIRA on real recording
        # del mr
        # mr = Mira(  settings           = load(preset_num),
        #             input_folder_path  = args["path_to_song"],
        #             init_matrix_file   = args["path_to_song"][-5:] + '.csv',
        #             lambda_matrix_file = args["matrix"],
        #             function_mode      = 6)
        # return mr.actions[6](mr, L)


    except Exception:
        print('Error. Aborting.')
        log.critical(traceback.format_exc())

    return False


def get_parser():
    #MANDATORY ARGS
    parser = argparse.ArgumentParser(description = 'Check and organize soundcheck data')
    parser.add_argument('path_to_song',
                    help    = 'path to the multichannel audio files [.wav].',
                    type    = str,
                    metavar = 'path_to_song')
    parser.add_argument('path_to_soundcheck',
                        help    = 'path to the folder containing all the soundcheck data [directory].',
                        type    = str,
                        metavar = 'path_to_soundcheck')
    
    #OPTIONAL ARGS
    parser.add_argument('-c', '--check',    help    = 'Check soundcheck data.',
                                            type    = bool,
                                            default = True)
    parser.add_argument('-s', '--synch',    help    = 'Perform audio files syncronization.',
                                            type    = bool,
                                            default = False)
    parser.add_argument('-o', '--organize', help    = 'Re-organize all the data in a new folder.',
                                            type    = bool,
                                            default = True)
    return parser


def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())

    if (not args["path_to_song"])  & (not args["path_to_soundcheck"]):
        parser.print_help()
        return False

    return run_soundcheck(args)


if __name__ == '__main__':
    command_line_runner()
