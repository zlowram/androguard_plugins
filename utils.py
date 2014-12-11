#!/usr/bin/env python

import string

def str_to_filename(ustr):
    safechars = '_' + string.digits + string.ascii_letters
    return "".join(x for x in ustr.replace("/","_") if x in safechars)
