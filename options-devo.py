# options file for devo.

import os
import inspect

# Sigh.
__mydir = os.path.dirname(os.path.abspath(inspect.getsourcefile(lambda _: None)))

WANT_JUST_SOME_BRANCHES = 1

execfile(os.path.join(__mydir, 'cvs2git-example.options'))
