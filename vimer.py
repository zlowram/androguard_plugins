#!/usr/bin/env python

from androguard.decompiler.dad import decompile
from androguard.core.bytecodes.dvm import ClassDefItem
from androguard.core.bytecodes.dvm import EncodedMethod
from tempfile import mkstemp
import os

def vim(dx, obj):
    if isinstance(obj, ClassDefItem):
        dec = decompile.DvClass(obj, dx)
        dec.process()
    elif isinstance(obj, EncodedMethod):
        mt = dx.get_method(obj)
        dec = decompile.DvMethod(mt)
        dec.process()
    else:
        print "[HELPER] Error: Type of obj parameter is " + type(obj)

    vimopen(dec.get_source())

def vimopen(contents):
    fd, filename = mkstemp(suffix=".java")
    f = os.fdopen(fd, "w")
    f.write(contents)
    f.close()
    os.system("tmux split-window -h 'vim "+filename+" && rm -f "+filename+"'")
