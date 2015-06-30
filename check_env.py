#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 2015 California Institute of Technology.
# License: 3-clause BSD.
"""
check environment scipt
"""
import sys

# requirements
has = dict(
    # parallel programming
    line_profiler='0.0.0',
    dill='0.2.4',
    # parallel computing
    mpi4py='0.0.0',
    pathos='0.0.0',
    cython='0.0.0',
    # dependencies
    pox='0.0.0',
    multiprocess='0.0.0',
    ppft='0.0.0',
    # examples
    numpy='0.0.0',
    # optional
    IPython='0.0.0',
    paramiko='0.0.0',
    pyina='0.0.0',
    objgraph='0.0.0',
)


# executables
run = dict(
    # parallel programming
    line_profiler=('lineprofiler.py','kernprof.py',),
    dill=('get_objgraph.py',),
    # parallel computing
    mpi4py=['mpiexec','mpirun','mpiexec-mpich-mp','mpiexec-openmpi-mp','mpirun-mpich-mp','mpirun-openmpi-mp'],
   #pathos=('pathos_tunnel.py','pathos_server.py','tunneled_pathos_server.py',),
    # dependencies
    ppft=('ppserver.py',),
    # examples
    # optional
   #IPython=('ipython*','ipcluster',),
   #paramiko=('ssh','scp',),
   #pyina=('sync','cp','rm','ezpool.py','ezscatter.py',),
)


returns = 0

# check installed packages
for module in has.keys():
    try:
        __module__ = __import__(module, globals(), locals(), [], 0)
        exec('%s = __module__' % module)
    except ImportError:
        print("%s:: %s" % (module, sys.exc_info()[1]))
        returns += 1


# check required versions
from distutils.version import LooseVersion as V
for module,version in has.items():
    try:
        assert V(eval(module).__version__) >= V(version)
    except NameError:
        pass # failed import
    except AttributeError:
        pass # can't version-check non-standard packages...
    except AssertionError:
        print("%s:: Version >= %s is required" % (module, version))
        returns += 1


# check required executables
try:
    from pox import which
   #from subprocess import Popen, STDOUT, PIPE#, call
except ImportError:
    sys.exit(returns)
for module,executables in run.items():
    for prog in reversed(executables):
        try:
            assert which(prog)
#           process = Popen([prog, '--help'], stderr=STDOUT, stdout=PIPE)
#           process.wait()
            if isinstance(executables, list): break  # just requires one
        except (OSError, AssertionError):
            if isinstance(executables, list) and \
               prog != executables[0]: pass
            from sys import exc_info
            print("%s:: Executable '%s' not found" % (module, prog))
           #print("%s:: %s" % (prog, exc_info()[1]))
            returns += 1


# final report
if not returns:
    print('\nOK.')

sys.exit(returns)


