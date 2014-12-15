#!/usr/bin/env python

import re

def find_str(d, regexp):
    r = re.compile(regexp)
    strings = d.get_strings()
    for s in strings:
        m = r.search(s)
        if m != None:
            print "[MATCH FOUND] " + s 

def find_src(d, regexp):
    r = re.compile(regexp)
    for c in d.get_classes():
        source = c.get_source()
        m = r.search(source)
        if m != None:
            print "[MATCH FOUND] Found " + m.group(0) + " in class " + c.get_name()
