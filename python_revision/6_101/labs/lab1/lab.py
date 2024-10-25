"""
6.101 Lab:
Audio Processing
"""

import copy
import wave
import struct

# No additional imports allowed!


def backwards(sound):
    """
    Returns a new sound containing the samples of the original in reverse
    order, without modifying the input sound.

    Args:
        sound: a dictionary representing the original mono sound

    Returns:
        A new mono sound dictionary with the samples in reversed order
    """
    return {"rate": sound["rate"], "samples": list(reversed(sound["samples"]))}


def mix(sound1, sound2, p):
    """

    Args:
        sound1: dictionary representing a sound
        sound2: dictionary representing a sound
        p: p value

    Returns: dictionary combining the sounds

    """
    if sound1["rate"] != sound2["rate"]:
        return None
    l1 = len(sound1["samples"])
    l2 = len(sound2["samples"])
    l = l1 - l2
    lst = [x * p + y * (1 - p) for x, y in zip(sound1["samples"], sound2["samples"])]
    if l < 0:
        lst.extend([p * sound1["samples"][x] for x in range(l2, l1)])
    elif l > 0:
        lst.extend([(1 - p) * sound2["samples"][x] for x in range(l1, l2)])
    return {"rate": sound1["rate"], "samples": lst}


def echo(sound, num_echoes, delay, scale):
    """
     Compute a new signal consisting of several scaled-down and delayed versions
     of the input sound. Does not modify input sound.

     Args:
         sound: a dictionary representing the original mono sound
         num_echoes: int, the number of additional copies of the sound to add
         delay: float, the amount of seconds each echo should be delayed
         scale: float, the amount by which each echo's samples should be scaled
    >>>inp = {
             "rate": 9,
             "samples": [1, 2, 3],
         }
     >>>    inp2 = copy.deepcopy(inp)
     >>>    exp = {
             "rate": 9,
             "samples": [1, 2, 3, 0, 0, 0.7, 1.4, 2.1, 0, 0, 0.49, 0.98, 1.47],
         }
     >>> echo(inp, 2, 0.6, 0.7)== exp
     True
     Returns:
         A new mono sound dictionary resulting from applying the echo effect.
    """
    sample_delay = round(delay * sound["rate"])
    samples = sound["samples"][:]
    n1 = len(samples)
    # expected=samples+[0 for _ in range(sample_delay)]
    # #expected*=num_echoes
    # n = len(expected)
    #
    # for i in range(1,num_echoes+1):
    #
    #     expected+=expected[]
    #
    #
    # #breakpoint(n==num_echoes*sample_delay)
    #
    # expected = [samples[i]*scale**i for i in range(sample_delay,n) ]
    # return {
    #     'rate': sound['rate'],
    #     'samples': expected
    # }
    pass


def pan(sound):
    raise NotImplementedError


def remove_vocals(sound):
    raise NotImplementedError


# below are helper functions for converting back-and-forth between WAV files
# and our internal dictionary representation for sounds


def load_wav(filename, stereo=False):
    """
    Load a file and return a sound dictionary.

    Args:
        filename: string ending in '.wav' representing the sound file
        stereo: bool, by default sound is loaded as mono, if True sound will
            have left and right stereo channels.

    Returns:
        A dictionary representing that sound.
    """
    sound_file = wave.open(filename, "r")
    chan, bd, sr, count, _, _ = sound_file.getparams()

    assert bd == 2, "only 16-bit WAV files are supported"

    out = {"rate": sr}

    left = []
    right = []
    for i in range(count):
        frame = sound_file.readframes(1)
        if chan == 2:
            left.append(struct.unpack("<h", frame[:2])[0])
            right.append(struct.unpack("<h", frame[2:])[0])
        else:
            datum = struct.unpack("<h", frame)[0]
            left.append(datum)
            right.append(datum)

    if stereo:
        out["left"] = [i / (2**15) for i in left]
        out["right"] = [i / (2**15) for i in right]
    else:
        samples = [(ls + rs) / 2 for ls, rs in zip(left, right)]
        out["samples"] = [i / (2**15) for i in samples]

    return out


def write_wav(sound, filename):
    """
    Save sound to filename location in a WAV format.

    Args:
        sound: a mono or stereo sound dictionary
        filename: a string ending in .WAV representing the file location to
            save the sound in
    """
    outfile = wave.open(filename, "w")

    if "samples" in sound:
        # mono file
        outfile.setparams((1, 2, sound["rate"], 0, "NONE", "not compressed"))
        out = [int(max(-1, min(1, v)) * (2**15 - 1)) for v in sound["samples"]]
    else:
        # stereo
        outfile.setparams((2, 2, sound["rate"], 0, "NONE", "not compressed"))
        out = []
        for l_val, r_val in zip(sound["left"], sound["right"]):
            l_val = int(max(-1, min(1, l_val)) * (2**15 - 1))
            r_val = int(max(-1, min(1, r_val)) * (2**15 - 1))
            out.append(l_val)
            out.append(r_val)

    outfile.writeframes(b"".join(struct.pack("<h", frame) for frame in out))
    outfile.close()


if __name__ == "__main__":
    # Code placed inside the if __name__ == "__main__" statement will only
    # be executed when you run the lab.py file.

    # Code placed in this special if statement will not be executed when you run
    # the tests in the test.py file or when you submit your code to the submission
    # server.

    # This makes it a good place to put your code for generating and saving
    # sounds, or any other code you write for testing on your computer.

    # Note that your checkoff conversation with a staff member will likely involve
    # showing and discussing the code you wrote to generate the sounds that you
    # submitted on the lab page, so please do not delete that code. However, you
    # can comment it out.

    # Here is an example of loading a file (note that this is specified as
    # sounds/hello.wav, rather than just as hello.wav, to account for the
    # sound files being in a different directory than this file):

    print("Loading hello file...")
    hello = load_wav("sounds/hello.wav")

    # write_wav(backwards(hello), "hello_reversed.wav")
