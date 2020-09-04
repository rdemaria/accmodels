import logging
logging.basicConfig(level=logging.INFO)

import accmodels

lhc=accmodels.lhc.get_model(source="scenarios/round/collision15.madx",
                           repository="/afs/cern.ch/eng/lhc/optics/HLLHCV1.5",
                           prefix="slhc")

lhc=accmodels.lhc.hllhc15.round.collision15()


lhc.lhcb1.show("")
