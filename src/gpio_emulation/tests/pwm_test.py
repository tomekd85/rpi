"""
Tests for PWM output
Input is one of four directions N, S, W, E.
Depending on how long the direction is kept relevant PWM fill should
increase.

"""

# N both engines go forward
def test_forward_direction():
    input = N
    
    PWM1 = 1
    PWM2 = 0
    PWM3 = 1
    PWM4 = 0
