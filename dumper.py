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

def dump_rich(d, filename):
    if os.path.exists(filename):
        raise Exception("File exists")
    print "Dumping " + filename
    f = open(filename, "w")
    for c in d.get_classes():
        f.write("//"+"-"*70+"\n")
        f.write("// Class: "+c.get_name()+"\n")

        for m in c.get_methods():
            f.write("\n")
            if m.code: f.write(get_params_info(m.code.get_registers_size(), m.get_descriptor()))
            f.write(get_xrefs(m))
            f.write(m.get_source())
    f.close()

def get_xrefs(m):
    buf = ""
    if len(m.XREFfrom.items) > 0:
        buf += "// XREFs from:\n"
        for xf in m.XREFfrom.items:
            buf += "//   %s %s %s %s\n" % (xf[0].get_class_name(), xf[0].get_name(),
                xf[0].get_descriptor(), ' '.join("%x" % j.get_idx() for j in xf[1]))
    if len(m.XREFto.items) > 0:
        buf += "// XREFs to:\n"
        for xt in m.XREFto.items:
            buf += "//   %s %s %s %s\n" % (xt[0].get_class_name(), xt[0].get_name(),
                xt[0].get_descriptor(), ' '.join("%x" % j.get_idx() for j in xt[1]))
    return buf

def get_params_info(nb, proto):
    buf = "// Parameters:\n"
    ret = proto.split(')')
    params = ret[0][1:].split()
    if params:
        buf += "//  - local registers: v%d...v%d\n" % (0, nb - len(params) - 1)
        j = 0
        for i in xrange(nb - len(params), nb):
            buf += "//  - v%d:%s\n" % (i, get_type(params[j]))
            j += 1
    else:
        buf += "//  - local registers: v%d...v%d\n" % (0, nb - 1)
    buf += "//  - return:%s\n" % get_type(ret[1])
    return buf

TYPE_DESCRIPTOR = {
    'V': 'void',
    'Z': 'boolean',
    'B': 'byte',
    'S': 'short',
    'C': 'char',
    'I': 'int',
    'J': 'long',
    'F': 'float',
    'D': 'double',
}

def get_type(atype, size=None):
    if atype.startswith('java.lang'):
        atype = atype.replace('java.lang.', '')
    res = TYPE_DESCRIPTOR.get(atype.lstrip('java.lang'))
    if res is None:
        if atype[0] == 'L':
            res = atype[1:-1].replace('/', '.')
        elif atype[0] == '[':
            if size is None:
                res = '%s[]' % get_type(atype[1:])
            else:
                res = '%s[%s]' % (get_type(atype[1:]), size)
        else:
            res = atype
    return res
