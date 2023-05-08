import wave
import numpy as np
import matplotlib.pyplot as plt


# 定义一个WAV文件读取类，用于读取并分析音频数据
class WavFile:
    def __init__(self, filename):
        self.filename = filename
        self.wavefile = wave.open(filename, 'rb')
        self.nchannels = self.wavefile.getnchannels()
        self.sample_width = self.wavefile.getsampwidth()
        self.framerate = self.wavefile.getframerate()
        self.nframes = self.wavefile.getnframes()
        self.duration = self.nframes / float(self.framerate)
        self.frames = self.wavefile.readframes(self.nframes)
        self.samples = np.frombuffer(self.frames, dtype='int16')

    # 计算音频的FFT频谱，并返回幅度和相位谱
    def calc_fft_spectrum(self):
        window = np.hamming(len(self.samples))
        spectrum = np.fft.fft(window*self.samples)
        freqs = np.fft.fftfreq(len(spectrum))
        return freqs[:len(freqs)//2], abs(spectrum)[:len(spectrum)//2], np.angle(spectrum)[:len(spectrum)//2]

    # 绘制音频的时域波形和频域谱图
    def plot_waveform_and_spectrum(self):
        fig, ax = plt.subplots(2, 1, figsize=(15, 8))
        ax[0].plot(np.arange(len(self.samples)) / float(self.framerate), self.samples)
        ax[0].set_xlabel('Time (s)')
        ax[0].set_ylabel('Amplitude')
        freqs, spectrum, _ = self.calc_fft_spectrum()
        ax[1].plot(freqs, spectrum)
        ax[1].set_xlabel('Frequency (Hz)')
        ax[1].set_ylabel('Magnitude')
        plt.show()
