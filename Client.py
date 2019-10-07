from Crypto import Random
from Crypto.PublicKey import RSA
import base64
import numpy as np
from random import randint
import message

class Client:
    #the constructor is initializing the public and the private keys/ the random seeds
    def __init__(self,size):
        self.SeedSize = size

        #self.R2 = randint(pow(10, self.SeedSize - 1) + 1, pow(10, self.SeedSize) - 1)
    
    
    def intiate_Process(self,F,n):
    #this function will send the (public_Key, R1, R2, Function) to the servers
        self.F = F
        self.R1 =[[]]
        cid = id(self.F)
        m = []
        for i in range(n):
            self.R1[i][0] = randint(pow(10, self.SeedSize - 1) + 1, pow(10, self.SeedSize) - 1)
            self.R1[i][1] = randint(pow(10, self.SeedSize - 1) + 1, pow(10, self.SeedSize) - 1)
            self.R1[i][2] = randint(pow(10, self.SeedSize - 1) + 1, pow(10, self.SeedSize) - 1)
        for i in range(n):
            m[i]=message(self.F,cid,self.R1[i])

        return m



    #this function to be called after recieving the results
    #def Decode_Verify(output = []):
    #    result = np.array([])
    #    if np.array_equal(output, outputWires):     #check for the labels first if they are equal
    #        for text in output:
    #            result.append(self.decryptt(text))
    #    return result        
    

    def Recieve(self, result):
        #calling the verify
        #Decode_Verify(result)
        pass
    

