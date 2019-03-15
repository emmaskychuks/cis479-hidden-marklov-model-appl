from HMM import HMM
from Robot import Robot

def startRobot():
    pass
def main():
    hmm = HMM()
    robot = Robot(hmm)

    robot.senseLocation(("O", "-", "-", "-"))


if __name__ == "__main__":
    main()