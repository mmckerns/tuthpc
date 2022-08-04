#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 2016-2022 Mike McKerns.
# License: 3-clause BSD.

import os
notebookdir = os.environ.get('NOTEBOOKDIR', '.')
os.environ['PYTHONPATH'] = ':'.join([
                            os.environ['PYTHONPATH'],
                            '.:/Users/mmckerns/lib/python2.7/site-packages',
                            notebookdir])
os.environ['DYLD_LIBRARY_PATH'] = ':'.join([
                            os.environ['DYLD_LIBRARY_PATH'],"."])
os.system("alias python='python2.7'")
os.chdir(os.path.abspath(notebookdir))

print ("loaded user env")
# EOF
