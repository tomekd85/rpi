import pigpio
import time

class Baymax(object):
    def __init__(self):
        self.move_duration = 0.5

        #pins connected to drv8833
        self.a_in1 = 23
        self.a_in2 = 24
        self.b_in1 = 5
        self.b_in2 = 6

        self.pi = pigpio.pi()
        self._set_pins_mode()

    def _set_pins_mode(self):
        self.pi.set_mode(self.a_in1, pigpio.OUTPUT)
        self.pi.set_mode(self.a_in1, pigpio.OUTPUT)
        self.pi.set_mode(self.a_in1, pigpio.OUTPUT)
        self.pi.set_mode(self.a_in1, pigpio.OUTPUT)

    def move_forward(self, *args, **kwargs):
        self._a_wheel_forward()
        self._b_wheel_forward()
#        time.sleep(self.move_duration)

    def move_backward(self, *args, **kwargs):
        self._a_wheel_backward()
        self._b_wheel_backward()
#        time.sleep(self.move_duration)

    def turn_left(self, *args, **kwargs):
        self._a_wheel_forward()
        self._b_wheel_backward()
#        time.sleep(self.move_duration)

    def turn_right(self, *args, **kwargs):
        self._a_wheel_backward()
        self._b_wheel_forward()
#        time.sleep(self.move_duration)

    def stop(self, *args, **kwargs):
        self._a_wheel_stop()
        self._b_wheel_stop()

    def _a_wheel_forward(self):
        self.pi.write(self.a_in1, 1)
        self.pi.write(self.a_in2, 0)

    def _a_wheel_backward(self):
        self.pi.write(self.a_in2, 1)
        self.pi.write(self.a_in1, 0)

    def _b_wheel_forward(self):
        self.pi.write(self.b_in1, 1)
        self.pi.write(self.b_in2, 0)

    def _b_wheel_backward(self):
        self.pi.write(self.b_in2, 1)
        self.pi.write(self.b_in1, 0)

    def _a_wheel_stop(self):
        self.pi.write(self.a_in1, 0)
        self.pi.write(self.a_in2, 0)

    def _b_wheel_stop(self):
        self.pi.write(self.b_in1, 0)
        self.pi.write(self.b_in2, 0)

    def finish_work(self):
        self.pi.stop()

if __name__ == "__main__":
    my_robot = Baymax()
    my_robot.move_forward()
    time.sleep(5)
    my_robot._a_wheel_stop()
    my_robot._b_wheel_stop()
    my_robot.finish_work()
