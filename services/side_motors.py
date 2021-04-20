"""
____________________________________________________
Author: Supuni Kaveendya
Date: 16/04/2021
Version : 1.0
Name: Dc motor controller
Properties: Rotate Dc Motor Forward and Backward
_______________________________________________________
"""

from roboclaw.roboclaw import RoboClaw


class SpinOneSide:
    def __init__(self, address):
        self.address = address  # address array of the RoboClaw as set in Motion Studio(ex:0x80)[2 addresses for 2 mortors]
        self.roboclaw = RoboClaw(“ / dev / ttyS0”, 38400)  # Create the RoboClaw object, passing the serial port and baudrate
        self.roboclaw.Open()

    def verify_speed(self, speed):
        # speed in a range from 0 to 127
        if speed > 127:
            speed = 127
        elif speed < 0:
            speed = 0
        else:
            speed = speed
        return speed

    def forward(self, speed):
        roboclaw = self.roboclaw

        speed = self.verify_speed(speed=speed)
        # the first parameter is the address, the second is the speed in a range from 0 to 127
        roboclaw.ForwardM1(self.address[0], speed)
        roboclaw.ForwardM2(self.address[1], speed)

    def backward(self, speed):
        roboclaw = self.roboclaw
        speed = self.verify_speed(speed=speed)
        # the first parameter is the address, the second is the speed in a range from 0 to 127
        roboclaw.BackwardM1(self.address[0], speed)
        roboclaw.BackwardM2(self.address[1], speed)

    def stop_motors(self):
        """Stops both motors on one side of the rover"""
        self.roboclaw.ForwardM1(self.address[0], 0)
        self.roboclaw.ForwardM2(self.address[1], 0)
