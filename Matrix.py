import numpy as np

class Matrix(object):

    def __init__(self, height, width):
        # Make a 8 x 11 matrix
        self.width = width
        self.height = height
        self.numberOfStates = 77

    def assignObstacleProb(self, matrix):  
        matrix[4][3] = 0.00

        matrix[4][4] = 0.00

        matrix[3][4] = 0.00

        matrix[2][4] = 0.00

        matrix[5][6] = 0.00

        matrix[5][7] = 0.00

        matrix[2][5] = 0.00

        matrix[2][6] = 0.00

        matrix[2][7] = 0.00

        matrix[4][7] = 0.00

        matrix[3][7] = 0.00

    def createPriorMatrix(self):
        priorList = [[(float(1) / self.numberOfStates) * 100.00] * self.width] * self.height
        priorMatrix = np.array(priorList)

        self.assignObstacleProb(priorMatrix)

        for row in priorMatrix:
            print(row)

        return priorMatrix

    def createTransitionMatrix(self, heading):

        #index each state tuple to a matrix(8X11) with  transition prob
        transitionMatrix = np.empty(shape=(1, 88))
        for x in range(0, self.height):
            for y in range(0, self.width):
                stateMatrix = np.array([[round(0.000, 2)] * self.width] * self.height)
                if self.isNotAnObstacle((x, y)):
                    self.assignTransitionProb(heading, (x, y), stateMatrix)
                    stateMatrix = stateMatrix.flatten()
                    transitionMatrix = np.vstack((transitionMatrix, stateMatrix))
                else:
                    stateMatrix = stateMatrix.flatten()
                    transitionMatrix = np.vstack((transitionMatrix, stateMatrix))

        # Delete first row (irrelevant)
        transitionMatrix = np.delete(transitionMatrix, 0, 0)

        return transitionMatrix

    def assignTransitionProb(self, heading, state, matrix):
        totalProbability = 0.00
        if heading == "NORTH":
            x, y = state
            if self.isWithinBoundary((x -1, y)):
                if self.isNotAnObstacle((x -1, y)):
                    matrix[x - 1][y] = 0.80
                else:
                    matrix[x - 1][y] = 0.00
                totalProbability += matrix[x - 1][y]

            if self.isWithinBoundary((x, y - 1)):
                if self.isNotAnObstacle((x, y - 1)):
                    matrix[x][y - 1] = 0.10
                else:
                    matrix[x][y - 1] = 0.00
                totalProbability += matrix[x][y - 1]

            if self.isWithinBoundary((x, y + 1)):
                if self.isNotAnObstacle((x, y + 1)):
                    matrix[x][y + 1] = 0.10  
                else:
                    matrix[x][y + 1] = 0.00
                totalProbability += matrix[x][y + 1]

            # probability the robot bounced back to current position
            if totalProbability < 1.00:
                matrix[x][y] = round(1.00 - totalProbability, 2)

        elif heading == "EAST":
            x, y = state
            if self.isWithinBoundary((x, y + 1)):
                if self.isNotAnObstacle((x, y + 1)):
                    matrix[x][y + 1] = 0.80
                else:
                    matrix[x][y + 1] = 0.00
                totalProbability += matrix[x][y + 1]

            if self.isWithinBoundary((x - 1, y)):
                if self.isNotAnObstacle((x - 1, y)):
                    matrix[x - 1][y] = 0.10
                else:
                    matrix[x - 1][y] = 0.00
                totalProbability += matrix[x - 1][y]

            if self.isWithinBoundary((x + 1, y)):
                if self.isNotAnObstacle((x + 1, y)):
                    matrix[x + 1][y] = 0.10  
                else:
                    matrix[x + 1][y] = 0.00
                totalProbability += matrix[x + 1][y]

            # probability the robot bounced back to current position
            if totalProbability < 1.00:
                matrix[x][y] = round(1.00 - totalProbability, 2)

        else:
            # For future headings 
            pass

    def isNotAnObstacle(self, coordinate):
        obstacles = [(4, 3), (4, 4), (3, 4), (2, 4), (5, 6), (5, 7), (2, 5), (2, 6), (2, 7), (4, 7), (3, 7)]

        if coordinate in obstacles:
            return False
        
        return True

    def isWithinBoundary(self, coordinate):
            x, y = coordinate
            # Check if a node is within the boundary of the map
            if (x >= 0 and x < 8) and (y >= 0 and y < 11):
                return True
            else:
                return False

    def representAsPerecentage(self, matrix, switch):
        if switch == True:
            for x in range(0, self.height):
                for y in range(0, self.width):
                    matrix[x][y] = matrix[x][y] * 100.00
        
        else:
             for x in range(0, self.height):
                for y in range(0, self.width):
                    matrix[x][y] = matrix[x][y] / 100.00


    def printMatrix(self, matrix):
         for row in matrix:
            print(row)
            print(" ")
