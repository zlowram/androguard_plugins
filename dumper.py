#!/usr/bin/env python

from utils import str_to_filename
import os

def dump_all(d, folder):
    if os.path.exists(folder):
        raise Exception("Folder exists")
    os.makedirs(folder)
    for c in d.get_classes():
        filename = str_to_filename(c.get_name()) + ".java"
        absfilename = os.path.join(folder, filename)
        print "Dumping " + absfilename
        f = open(os.path.join(folder, absfilename), "w")
        f.write(c.get_source())
        f.close()
