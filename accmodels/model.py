"""
A Model consists on set components that allow to compute optics functions. A specialized model contains additional highlevel methods for the machine.

The components of a model are:
- a lattice: sequence or line of elements
- an optics: list of variables definitions, expressions, knobs
- a beam
- a setting file: list of variable definitions.

A Collection is an indexed list of models. The index can be time for beam process or beta* or other indexes.

Workflow:

repo=accmodels.<machine>.<scenario>.from_github()
repo=accmodels.<machine>.from_path()

model=repo.<collection>.<model>()
model=repo.<model>()

Repository Examples

:collections.txt #lisf of scenarios files
round/round.txt
flatcc/flat.txt

:round/round.txt
<key> <path>
6     round/round6000.madx
0.15  round/round150.madx

models.txt
scenarios.txt

"""

from pathlib import Path
import tempfile
import shutil
import os

from pyoptics import optics

from .logger import logger


class Model:
    def __init__(self,source,repository,prefix):
        self.source=Path(source)
        self.repository=Path(repository)
        self.prefix=Path(prefix)

        self._tempdir=Path(tempfile.mkdtemp())
        os.symlink(repository,self._tempdir/prefix)
        logger.info(f"creating {self._tempdir}")

        self._stdout=open(self._tempdir/"mad.log","a+")
        self.reload()

    def __del__(self):
        logger.info(f"removing {self._tempdir}")
        self.mad.exit()
        self._stdout.close()
        shutil.rmtree(self._tempdir)

    def reload(self):
        from cpymad.madx import Madx
        self.mad=Madx(stdout=self._stdout, stderr=self._stdout,)
        self.mad.chdir(str(self._tempdir))
        source=str(self.prefix/self.source)
        logger.info(f"loading {source}")
        self.mad.call(source)


    def mad_log(self):
        self._stdout.seek(0)
        print(self._stdout.read())


twiss_cols=[
"betx", "alfx", "mux",
"bety", "alfy", "muy",
"x", "px", "y", "py", "t", "pt",
"dx", "dpx", "dy", "dpy",
"wx", "phix", "dmux", "wy", "phiy", "dmuy",
"ddx", "ddpx", "ddy", "ddpy",
"r11", "r12", "r21", "r22",
"energy"]



class Selection:
    def __init__(self,sequence,twiss,start=None,end=None,):
        self.sequence=sequence
        self.start=start
        self.end=end
        self.mad=None

    def twiss(self):
        if self.start is None:
            return self.mad.twiss()


class Point:
    def __init__(self,sequence,element):
        self.sequence=sequence
        self.element=element
        self.twiss_data={}















