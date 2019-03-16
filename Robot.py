class Robot:
    def __init__(self, hmmModel):
        self.hmm = hmmModel

    def senseLocation(self, perception):

        self.hmm.sensorUpdate(perception)
        self.hmm.printGrid()
    
    def moveRobot(self, heading):

        self.hmm.motionUpdate(heading)
        self.hmm.printGrid()
    

    

   
   





