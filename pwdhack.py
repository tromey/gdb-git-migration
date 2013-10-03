# read sware-passwd file and missed-users and
# compute a user map.

import sys

passwdmap = {}
with open('sware-passwd') as f:
    for line in f:
        line = line.rstrip()
        vec = line.split(':')
        passwdmap[vec[0]] = vec[4]

with open('missed-users') as f:
    for line in f:
        line = line.rstrip()
        if line not in passwdmap:
            print line
            sys.exit(1)
        print '%s=%s <%s@sourceware.org>' % (line, passwdmap[line], line)
