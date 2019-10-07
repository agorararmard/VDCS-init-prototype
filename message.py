import circuit

class message:

    def __init__(self,circ,R, winx=0, winy=0):
        self.circ = circ
        self.R = R
        self.winx = winx
        self.winy = winy
    
    def extract(self):
        return self.circ,self.R,self.winx, self.winy
