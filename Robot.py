class Robot:
    def __init__(self, hmmModel):
        self.hmm = hmmModel

    def senseLocation(self, perception):

        self.hmm.sensorUpdate(perception)
        print("Robot Senses: {0}".format(perception))
        self.hmm.printGrid()
    
    def moveRobot(self, heading):

        self.hmm.motionUpdate(heading)
        print("Robot is Moving {0}".format(heading))
        self.hmm.printGrid()
    

    

   
   





