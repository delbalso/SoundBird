import pyaudio
import time
import numpy as np
from matplotlib import pyplot as plt

CHUNKSIZE = 1024 # fixed chunk size

class Stream(object):
    def __init__(self):
# initialize portaudio
        p = pyaudio.PyAudio()
        self.stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=CHUNKSIZE)
        #plt.ion()

    def getSpeed(self):
# do this as long as you want fresh samples
        data = self.stream.read(CHUNKSIZE, exception_on_overflow=False)
        recorded_data = np.fromstring(data, dtype=np.int16)
        Y    = np.fft.fft(recorded_data)
        freq = np.fft.fftfreq(CHUNKSIZE, 1/float(44100))
        data = np.squeeze(np.dstack((np.absolute(Y), freq)))[1:511]
        highest_freq = data[data[:,0].argmax(),1]
        print "original freq: {0}".format(highest_freq)

# plot data
        #plt.cla()
        #plt.yscale('log')
        #plt.xlim(xmin=100)
        #plt.xlim(xmax=20000)
        #plt.ylim(ymin=100)
        #plt.plot(data[:,1],data[:,0])
        return highest_freq

# close stream
#stream.stop_stream()
#stream.close()
#p.terminate()
