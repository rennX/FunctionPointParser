#! /usr/bin/env python

from FileIo import *
from InputProcessor import *

input = "../input.txt"

fio = FileIo(input)
ip = InputProcessor()

print ip.processInput(fio.getFile())
