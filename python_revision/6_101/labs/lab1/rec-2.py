# 6.101 recitation: lab 0 wrapup


############### Data representation

# sound is a dictionary, with keys
#    rate: int, the sampling rate, in samples per second
#    samples: a list of floats, the samples
sound = {"rate": 8000, "samples": [1, 2, 3]}
sound["rate"]
sound["samples"]

# OR:
# sound is a list whose first element is the rate and second is a sublist
# containing the samples
sound = [8000, [1, 2, 3]]
sound[0]
sound[1]

# OR:
# sound is a list whose first element is the rate, and remaining elements the
# samples
sound = [8000, 1, 2, 3]
sound[0]
sound[1:]


# OR: (coming later in semester)
# class Sound:
#    ...
# sound = Sound(8000, [1,2,3])
# sound.rate
# sound.samples
# isinstance(sound, Sound) ==> True


############### backwards

# what's good about this solution to backwards()?
# what could be improved?
# what might be buggy?


def backwards(sound):
    new_samples = sound["samples"]
    new_samples.reverse()
    return {
        "rate": sound["rate"],
        "samples": new_samples,
    }


############### mix


def mix(sound1, sound2, p):
    # initialize a new sound
    new_sound = {}

    # scale the input sounds by p and 1-p
    sound1_scaled = []
    for s in sound1["samples"]:
        sound1_scaled.append(s * p)
    sound2_scaled = []
    for s in sound1["samples"]:
        sound2_scaled.append(s * 1 - p)

    # combine the scaled sounds
    new_samples = []
    if len(sound1_scaled) < len(sound2_scaled):
        new_length = len(sound2_scaled)
    else:
        new_length = len(sound1_scaled)
    new_samples = [0] * new_length
    for i in range(new_length):
        new_samples[i] = sound1_scaled[i] + sound2_scaled[i]

    # fill in the new sound with the new samples
    new_sound["rate"] = sound["rate"]
    new_sound["samples"] = []
    for sample in new_samples:
        new_sound["samples"].append(sample)

    # return the mixed sound
    return new_sound


def scale(samples, p):
    """Return a new sample list that multiplies every element of samples by p."""
    pass


def add(samples1, samples2):
    """Add two sample lists elementwise, returning a new list."""
    pass
