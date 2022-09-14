from qulib import Operators as op
op.x()
op.h()
op.cx(1, 0)
op.swap(1, 1)
op.cswap(1, 1, 0)


from qulib import QuantumTeleportation as qt
qt.QuantumTeleportation()


from qulib import SuperdenseCoding as sc
sc.SuperdenseCoding()


from qulib import GroverSearch as gs
gs.ClassicalSearch()
gs.GroverSearch()


from qulib import TruelyRandomByte as trb
for i in range(10):
    print(trb.TruelyRandomByte(), end = ' ')


from qulib import QuantumWalk as qw
qw.QuantumWalk()
