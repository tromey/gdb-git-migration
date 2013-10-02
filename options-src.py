# options file for src.

import os
import inspect

# Sigh.
__mydir = os.path.dirname(os.path.abspath(inspect.getsourcefile(lambda _: None)))

WANT_JUST_SOME_BRANCHES = 0

execfile(os.path.join(__mydir, 'cvs2git-example.options'))
