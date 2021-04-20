from services.side_motors import SpinOneSide


class Move:
    def __init__(self):
        self.left = SpinOneSide(address=[0x80, 0x70])  # change pin numbers
        self.right = SpinOneSide(address=[0x80, 0x70])  # change pin numbers

    def forward(self, speed):
        left = self.left
        right = self.right
        left.forward(speed=speed)
        right.backward(speed=speed)

    def backward(self, speed):
        left = self.left
        right = self.right
        right.forward(speed=speed)
        left.backward(speed=speed)

    def Break(self):
        left = self.left
        right = self.right
        left.stop_motors()
        right.stop_motors()
