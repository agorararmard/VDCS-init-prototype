import circuit
class Server:
    IDs = 0                             #for keeping track of object ids, alt: use id() func

    def __init__(self):                 #constructor: assigns ID to obj
        self.ID = (Server.IDs)
        Server.IDs += 1


    def getID(self):                    #get ID of obj
        return self.ID

    def receiveC(self, F,cid, R1):#, R2):       #Receive a boolean expression from user
        self.Circuit = circuit(F,cid)       #F is the single bit function, cid is the computation ID
        self.F = F
        self.R1 = R1
        #self.R2 = R2

    def receiveS(self, GC,cid, R1):#, R2):      #Receive a Garbled Circuit from server
        self.GC = GC
        self.R1 = R1
        #self.R2 = R2

    def garble(self):                   #Garbling F to GC(1)
        self.GC = self.Circuit
        self.GC.YaoGarbledCkt(self.R1[self.ID][0], self.R1[self.ID][1], self.R1[self.ID][2])
        return self.GC

    def eval(self,inWire):              #Evaluating GC(i) on inWire
        return self.GC.eval(inWire), self.GC.getOutWires()

    def reRand(self):                   #reRanding GC(i-1) to GC(i)// for now it's doing the same as garble.
        self.GC = self.Circuit
        self.GC.YaoGarbledCkt(self.R1[self.ID][0], self.R1[self.ID][1], self.R1[self.ID][2])
        return self.GC

    def getGC(self):                    #returning GC(i)
        return self.GC

    def getCircuit(self):               #returning input Circuit
        return self.Circuit