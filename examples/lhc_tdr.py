import numpy as np

import accmodels
from pyoptics import optics

def print_tdr(lhc):
    lhc.mad.use("lhcb1")
    tw1=optics(lhc.mad.twiss())
    lhc.mad.use("lhcb2")
    tw2=optics(lhc.mad.twiss())

    for ll in ['dx','dy','betx','bety']:
        sel1=lhc._get_arc_boundaries(beam=1)
        sel2=lhc._get_arc_boundaries(beam=2)
        v1max= np.max([ tw1.select(a,b)[ll].max() for (a,b) in sel1])
        v2max= np.max([ tw2.select(a,b)[ll].max() for (a,b) in sel2])
        sel1=lhc._get_arc_boundaries(beam=1)
        sel2=lhc._get_arc_boundaries(beam=2)
        v1min= np.min([ tw1.select(a,b)[ll].min() for (a,b) in sel1])
        v2min= np.min([ tw2.select(a,b)[ll].min() for (a,b) in sel2])
        print(f"{ll:6} {max(v1max,v2max):8.2f} {min(v1min,v2min):8.2f} ")

    for ip in ['ip1','ip2','ip5','ip8']:
        ss1=tw1//ip
        ss2=tw2//ip
        print(f"{ip}")
        for ll,ff in [('px',1e6),('py',1e6),('x',1e3),('y',1e3)]:
            print(f"{tw1[ll][ss1][0]*ff:8.3f} {tw2[ll][ss2][0]*ff:8.3f}")
        print()


    for ll,ff in [('q1',1),('q2',1),('dq1',1),('dq2',1)]:
       print(f"{tw1.param[ll]*ff:8.3f} {tw2.param[ll]*ff:8.3f}")

    alfa1=tw1.param['alfa']
    alfa2=tw2.param['alfa']
    gamma1=tw1.param['gamma']
    gamma2=tw2.param['gamma']
    gammatr1=tw1.param['gammatr']
    gammatr2=tw2.param['gammatr']
    eta1=alfa1-1/gamma1**2
    eta2=alfa2-1/gamma2**2
    print(eta1,alfa1)

    print(f"{alfa1*1e4:8.3f} {alfa2*1e4:8.3f}")
    print(f"{eta1*1e4:8.3f} {eta2*1e4:8.3f}")
    print(f"{gammatr1:8.3f} {gammatr2:8.3f}")


    return tw1,tw2


accmodels.lhc.hllhc15.checkout()

lhc=accmodels.lhc.hllhc15.round.injection6000()
tw1,tw2=print_tdr(lhc)

lhc=accmodels.lhc.hllhc15.round.collision150()
tw1,tw2=print_tdr(lhc)

