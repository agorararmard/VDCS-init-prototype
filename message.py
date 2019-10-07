class message:

    def __init__(self,F,cid,R):
        self.F = F
        self.cid = cid
        self.R = R
    
    def extract(self):
        return self.F,self.cid,self.R