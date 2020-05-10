#!/usr/bin/env python

import sys
import re

begun = False
carry_pre = ""
carry_post = ""
out = ""
for line in sys.stdin:
    if(("Yellow highlight | " in line or "Note | " in line) and not begun):
        begun = True
    if(begun):
        if("Yellow highlight" in line):
            carry_pre = "- \""
            carry_post = "\" (page " + re.search("\d+", line).group() + ")"
        elif("Note |" in line):
            carry_pre = ""
            carry_post = " (page " + re.search("\d+", line).group() + ")"
        elif("Note:" in line):
            out += "\t- " + re.sub("Note:", "", line)
        elif(line.strip()):
            out += carry_pre + line.rstrip() + carry_post + "\n"

print(out)
