from wav_module import WavFile
from filter_module import LowPassFilter
import wave
import numpy as np


# 读取音频文件并绘制其时域波形和频域谱图
input_wav = WavFile('test.wav')
input_wav.plot_waveform_and_spectrum()

# 创建低通滤波器，并将其应用于输入音频数据
lpf = LowPassFilter(cutoff_freq=2000, sample_rate=input_wav.framerate, filter_order=4)
filtered_samples = lpf.apply(input_wav.samples)

# 创建新的WAV文件，并写入滤波后的数据
output_wav = wave.open('example.wav', 'wb')
output_wav.setnchannels(input_wav.nchannels)
output_wav.setsampwidth(input_wav.sample_width)
output_wav.setframerate(input_wav.framerate)
output_wav.writeframes(np.array(filtered_samples).astype(input_wav.samples.dtype).tobytes())
output_wav.close()

# 读取滤波后的音频文件并绘制其时域波形和频域谱图
filtered_wav = WavFile('example.wav')
filtered_wav.plot_waveform_and_spectrum()
