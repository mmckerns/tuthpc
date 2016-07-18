Efficient Python for High-Performance Parallel Computing
==========================================================

This tutorial is targeted at the intermediate-to-advanced Python user who
wants to extend Python into High-Performance Computing. The tutorial will
provide hands-on examples and essential performance tips every developer
should know for writing effective parallel Python. The result will be a clear
sense of possibilities and best practices using Python in HPC environments.

Many of the examples you often find on parallel Python focus on the mechanics
of getting the parallel infrastructure working with your code, and not on
actually building good portable parallel Python. This tutorial is intended to
be a broad introduction to writing high-performance parallel Python that is
well suited to both the beginner and the veteran developer. Parallel efficiency
starts with the speed of the target code itself, so we will start with how to
evolve code from for-loops to Python looping constructs and vector programming.
We will also discuss tools and techniques to optimize your code for speed and
memory performance.

The tutorial will overview working with the common parallel
communication technologies (threading, multiprocessing, MPI) and introduce the
use of parallel programming models such as blocking and non-blocking pipes,
asynchronous and iterative conditional maps, and map-reduce. We will discuss
strategies for extending parallel workflow to utilize hierarchical and
heterogeneous computing, distributed parallel computing, and job schedulers.
We then return our focus to the speeding up our target code by leveraging
parallelism within compiled code using Cython.

At the end of the tutorial,
participants should be able to write simple parallel Python scripts, make use
of effective parallel programming techniques, and have a framework in place to
leverage the power of Python in High-Performance Computing.



Content
---------

All tutorial content can be obtained from this repository either with
`git, or by downloading the repository content as a zip file.  If you use
git, you can clone this repostory with::

    $ git clone https://github.com/mmckerns/tuthpc.git


or, download and unzip the zipfile.

As the day of the tutorial get nearer, it is highly recommended to update
this repository.  When tutorial content is added or modified, it is
recommended to update your copy of the tutorial.  Tutorial content may be
updated up to the day of the tutorial, during the tutorial, and beyond.
To update your copy of the tutorial content with git, change to the tutorial
directory (i.e. `tuthpc`), then pull an update with::

    $ git pull


or, download and unzip a new copy of the zipfile.



Requirements
--------------

To be able to run the examples, demos, and exercises in this tutorial,
the following packages must be installed::

    numpy >= 1.0,
    flake8 >= 2.0,
    line_profiler >= 1.0,
    nose >= 1.3.1,
    cython >= 0.22,
    mpi4py >= 2.0.0,
    pox >= 0.2.2,
    dill >= 0.2.5,
    multiprocess >= 0.70.4,
    ppft >= 1.6.4.5,
    pathos >= 0.2.0,
    llvmlite >= 0.2.2,
    numba >= 0.17.0,


and optionally::

    IPython >= 3.0.0,
    paramiko >= 1.15.2,
    pyina >= 0.2a1.dev0



Installation
--------------

All packages can be installed with `pip`::

    >$ pip install setuptools
    >$ pip install numpy
    >$ pip install flake8
    >$ pip install line_profiler
    >$ pip install nose
    >$ pip install cython
    >$ pip install pathos
    >$ pip install mpi4py
    >$ pip install llvmlite
    >$ pip install numba


and optionally::

    >$ pip install "ipython[parallel]"
    >$ pip install paramiko
    >$ pip install git+https://github.com/uqfoundation/pyina.git@master


The install of `numpy` and `llvmlite` can fail.  A more stable choice for
installing these two packages is to use a scientific python distribution
such as `canopy` or `anaconda`.


Note that on windows, `mpi4py` is known to be a difficult install, and
commonly fails with `pip` (or `conda`, etc).  You may be able to get a
compatible wheel at either of these two locations::

    http://www.lfd.uci.edu/~gohlke/pythonlibs
    https://ci.appveyor.com/api/buildjobs/38i20k6b1r4xn65q/artifacts/


The optional install for `ipython-parallel` also can be difficult, and
commonly fails with `pip` (or `conda`, etc).  Compatible wheels may be
available at this location::

    http://www.lfd.uci.edu/~gohlke/pythonlibs


The optional install for `pyina` is not supported on Windows.


The following steps were used by the tutorial author to test on Windows:

    # installed Visual Studio Community 2015 RC
    # installed Python Tools 2.2 RC for Visual Studio 2015
    # installed Microsoft Visual C++ Compiler for Python 2.7
    # installed Miniconda 3.10.1 (64-bit) for Python 2.7
    # installed Git for Windows 1.9.5-preview20150319 (including cmd tools)
    # installed Microsoft MPI v6
    >$ conda install pip
    >$ conda install setuptools
    >$ conda install flake8
    >$ conda install line_profiler
    >$ conda install nose
    >$ conda install numpy
    >$ conda install cython
    # get https://github.com/uqfoundation/pox/blob/master/tools/pythonstartup
    # save as ~\.python (also add as PYTHONSTARTUP to environment variables)
    # associate .py file with conda's python.exe
    # fix bug where conda doesn't respect all `sys.argv`
    #   regedit HKEY_CLASSES_ROOT\Applications\python27.exe\shell\open\command
    #   regedit HKEY_CLASSES_ROOT\py_auto_file\shell\open\command
    >$ pip install pathos
    >$ pip install https://ci.appveyor.com/api/buildjobs/38i20k6b1r4xn65q/artifacts/dist/mpi4py-2.0.0a0-cp27-none-win_amd64.whl
    >$ conda install numba



Verification
--------------

To test your installation, change to the tutorial directory, and run::

    >$ python check_env.py
    OK.  All required items installed.


If you choose not install all optional dependencies, you will see a warning::

    >$ python check_env.py 
    pyina:: No module named pyina
    OK.  All required intems installed.


Feel free to ignore warnings for optional dependencies.

