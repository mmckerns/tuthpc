#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 2015-2016 California Institute of Technology.
# Copyright (c) 2016-2019 Mike McKerns.
# License: 3-clause BSD.
"""
check environment scipt
"""
import sys

# requirements
has = dict(
    # parallel programming
    numpy='1.0',
    flake8='2.0',
    line_profiler='1.0',
    nose='1.3.1',
    dill='0.2.5',
    # parallel computing
    mpi4py='2.0.0',
    pathos='0.2.0',
    cython='0.22',
    llvmlite='0.2.2',
    numba='0.17.0',
    # dependencies
    pox='0.2.2',
    multiprocess='0.70.4',
    ppft='1.6.4.5',
    # optional
    IPython='3.0.0',
    pyina='0.2.0.dev0',
   #numexpr='2.4',
    paramiko='1.15.2',
   #objgraph='1.7.2',
   #guppy='0.1.10',
   #pympler='0.4.1',
   #scoop='???',
   #MPI_import='???',
)


# executables
#  list: At least one item is expected
#  tuple: All items are expected
run = dict(
    # parallel programming
    flake8=['flake8','flake8-2.7'],
    line_profiler=('kernprof',),
    nose=['nosetests','nosetests-2.7'],
   #dill=('get_objgraph.py',),
    # parallel computing
    mpi4py=['mpiexec','mpirun','mpiexec-mpich-mp','mpiexec-openmpi-mp','mpirun-mpich-mp','mpirun-openmpi-mp'],
    pathos=('pathos_tunnel.py','pathos_server.py','tunneled_pathos_server.py',),
    # dependencies
    ppft=('ppserver.py',),
    # optional
    IPython=['ipcluster','ipcluster-2.7','ipcluster2-2.7'],
    pyina=('sync','cp','rm','ezpool.py','ezscatter.py',),
    paramiko=('ssh','scp',),
)


returns = 0

# check installed packages
for module in has.keys():
    try:
        __module__ = __import__(module, globals(), locals(), [], 0)
        exec('%s = __module__' % module)
    except ImportError:
        print("%s:: %s" % (module, sys.exc_info()[1]))
        run.pop(module, None)
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

def executable_exist(module, prog):
    try:
        assert which(prog)
#           process = Popen([prog, '--help'], stderr=STDOUT, stdout=PIPE)
#           process.wait()
        return True
    except (OSError, AssertionError):
        from sys import exc_info
        print("%s:: Executable '%s' not found" % (module, prog))
        #print("%s:: %s" % (prog, exc_info()[1]))
        return False

# check required executables
try:
    from pox import which
   #from subprocess import Popen, STDOUT, PIPE#, call
except ImportError:
    sys.exit(returns)
for module,executables in run.items():
    if isinstance(executables, list):
        found = False
        for executable in executables:
            if executable_exist(module, executable):
                found = True
                break
        if not found:
            returns += 1
    else:
        for executable in executables:
             if not executable_exist(module, executable):
                 returns += 1

# final report
if not returns:
    print('-'*50)
    print('OK.  All required items installed.')

sys.exit(returns)


