'''

## Unitary Operators
1. Pault Group Operators: X, Y, Z
2. General Phase Shift Operator: R, P, S, T
3. Hadamard Operator: H
4. Identity Operator: I

---
## Binary Operators
1. Controlled NOT Operator (CNOT)
2. Control Operator (CZ)
3. SWAP Operator (SWAP)

---
## Ternary Operator
1. Toffoli Operator (CCNOT)
2. Fredkin Operator (CSWAP)

'''


import qiskit
from qiskit.providers.aer import AerSimulator
from qiskit import QuantumCircuit
from math import pi

#Quantum NOT Operator [X]
def x():

    #prepare circuit
    qc = QuantumCircuit(1,1)
    qc.x(0)
    qc.measure(0,0)

    #simulaton & result
    result = AerSimulator().run(qc).result()

    print('\nresult: ',result.get_counts())
    return qc.draw(output='mpl')

#Quanutm [Y] Operator
def y():

    #prepare circuit
    qc = QuantumCircuit(1,1)
    qc.y(0)
    qc.measure(0,0)

    #simulaton & result
    result = AerSimulator().run(qc).result()

    print('\nresult: ',result.get_counts())
    return qc.draw(output='mpl')

#Quanutm [Z] Operator
def z():

    #prepare circuit
    qc = QuantumCircuit(1,1)
    qc.z(0)
    qc.measure(0,0)

    #simulaton & result
    result = AerSimulator().run(qc).result()

    print('\nresult: ',result.get_counts())
    return qc.draw(output='mpl')

#Quanutm [R] Operator
def r(phase):

    #prepare circuit
    qc = QuantumCircuit(1,1)
    qc.rz(phase, 0)
    qc.measure(0,0)

    #simulaton & result
    result = AerSimulator().run(qc).result()

    print('\nresult: ',result.get_counts())
    return qc.draw(output='mpl')

#Quanutm [P] Operator
def p(phase):

    #prepare circuit
    qc = QuantumCircuit(1,1)
    qc.p(phase,0)
    qc.measure(0,0)

    #simulaton & result
    result = AerSimulator().run(qc).result()

    print('\nresult: ',result.get_counts())
    return qc.draw(output='mpl')

#Quanutm [S] Operator: R-Gate with Phase = Pi/2
def s():

    #prepare circuit
    qc = QuantumCircuit(1,1)
    qc.s(0)
    qc.measure(0,0)

    #simulaton & result
    result = AerSimulator().run(qc).result()

    print('\nresult: ',result.get_counts())
    return qc.draw(output='mpl')

#Quanutm [T] Operator: R-Gate with Phase = Pi/4
def t():

    #prepare circuit
    qc = QuantumCircuit(1,1)
    qc.t(0)
    qc.measure(0,0)

    #simulaton & result
    result = AerSimulator().run(qc).result()

    print('\nresult: ',result.get_counts())
    return qc.draw(output='mpl')

#Quantum [H] Operator 
def h():

    #prepare circuit
    qc = QuantumCircuit(1,1)
    qc.h(0)
    qc.measure(0,0)

    #simulaton & result
    result = AerSimulator().run(qc).result()

    print('\nresult: ',result.get_counts())
    return qc.draw(output='mpl')

#Quantum [I] Operator 
def i():

    #prepare circuit
    qc = QuantumCircuit(1,1)
    qc.i(0)
    qc.measure(0,0)

    #simulaton & result
    result = AerSimulator().run(qc).result()

    print('\nresult: ',result.get_counts())
    return qc.draw(output='mpl')


#Controlled NOT [CNOT] Operator 
def cx(a, b):
    
    #preparing state-vectors
    a = [1,0] if a == 0 else [0,1]
    b = [1,0] if b == 0 else [0,1]
    #prepare circuit
    qc = QuantumCircuit(2,2)
    qc.initialize(a,0)
    qc.initialize(b,1)
    qc.cx(0,1)
    qc.measure(0,0)
    qc.measure(1,1)
    
    #simulaton & result
    result = AerSimulator().run(qc).result()

    print('\nresult: ',result.get_counts())
    return qc.draw(output='mpl')

#Control [CZ] Operator 
def cz(a, b):
    
    #preparing state-vectors
    a = [1,0] if a == 0 else [0,1]
    b = [1,0] if b == 0 else [0,1]
    
    #prepare circuit
    qc = QuantumCircuit(2,2)
    qc.initialize(a,0)
    qc.initialize(b,1)
    qc.cz(0,1)
    qc.measure(0,0)
    qc.measure(1,1)
    
    #simulaton & result
    result = AerSimulator().run(qc).result()

    print('\nresult: ',result.get_counts())
    return qc.draw(output='mpl')

#SWAP [SWAP] Operator 
def swap(a, b):
    
    #preparing state-vectors
    a = [1,0] if a == 0 else [0,1]
    b = [1,0] if b == 0 else [0,1]
    
    #prepare circuit
    qc = QuantumCircuit(2,2)
    qc.initialize(a,0)
    qc.initialize(b,1)
    qc.swap(0,1)
    qc.measure(0,0)
    qc.measure(1,1)
    
    #simulaton & result
    result = AerSimulator().run(qc).result()

    print('\nresult: ',result.get_counts())
    return qc.draw(output='mpl')

#Toffoli [CCNOT] Operator
def ccx(a, b):
    
    #preparing state-vectors
    a = [1,0] if a == 0 else [0,1]
    b = [1,0] if b == 0 else [0,1]
    
    #prepare circuit
    qc = QuantumCircuit(3, 3)
    qc.initialize(a, 0)
    qc.initialize(b, 1)
    qc.ccx(0, 1, 2)
    qc.measure(0, 0)
    qc.measure(1, 1)
    qc.measure(2, 2)
    
    #simulaton & result
    result = AerSimulator().run(qc).result()

    print('\nresult: ',result.get_counts())
    return qc.draw(output='mpl')

#Fredkin [CSWAP] Operator
def cswap(a, b, c):
    
    #preparing state-vectors
    a = [1,0] if a == 0 else [0,1]
    b = [1,0] if b == 0 else [0,1]
    c = [1,0] if c == 0 else [0,1]
    
    #prepare circuit
    qc = QuantumCircuit(3, 3)
    qc.initialize(a, 0)
    qc.initialize(b, 1)
    qc.initialize(c, 2)
    qc.cswap(0, 1, 2)
    qc.measure(0, 0)
    qc.measure(1, 1)
    qc.measure(2, 2)
    
    #simulaton & result
    result = AerSimulator().run(qc).result()

    print('\nresult: ',result.get_counts())
    return qc.draw(output='mpl')


    
