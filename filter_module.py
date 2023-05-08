import scipy.signal as signal

class LowPassFilter:
    def __init__(self, cutoff_freq, sample_rate, filter_order):
        nyquist_rate = sample_rate / 2.0
        normalized_cutoff = cutoff_freq / nyquist_rate
        self.b, self.a = signal.butter(filter_order, normalized_cutoff, btype='lowpass')

    def apply(self, samples):
        return signal.filtfilt(self.b, self.a, x=samples)

