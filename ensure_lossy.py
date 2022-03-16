import pydub
import os
from tqdm import tqdm

DATA_FOLDER = 'data'
FLAC_FOLDER = DATA_FOLDER+'/flac'
ENCODED_FOLDER = DATA_FOLDER+'/encoded'

ENCODED_CODECS = {
    'libmp3lame': ('mp3', 'mp3'),
    #'aac' : ('m4a', 'adts'),
}

BITRATES = ['64k', '96k', '128k', '256k'] # '64k', '96k', '128k', '256k', '320k'

# go through every file in data/flac and create a corresponding mp3 file to data/mp3 with the same name
counter = 0
for flac in tqdm(os.listdir(FLAC_FOLDER), desc='Converting FLAC to Lossy', unit='files'):
    # if not exists, create file
    for codec, other in ENCODED_CODECS.items():
        file_ext, format_type = other
        filename = flac.split('.')[0]
        if flac.endswith('.flac') and not os.path.exists(ENCODED_FOLDER+'/'+filename+'.'+file_ext):
            counter += 1
            # load flac file
            flac_file = pydub.AudioSegment.from_file(FLAC_FOLDER+'/'+flac)
            # convert to lossy file
            for br in BITRATES:
                flac_file.export(f"{ENCODED_FOLDER}/{filename}.{br}.{file_ext}", format=format_type, bitrate=br, codec=codec)

if counter:
    print("Converted %d files" % counter)
else:
    print("No files to convert")