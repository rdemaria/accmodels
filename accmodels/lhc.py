from .accelerator import Accelerator, Repository, Collection


class LHCModel(Model):
    """ additional code specific for LHC models
    """

LHC=Accelerator("LHC",LHCModel)

LHC.add(Repository(
    "hllhc15",
    github="lhcopt/hllhc15.git")


