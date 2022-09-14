
#importing modules from Qiskit library
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, BasicAer, execute

def TruelyRandomByte():
    #initializing quantum register
    q = QuantumRegister(8)
    #initializing classical register
    c = ClassicalRegister(8)

    #initializing quantum circuit
    circuit = QuantumCircuit(q, c)
    
    #applying H-Gate to qubits
    for i in range(8):
        circuit.h(q[i])
    
    #measuring qubit values
    circuit.measure(q, c) 
    
    #creating backend for simulation
    b = BasicAer.get_backend('qasm_simulator')
    #executing circuit on backend
    j = execute(circuit, b, shots = 1)
    #calculating result
    result = j.result()

    #listing all results
    ls = result.get_counts().keys()
    #returning result in decimal form
    for i in ls:
        return int(i,2) 
    
for i in range(10):
    print(TruelyRandomByte())