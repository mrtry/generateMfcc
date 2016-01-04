#!/usr/bin/python
#coding:utf-8

import sys
import os
from scikits.audiolab import wavread
from scikits.talkbox.features import mfcc
from modules.frame import getFrameSize
from modules.cmd import execute, getFileName, rm

def generateMfcc(wavFile):
    filteredFile = filtering(wavFile, 2800, 3400)
    audio, fs, enc = wavread(filteredFile)
    size = getFrameSize(filteredFile)

    ceps, mspec, spec = mfcc(audio, nwin=size, nfft=size, fs=fs, nceps=13)

    return ceps

def filtering(wavFile, x0, x1):
    fileName, ext = os.path.splitext(wavFile)

    fileName = fileName.replace('(', '\(')
    fileName = fileName.replace(')', '\)')

    filteredFile = '%s_filtered.wav' % fileName

    cmd = 'sox %s.wav %s sinc %d-%d norm' % (fileName, filteredFile, x0, x1)
    execute(cmd)

    filteredFile = filteredFile.replace('\(', '(')
    filteredFile = filteredFile.replace('\)', ')')

    return filteredFile

if __name__ == "__main__":
    print generateMfcc(sys.argv[1])

