import numpy
import soundfile as sf
import librosa
import warnings
import matplotlib.pyplot as plt

def load_flac_to_numpy(filename):
    data, samplerate = sf.read(filename)
    return data, samplerate

def load_mp3_to_numpy(filename, filter_warnings=True):
    # filter warnings from librosa
    if filter_warnings:
        warnings.filterwarnings('ignore')
    data, samplerate = librosa.load(filename, sr=None, mono=False)
    data = data.T
    return data, samplerate

# slice audio file into samples of size n_samples with numpy
def slice_audio(audio, n_samples, bit_depth=numpy.float16):
    # ensure N bit audio
    audio = audio.astype(bit_depth)
    # get number of samples
    n_samples_audio = len(audio)
    # get number of slices
    n_slices = n_samples_audio // n_samples
    # ensure audio is divisible by n_samples
    if n_samples_audio % n_samples != 0:
        # resize
        audio = audio[:n_samples * n_slices]
    # slice audio into samples
    slices = numpy.split(audio, n_slices)
    return numpy.array(slices, dtype=bit_depth)


# perform FFT on audio
def fft_audio(audio):
    # perform fft
    fft = numpy.fft.fft(audio)
    return fft

# convert fft back into audio file
def fft_to_audio(fft):
    # convert fft to audio
    audio = numpy.fft.ifft(fft)
    return audio


# Some testing...
if __name__ == '__main__':
    DATA_FOLDER = 'data'
    FLAC_FOLDER = DATA_FOLDER+'/flac'
    ENCODED_FOLDER = DATA_FOLDER+'/encoded'

    test_flac = '2l_145_01_stereo_01_cd.flac'
    print("Loading file...")
    data, samplerate = load_mp3_to_numpy(FLAC_FOLDER+'/'+test_flac)
    print(data)
    print(data.shape, "samplerate:", samplerate)
    print("Slicing audio...")
    slices = slice_audio(data, n_samples=16000)
    print(slices.shape)
    print(slices[0])

    #print("FFTing audio...")
    #ffts = fft_audio(data)
    #print(ffts.shape)
