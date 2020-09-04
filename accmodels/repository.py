"""
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
import shutil
import os
import site

from .logger import logger

class Machine:
    def __init__(self,name,model):
        self.name=name
        self.model=model

    def get_model(self,source,repository,prefix):
        return self.model(source,repository,prefix)


class GitRepo:
    def __init__(self,name,url,branch=None,tag=None,prefix='slhc',model=None):
        self.name=name
        self.url=url
        self.branch=branch
        self.tag=tag
        self.prefix=prefix
        self.model=model
        self.base=Path(site.getuserbase())/'share'/'accmodels'
        self.base.mkdir(parents=True, exist_ok=True)
        self.clonepath=self.base/self.name
        self.checkout()
        self.populate()

    def checkout(self):
        if self.clonepath.is_dir():
            if self.tag is None:
                logger.info(f"pulling {self.clonepath}")
                os.system(f"cd {self.clonepath}; git pull")
        else:
            logger.info(f"cloning {self.url} into {self.clonepath}")
            if self.branch is not None:
               os.system(f"cd {self.base}; git clone -b {self.branch} {self.url} {self.name}")
            elif self.branch is not None:
               os.system(f"cd {self.base}; git clone -b {self.branch} {self.url} {self.name}")
            else:
               os.system(f"cd {self.base}; git clone {self.url} {self.name}")

    def populate(self):
        ### implement metadata alternative to self discovery
        scenarios=self.clonepath/'scenarios'
        for pp in scenarios.iterdir():
            setattr(self,pp.stem,Collection(name=pp.stem,
                                       path=pp,
                                       repository=self.clonepath,
                                       prefix=self.prefix,
                                       model=self.model))

class Collection:
    def __init__(self,name,path,repository,prefix,model=None,models=None):
        self.name=name
        self.path=path
        self.repository=repository
        self.prefix=prefix
        self.model=model
        if models is None:
            self.models=[]
            for pp in path.iterdir():
                self.models.append(pp.stem)
                setattr(self,pp.stem,ModelLoader(pp,self.repository,self.prefix,self.model))

class ModelLoader:
    def __init__(self,source,repository,prefix,model):
        self.source=source
        self.repository=repository
        self.prefix=prefix
        self.model=model

    def __call__(self):
        return self.model(self.source,self.repository,self.prefix)

