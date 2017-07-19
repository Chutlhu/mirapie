# mirapie

## Multitrack Interference RemovAl for full-lenght live recordings
------------------------------------------------------------------

Example:

Using the toydata:

    $./mirapie  toydata/ toydata/initL.csv -p 1 -m 1

Multitrack dataset in `../Dataset/` and the `../Dataset/initL.csv` is the table containig the information about microphone channels and instruments

    $./mirapie    ../Dataset/   ../Dataset/initL.csv

## Installation
1 Setup the virtual enviroment, run it and intall all the dependencies

    $ virtualenv  venv -p python3
    $ source venv/bin/activate
    $ pip install -r requirements
## Usage

    $ ./mirapie.py -h
        MIRAPIE: Multitrack Interference RemovAl for full-lenght live recordings
        usage: 
            mirapie.py  path-to-wavs csv-matrix [-h] [-l MATRIX] [-p PRESET] [-m MODE]
        Python implementation for MIRA
        positional arguments:
            path-to-wavs        location of the multitrack recordings [.wav]
            csv-matrix          name of the initial interference matrix [.csv]
        optional arguments:
        -h, --help              show this help message and exit
        -l MATRIX, --matrix MATRIX   
                                L matrix file (default: None)
        -p PRESET, --preset PRESET
                                select one of the possible preset (default: 1)
        -m MODE, --mode MODE    select one of the possible mode (default: 0)
## Command line arguments
`path-to-wavs` : folder containing the audio recording in [.wav]
`csv-matrix`   : file containing info about mic channels and instrumens organized in a table [.csv]
`-p PRESET`    : present number in the user-editable yaml file `preset.yml`
`-m MODE`      : mode of the algorithm, `1` one chunk, `2` one chunk with random projection, `3` full-length with random projection.

__advance algorithm parameters__ in `preset.yml` file

## Author
Diego Di Carlo (`@Chutlhu <https://github.com/Chutlhu>`)

## Notes
-  Works only with Python3
-  A standalone Windows executable with the howdoi application _is not yet available_
-  Conference paper about mirapie can be downloaded `@here <https://hal.inria.fr/hal-01515971/file/gaussian-framework-interference.pdf>`
-  Special thanks to Antoine Liutkus and Thomas Praetzlich and Multispeech Team at INRIA GRAND EST.

## Development
- check the github repo `@mirapieDev <https://github.com/Chutlhu/mirapieDev>`

## Troubleshooting
- please write to `diego.dicarlo89@gmail.com` for any question

## License
GPL v3
