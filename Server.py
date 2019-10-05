class Garbled_Circuit:
    def garble(self):
        return self

class Server:
    
    IDs = 0

    def __init__(self):
        self.ID = (Server.IDs+1)
        Server.IDs += 1


    def getID(self):
        return self.ID

    


