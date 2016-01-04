#!/usr/bin/python
#coding:utf-8

import sys
from scikits.audiolab import wavread
from scikits.talkbox.features import mfcc
from modules.frame import getFrameSize

def generateMfcc(wavFile):
    audio, fs, enc = wavread(wavFile)
    size = getFrameSize(wavFile)

    ceps, mspec, spec = mfcc(audio, nwin=size, nfft=size, fs=fs, nceps=13)

    return ceps

if __name__ == "__main__":
    print generateMfcc(sys.argv[1])

