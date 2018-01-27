class Mover:
    def __init__(self):
        print("Mover initialized")

    def _set_pins_mode(self):
        print("Pins set")

    def move_forward(self, *args, **kwargs):
        print("Moving forward")

    def move_backward(self, *args, **kwargs):
        print("Moving backward")

    def turn_left(self, *args, **kwargs):
        print("Turning left")

    def turn_right(self, *args, **kwargs):
        print("Turning right")

    def stop(self, *args, **kwargs):
        # print("Stopping")
        pass

    def _a_wheel_forward(self):
        raise NotImplementedError

    def _a_wheel_backward(self):
        raise NotImplementedError

    def _b_wheel_forward(self):
        raise NotImplementedError

    def _b_wheel_backward(self):
        raise NotImplementedError

    def _a_wheel_stop(self):
        raise NotImplementedError

    def _b_wheel_stop(self):
        raise NotImplementedError

    def finish_work(self):
        print("Finished work")


if __name__ == "__main__":
    my_robot = Mover()
    my_robot.move_forward()

