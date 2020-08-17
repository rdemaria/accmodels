from .model import Machine, Model

class LHCModel(Model):
    """ additional code specific for LHC models
    """

lhc=Machine("lhc",LHCModel)

lhc.hllhc15=GitRepo("https://github.com/lhcopt/hllhc15.git", "master")




