#!/usr/bin/env python

import sys
import re

input = sys.stdin.read()

# p = re.compile("^\s+\#")
p = re.compile("(\s+#|\s+- #)")
output = p.sub("\n\n#", input)

for line in output.split("\n"):
    s = re.search("\s+-", line)
    if(s != None):
        p2 = re.compile(s.group())
        output = p2.sub("    -", output)
        print()
        break

print(output)
