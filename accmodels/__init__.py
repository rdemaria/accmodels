"""
A Model instance represent a fixed configuration of a machine and the class implements specialized actions to modify or query the model.


A Machine builds specialied models
- building from a path
- building from a repositories




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
scenarios
"""




__version__= '0.0.0'

import logging
logger=logging.getLogger("accmodel")

from .lhc import lhc

