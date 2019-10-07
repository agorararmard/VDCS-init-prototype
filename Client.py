from Crypto import Random
from Crypto.PublicKey import RSA
import base64
import numpy as np
import random
from circuit import circuit
from message import message

class Client:
    #the constructor is initializing the public and the private keys/ the random seeds
    def __init__(self,size):
        self.SeedSize = size

        #self.R2 = randint(pow(10, self.SeedSize - 1) + 1, pow(10, self.SeedSize) - 1)
    
    
    def intiate_Process(self,F, win, servers):
    #this function will send the (public_Key, R1, R2, Function) to the servers
        self.F = F
        self.R =[[0]*3]*servers
        cid = id(self.F)
        m = [0]*servers

        circ = circuit(self.F, cid)

        for i in range(servers):
            self.R[i][0] = (random.getrandbits(self.SeedSize))
            self.R[i][1] = random.getrandbits(self.SeedSize)
            self.R[i][2] = random.getrandbits(self.SeedSize)

        inwires = circ.YaoGarbledCkt_in(self.R[servers-1][0])
        winx, winy = inwires[0+win[0]], inwires[2+win[1]]
        self.outwires = circ.YaoGarbledCkt_out(self.R[servers-1][1])

        for i in range(servers-1):
            m[i]=message(circ, self.R[i])
        m[servers-1] = message(circ, self.R[servers-2], winx, winy)

        return m



    #this function to be called after recieving the results
    #def Decode_Verify(output = []):
    #    result = np.array([])
    #    if np.array_equal(output, outputWires):     #check for the labels first if they are equal
    #        for text in output:
    #            result.append(self.decryptt(text))
    #    return result        
    

    def result(self, z):
        if z == self.outwires[0]:
            return 0
        elif z == self.outwires[1]:
            return 1
        else:
            return None
