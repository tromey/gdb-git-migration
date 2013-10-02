# Merge the USERS file into the combined Meyering-style user-map.
# See README.md.

import re

_line_rx = re.compile('([^=]+)=(.*)$')


def user_mapping(filename):
    names = {}
    with open (filename) as f:
        for line in f:
            line = line.rstrip()
            matches = _line_rx.match(line)
            if matches is not None:
                names[matches.group(1)] = matches.group(2)
            else:
                print "not line %s" % line
    return names

mapping = user_mapping('combined-meyering-user-map')

with open('../iant-unpacked/USERS') as f:
    for line in f:
        line = line.rstrip()
        if line in mapping:
            mapping[line] = 'FIXME <%s@cygnus>' % line

for i in sorted(mapping.items()):
    print '%s=%s' % i
