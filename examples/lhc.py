import accmodels

import logging
logging.basicConfig(level=logging.INFO)


lhc=accmodels.lhc.get_model(source="scenarios/round/collision15.madx",
                           repository="/afs/cern.ch/eng/lhc/optics/HLLHCV1.5",
                           prefix="slhc")



