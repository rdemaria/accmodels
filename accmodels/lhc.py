from .repository import Machine, GitRepo

from .model import Model

class LHCModel(Model):
    """ additional code specific for LHC models
    """
    def _get_arcs_indexes(self):
        return ((i%8+1,(i+1)%8+1) for i in range(8))

    def _get_arcds_boundaries(self,beam=1):
        for a,b in self._get_arcs_indexes():
            yield f"s.ds.r{a}.b{beam}",f"e.ds.l{b}.b{beam}"

    def _get_arc_boundaries(self,beam=1):
        for a,b in self._get_arcs_indexes():
            yield f"e.ds.r{a}.b{beam}",f"s.ds.l{b}.b{beam}"

    def _get_ir_boundaries(self,beam=1):
        for a,b in self._get_arcs_indexes():
            yield f"s.ds.l{a}.b{beam}",f"e.ds.r{b}.b{beam}"

    def _get_lss_boundaries(self,beam=1):
        for a,b in self._get_arcs_indexes():
            yield f"e.ds.l{a}.b{beam}",f"s.ds.r{b}.b{beam}"






lhc=Machine("lhc",LHCModel)

lhc.hllhc15=GitRepo("hllhc15",url="https://github.com/lhcopt/hllhc15.git",prefix="slhc",model=LHCModel)



