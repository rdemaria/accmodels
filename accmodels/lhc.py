from .repository import Machine, GitRepo

from .model import Model

class LHCModel(Model):
    """ additional code specific for LHC models
    """

lhc=Machine("lhc",LHCModel)

lhc.hllhc15=GitRepo("hllhc15",url="https://github.com/lhcopt/hllhc15.git",prefix="slhc",model=LHCModel)



