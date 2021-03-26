#!/usr/bin/python

import os
import stat
import glob

all_files = glob.glob("/root/*")
out = open("/tmp/answer.txt", "w")

for fname in all_files:
    try:
        with open(fname) as f:
            out.write("[" + fname + "]\n\n")
            for line in f:
                out.write(line + "\n")
    except:
        out.write("can't open " + fname + "\n")
