import deepspeech
import numpy as np
import os
import pyaudio
import time

# DeepSpeech parameters
model_file_path = '/home/pi/env/deepspeech-0.9.3-models.tflite'
scorer_file_path = '/home/pi/env/deepspeech-0.9.3-models.scorer'
lm_alpha = 0.75
lm_beta = 1.85
beam_width = 500

# Make DeepSpeech Model
model = deepspeech.Model(model_file_path)
model.enableExternalScorer(scorer_file_path)
model.setScorerAlphaBeta(lm_alpha, lm_beta)
model.setBeamWidth(beam_width)

# Create a Streaming session
ds_stream = model.createStream()

# Encapsulate DeepSpeech audio feeding into a callback for PyAudio
text_so_far = ''
def process_audio(in_data, frame_count, time_info, status):
    global text_so_far
    data16 = np.frombuffer(in_data, dtype=np.int16)
    ds_stream.feedAudioContent(data16)
    text = ds_stream.intermediateDecode()
    if text != text_so_far:
        print('Interim text = {}'.format(text))
        text_so_far = text
    return (in_data, pyaudio.paContinue)

# PyAudio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK_SIZE = 1024

# Feed audio to deepspeech in a callback to PyAudio
audio = pyaudio.PyAudio()
stream = audio.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=16000,
    input=True,
    frames_per_buffer=1024,
    stream_callback=process_audio
)
print('Please start speaking, when done press Ctrl-C ...')
stream.start_stream()

try: 
    while stream.is_active():
        time.sleep(0.1)
except KeyboardInterrupt:
    # PyAudio
    stream.stop_stream()
    stream.close()
    audio.terminate()
    print('Finished recording.')
    # DeepSpeech
    text = ds_stream.finishStream()
    print('Final text = {}'.format(text))