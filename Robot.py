class Robot:
    def __init__(self, hmmModel):
        self.hmm = hmmModel

    def senseLocation(self, perception):
        w, n, e, s = perception

        self.hmm.sensorUpdate(perception)
        self.hmm.printGrid()
    
    

    

   
   





