from HMM import HMM
from Robot import Robot

def startRobot():
    pass
def main():
    hmm = HMM()
    robot = Robot(hmm)

    # Order:  West, North, East, South

    robot.senseLocation(("-", "-", "-", "-"))
    robot.moveRobot("NORTH")

    robot.senseLocation(("-", "-", "-", "-"))
    robot.moveRobot("NORTH")

    robot.senseLocation(("-", "-", "O", "-"))
    robot.moveRobot("NORTH")

    robot.senseLocation(("-", "-", "-", "-"))
    robot.moveRobot("EAST")

    robot.senseLocation(("-", "-", "O", "O"))
    robot.moveRobot("NORTH")

    robot.senseLocation(("-", "-", "O", "-"))


if __name__ == "__main__":
    main()