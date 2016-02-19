from pydub import AudioSegment

sound1 = AudioSegment.from_wav("song.wav")
sound2 = AudioSegment.from_wav("sound1.wav")

combined_sounds = sound1.overlay(sound2, position = 0)
combined_sounds.export("song3.wav", format="wav")