from Matrix import Matrix
import numpy as np
np.set_printoptions(precision= 'maxprec', formatter={'float': lambda x: "{0:0.2f}".format(x)})

class HMM(object):

    SENSED_AN_OBSTACLE_AS_OBSTACLE = 0.90
    SENSED_A_STATE_AS_OBSTACLE = 0.05

    SENSED_SENSED_AN_OBSTACLE_AS_STATE = 0.10
    SENSED_A_STATE_AS_STATE = 0.95

    def __init__(self):
        self.matrix = Matrix(8, 11)
        self.northTransitionMatrix = self.matrix.createTransitionMatrix("NORTH")
        self.eastTransitionMatrix = self.matrix.createTransitionMatrix("EAST")
        self.probabilityMatrix = self.matrix.createPriorMatrix()

    def sensorUpdate(self, perception):
        w, n, e, s = perception
        tempMatrix = self.probabilityMatrix

        self.matrix.representAsPerecentage(self.probabilityMatrix,False)

        for x in range(0, 8):
            for y in range(0, 11):
                westProb = self.assignSensedProb((x, y - 1), w)
                northProb = self.assignSensedProb((x - 1, y), n)
                eastProb = self.assignSensedProb((x, y + 1), e)
                southProb = self.assignSensedProb((x + 1, y), s)

                prior = self.probabilityMatrix[x][y]
                probability = (westProb * northProb * eastProb * southProb) * prior
                tempMatrix[x][y] = probability

        tempMatrix /= np.sum(tempMatrix)
        self.matrix.representAsPerecentage(tempMatrix, True)
        
        #Debug
        #totalProbability = np.sum(tempMatrix)

        self.probabilityMatrix = tempMatrix

    def motionUpdate(self, heading):
        tempMatrix = self.probabilityMatrix

        self.matrix.representAsPerecentage(tempMatrix, False)

        tempMatrix = tempMatrix.flatten()
        if heading == "NORTH":
            tempMatrix = tempMatrix.dot(self.northTransitionMatrix)
        elif heading == "EAST":
            tempMatrix = tempMatrix.dot(self.eastTransitionMatrix)

        tempMatrix = tempMatrix.reshape(8, 11)
        self.matrix.representAsPerecentage(tempMatrix, True)
        self.probabilityMatrix = tempMatrix


    def assignSensedProb(self, state, evidence):
        # West, North, East, South
        x, y = state

        if self.matrix.isNotAnObstacle((x, y)) and self.matrix.isWithinBoundary((x, y)):
            #West
            if(evidence == "O"):
                return self.SENSED_A_STATE_AS_OBSTACLE
            else:
                return self.SENSED_A_STATE_AS_STATE
        else:
            # If state is an obstacle
            if(evidence == "O"):
                # Robot sees an obstacle
                return self.SENSED_AN_OBSTACLE_AS_OBSTACLE
            else:
                # Robot sees state
                return self.SENSED_SENSED_AN_OBSTACLE_AS_STATE


    def printGrid(self):
        print("Probability Matrix of Robot's Location")
        self.matrix.printMatrix(self.probabilityMatrix)

    """  print(" ")
        for row in tMatrix:
            print(row)
            print(" ") """