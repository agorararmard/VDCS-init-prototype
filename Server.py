class Circuit:
    def __init__(self,F):
        pass


class Garbled_Circuit:
    def __init__(self,F,R1,R2):
        self.outWires =[1,2,3]

    def garble(self):
        return self

    def getOutwires(self):
        return self.outWires

class Server:
    #Input wires. To be stored inside the GC class
    #Output wires.  To be stored inside the GC class

    IDs = 0                             #for keeping track of object ids, alt: use id() func

    def __init__(self):                 #constructor: assigns ID to obj
        self.ID = (Server.IDs+1)
        Server.IDs += 1


    def getID(self):                    #get ID of obj
        return self.ID

    def receiveC(self, F, R1, R2):       #Receive a boolean expression from user
        self.Circuit = Circuit(F)
        self.R1 = R1
        self.R2 = R2

    def receiveS(self, GC, R1, R2):      #Receive a Garbled Circuit from server
        self.GC = GC
        self.R1 = R1
        self.R2

    def garble(self):                   #Garbling F to GC(1)
        self.GC = Garbled_Circuit(self.Circuit, self.R1, self.R2)
        return self.GC

    def eval(self,inWire):              #Evaluating GC(i) on inWire
        return self.GC.eval(inWire), self.GC.getOutWires()

    def reRand(self):                   #reRanding GC(i-1) to GC(i)
        self.GC = Garbled_Circuit(self.GC, self.R1, self.R2)
        return self.GC

    def getGC(self):                    #returning GC(i)
        return self.GC

    def getCircuit(self):               #returning input Circuit
        return self.Circuit