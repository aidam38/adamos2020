#!/usr/bin/env python

import sys
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--page', help='page from which you want to copy your notes to the end')
args = vars(parser.parse_args())
start_page = int(args['page'])

begun = False
past = False
carry_pre = ""
carry_post = ""
highlight = ""
page = 0
out = ""

for line in sys.stdin:
    if(("Yellow highlight | " in line or "Note | " in line) and not begun):
        begun = True
    if(begun):
        if("Yellow highlight" in line):
            carry_pre = "\t- \""
            page = re.search("\d+", line).group()
            carry_post = "\" (page " + page + ")"
        elif("Note |" in line):
            carry_pre = ""
            page = re.search("\d+", line).group()
            carry_post = " (page " + page + ")"
            highlight = ""
        elif(int(page) >= start_page):
            if("Note:" in line):
                out += "- " + re.sub("Note:", "", line)
                out += highlight
            elif(line.strip()):
                highlight = carry_pre + line.rstrip() + carry_post + "\n"

print(out)
