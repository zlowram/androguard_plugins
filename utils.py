#!/usr/bin/env python

# Copyright 2015 The plugins Authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import string

def str_to_filename(ustr):
    safechars = '_' + string.digits + string.ascii_letters
    return "".join(x for x in ustr.replace("/","_") if x in safechars)
