import os
from tqdm import tqdm

DATA_FOLDER = 'data'
FLAC_FOLDER = DATA_FOLDER+'/flac'


def get_correct_name(flac_file):
    # get extension
    extension = flac_file.split('.')[-1]
    # get filename
    filename = flac_file[:-len(extension)-1]
    correct_name = filename.replace('.', '_').lower().replace(' ', '_').replace('-', '_').replace('__', '_').strip()+'.flac'
    return correct_name

for flac in tqdm(os.listdir(FLAC_FOLDER)):
    if flac.endswith('.flac'):
        correct_name = get_correct_name(flac)
        if flac != correct_name:
            os.rename(FLAC_FOLDER+'/'+flac, FLAC_FOLDER+'/'+correct_name)
