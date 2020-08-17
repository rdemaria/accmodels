import accmodels

lhc=accmodels.LHC.from_path("/home/rdemaria/local/hllhc15")
lhc=accmodels.LHC.hllhc15.from_github()

mm=lhc.round15.collision.load()



