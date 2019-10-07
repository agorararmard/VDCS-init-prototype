from circuit import circuit
from message import message
class Server:
    IDs = 0                             #for keeping track of object ids, alt: use id() func

    def __init__(self):                 #constructor: assigns ID to obj
        self.ID = (Server.IDs)
        Server.IDs += 1


    def getID(self):                    #get ID of obj
        return self.ID

    def receiveC(self, m):#, R2):       #Receive a boolean expression from user
        self.Circuit, self.R,  x, y = m[self.ID].extract()

    def receiveS(self,m, GC):#, R2):      #Receive a Garbled Circuit from server
        self.GC = GC
        self.Circuit, self.R,  self.winx, self.winy = m[self.ID].extract()
        #self.R2 = R2

    def garble(self):                   #Garbling F to GC(1)
        #self.GC = self.Circuit
        self.Circuit.YaoGarbledCkt(self.R[0], self.R[1], self.R[2])
        return self.Circuit

    def eval(self):              #Evaluating GC(i) on inWire
        return self.GC.eval(self.winx, self.winy)

    def reRand(self):                   #reRanding GC(i-1) to GC(i)// for now it's doing the same as garble.
        self.Circuit.reRand(self.R)
        return self.Circuit

    def getGC(self):                    #returning GC(i)
        return self.GC

    def getCircuit(self):               #returning input Circuit
        return self.Circuit
