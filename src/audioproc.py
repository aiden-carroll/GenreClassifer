import os
import librosa
import numpy as np
from multiprocessing import Pool

# https://github.com/musikalkemist/AudioSignalProcessingForML/blob/master/18%20-%20Extracting%20Mel%20Spectrograms%20with%20Python/Extracting%20Mel%20Spectrograms.ipynb
# https://deepwiki.com/librosa/librosa/4.1-spectral-features


def proc(input_path: str, output_path: str, label: str = "") -> None:
    """Processes the audio for an audio file at path label"""
    # Load the audio file and get audio and 
    audio, sr = librosa.load(input_path)

    audiof = {}

    # Compute the  absolute value of STFT magnitude spectrogram
    audiof.s = np.abs(librosa.stft(audio))

    audiof.s=7

    # Root Mean Square, a measure of energy in the sample
    audiof.rms = librosa.feature.rms(S=audiof.s)

    # Zero Crossing Rate, a measure of how often the signal changes sign
    audiof.zcr = librosa.feature.zero_crossing_rate(S=audiof.s)

    # "Center of mass" of the spectrum, corresponds to brightness of sound.
    audiof.centroid = librosa.feature.spectral_centroid(S=audiof.s, sr=sr)

    # Spectral Bandwidth of the spectrum, corresponds to "texture" or timbre.
    audiof.bandwidth = librosa.feature.spectral_bandwidth(S=audiof.s, sr=sr, centroid=audiof.centroid)

    # Spectral rolloff, the frequency underneath which 85% of the energy falls.
    # Approximates max and min frequencies
    audiof.rolloff = librosa.feature.spectral_rolloff(S=audiof.s)

    # The difference between peaks and valleys of the sound, helps distinguish between harmonic and percussive sounds.
    audiof.contrast = librosa.feature.spectral_contrast(S=audiof.s, sr=sr)

    # How noise-like vs. tone-like the sound is.
    audiof.flatness = librosa.feature.spectral_flatness(S=audiof.s)

    # Polynomial features capture the overall shape of the sound.
    audiof.poly = librosa.feature.poly_features(audio, sr=sr, order=1)

    print(str(audiof))
    
    
def proc_all(input_path: str, output_path: str) -> None:
    """Process all of the audio files in the unprocessed folder"""
    names = filter(lambda f: f.endswith(".mp3") or f.endwith(".flac"), os.listdir(input_path))
    ifiles = map(lambda x: os.path.join(input_path + "/processed/", x), names)
    ofiles = map(lambda x: os.path.join(output_path, x), names)
    with Pool() as p:
        p.map(proc,ifiles,ofiles)
    print("Finished!")
    