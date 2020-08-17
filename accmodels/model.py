"""
A Machine:
- allows to locate a set of repositories using SourceSets or loading from a path
- defines a specialized model generator

A repositories contains a Collections of Models or Models using metadata and data contained in the repository.

A Model consists on set components that allow to compute optics functions. A specialized model contains additional highlevel methods and features for the machine.

The components are:
- a lattice: sequence or line of elements
- an optics: list of values, expressions, knobs
- a beam


Workflow:

repo=accmodels.<machine>.<scenario>.from_github()
repo=accmodels.<machine>.from_path()

model=repo.<collection>.<model>()
model=repo.<model>()


Repository Examples

:scenarios.txt #lisf of scenarios files
round/round.txt
flatcc/flat.txt

:round/round.txt
<key> <path>
6     round/round6000.madx
0.15  round/round150.madx

models.txt
scenarios.txt



name path





"""

from pathlib import Path

class Machine:
    def __init__(self,name,model_generator):
        self.name=name
        self.repositories={}
        self.model_generator=model_generator

    def add_repository(self,name,github=None, afs=None):
        repo=Repository(name,github=github,afs=afs)
        self.repositories[name]=repo

    def __getattr__(self,name):
        return self.repositories[name]

    def __getitem__(self,name):
        return self.repositories[name]

    def from_path(self,path):
        return Repository(PathSource(path))

class PathSource:
    def __init__(self,path):
        self.path=Path(path)
    def read_file(self,path):
        return open(self.path/path).read()

class SourceList:
""" Correspond to a repository
"""
def __init__(self,
        source):
        gitlab=None,
        afs=None,
        eos=None,
        source=None):

    self.github=github
    self.afs=afs
    self.source=source







