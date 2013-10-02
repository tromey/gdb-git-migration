# Compute the usermap from the file we have.

import re

_line_rx = re.compile('([^=]+)=(.*)$')

def user_mapping(filename):
    names = { }
    with open (filename) as f:
        for line in f:
            line = line.rstrip()
            matches = _line_rx.match(line)
            if matches is not None:
                names[matches.group(1)] = matches.group(2)
            else:
                print "not line %s" % line
    return names
