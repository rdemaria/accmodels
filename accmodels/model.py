"""
A Machine:
- allows to locate a set of repositories using SourceSets or loading from a path
- defines a specialized model generator

A repositories contains a set of Models or Collections of Models using metadata and data contained in the repository.

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
import site

import logging

logger=logging.getLogger("accmodel")



class Machine:
    def __init__(self,name,model):
        self.name=name
        self.model=model

    def get_model(self,source,repository,prefix):
        return self.model(source,repository,prefix)


class GitRepo:
    def __init__(self,name,url,branch=None,tag=None):
        self.url=url
        self.branch=branch
        self.tag=tag
        self.checkout()
        self.base=Path(site.getuserbase())/'share'/'accmodels'
        self.base.mkdir(parents=True, exist_ok=True)
        self.dirname=self.base/self.name

    def checkout(self):
        if self.dirname.is_dir():
            if self.tag is None:
                os.system(f"cd {self.dirname}; git pull")
        else:
            if self.tag is None:
               os.system(f"cd {self.base}; git clone -b {self.tag} {self.url} {self.name}")
            else:
               os.system(f"cd {self.base}; git clone -b {self.branch} {self.url} {self.name}")

    def populate(self):
        pass


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
        logger.info(f"removing {self.dtemp}")
        self.mad.exit()
        self._stdout.close()
        shutil.rmtree(self.dtemp)

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













