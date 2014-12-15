#!/usr/bin/env python

from androguard.core.analysis.analysis import TaintedVariable
from androguard.core.bytecodes.dvm import ClassDefItem
from androguard.core.bytecodes.dvm import EncodedMethod 
from androguard.core.analysis.analysis import show_Paths 

def xrefs(d, dx, obj):
    if isinstance(obj, str):
        s = dx.tainted_variables.get_string(obj)
        if s != None:
            print "[XREFS] XREFS for " + s.get_info() + ":\n"
            s.show_paths(d)
    elif isinstance(obj, ClassDefItem):
        print "[XREFS] XREFS for class \"" + obj.get_name() + "\":\n"
        print_xref(d, obj)
    elif isinstance(obj, EncodedMethod):
        print "[XREFS] XREFS for method \"" + obj.get_name() + " \":\n"
        print_xref(d, obj)
    else:
        print "[ERROR] XREF non defined for objects of type " + type(obj)

def print_xref(d, obj):
    for xref in obj.XREFfrom.items:
        print show_Paths(d, xref[1])
