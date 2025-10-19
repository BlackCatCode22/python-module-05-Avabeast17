# regex_extract.py
# From a mailbox file, extract X-DSPAM-Confidence values and print the maximum.

import re

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

vals = []
for line in open(fname):
    line = line.rstrip()
    stuff = re.findall(r"^X-DSPAM-Confidence:\s*([0-9.]+)", line)
    if len(stuff) != 1:
        continue
    vals.append(float(stuff[0]))

if vals:
    print(max(vals))
else:
    print("No matching lines found.")