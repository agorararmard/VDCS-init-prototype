from Server import Server
from Client import Client

def AND(a, b):
    return a&b

C = Client(32)
m = C.intiate_Process(AND, [1, 1], 4)
S1 = Server()
S1.receiveC(m)
S1.garble()
S2 = Server()
S2.receiveS(m,S1.getCircuit())
S2.reRand()
S3 = Server()
S3.receiveS(m,S2.getCircuit())
S3.reRand()
S4 = Server()
S4.receiveS(m,S3.getCircuit())
z = S4.eval()
print(C.result(z))
