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
        if(not (user in line or "in  Public" in line or not re.search("^\d\d\s\w+\s\d\d\d\d$", line) == None or not line.strip())):
            if(bimbam == 0):
                carry = "\t- \"" + line.strip() + "\""
                bimbam = 1
            elif(bimbam == 1):
                out = carry + "\n" + out
                out = "- " + line + out
                bimbam = 0

print(out)
