# hashing of folder structure and file contents
import hashlib
import os
import numpy

def save_checksum(checksum):
    # save checksum to file
    with open('checksum.txt', 'w') as f:
        f.write(checksum)

def get_checksum():
    # get checksum from file
    try:
        with open('checksum.txt', 'r') as f:
            return f.read()
    except FileNotFoundError:
        return None

def save_to_cache(folder, trainX, trainY):
    # get checksum
    checksum = _checksum(folder)
    # save checksum to file
    save_checksum(checksum)

    # save trainX to file
    numpy.save(folder+'/trainX.npy', trainX)
    # save trainY to file
    numpy.save(folder+'/trainY.npy', trainY)

def load_from_cache(folder):
    # get checksum
    checksum = get_checksum()
    if checksum is None:
        return None, None
    # get checksum from file
    checksum_file = _checksum(folder)
    # check if checksums match
    if checksum == checksum_file:
        # load trainX from file
        trainX = numpy.load(folder+'/trainX.npy')
        # load trainY from file
        trainY = numpy.load(folder+'/trainY.npy')
        return trainX, trainY
    else:
        return None, None


def _checksum(folder):
    # create a hash object
    hash_md5 = hashlib.md5()
    # get all files in folder
    files = os.listdir(folder)
    # loop through each file
    for file in files:
        # get file path
        path = os.path.join(folder, file)
        # check if path is a file
        if os.path.isfile(path):
            # read the file
            with open(path, "rb") as f:
                # loop through the file
                for chunk in iter(lambda: f.read(4096), b""):
                    # update the hash object
                    hash_md5.update(chunk)
            # include path to file in hash
            hash_md5.update(path.encode('utf-8'))
    # return the hex digest
    return hash_md5.hexdigest()