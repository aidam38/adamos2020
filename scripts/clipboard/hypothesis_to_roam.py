#!/usr/bin/env python

import sys
import re

user = "aidam"

carry = ""
begun = False
ended = False
out = ""
bimbam = 0

for line in sys.stdin:
    if("in  Public" in line):
        begun = True
    if("Visit annotations in context" in line):
        ended = True

    if(begun and not ended):
        if(not (user in line or not re.search("^\d\d\s\w+\s\d\d\d\d$", line) == None or not line.strip())):
            if("in  Public" in line):
                bimbam = 0
            elif(bimbam == 0):
                carry = "\t- \"" + line.strip() + "\"" + "\n"
                bimbam = 1
            elif(bimbam == 1):
                carry = "- " + line.strip() + "\n" + carry
                bimbam = 0
        elif(bimbam == 1):
            carry = "- highlight\n" + carry.strip()
            bimbam = 0

        out = carry + out
        carry = ""

print(out)
