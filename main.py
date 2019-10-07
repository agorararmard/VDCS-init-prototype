import Server
import Client

def AND(a, b):
    return a&b

C = Client(10)
m = C.intiate_Process(AND, 4)
S1 = Server()
S1.receiveC(m)
S1.garble()
S2 = Server()
S2.receiveS(m,S1.getGC())
S2.reRand()
S3 = Server()
S3.receiveS(m,S2.getGC())
S3.reRand()
S4 = Server()
S4.receiveS(m,S3.getGC())
#S4.eval()
