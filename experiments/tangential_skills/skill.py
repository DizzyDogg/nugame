#!/bin/env python

'''
A skill can be trained and will atrophy with time.

In this experiment, skill level will range from 0 to 100%.  The amount of
practice required to reach a given skill level will be on a tangential scale:

practice_time = tangent(percent * 0.01 * pi/2) * scaling_factor

Atrophy will knock off practice time at a set rate for all skills.

Rationale:

This avoids having an arbitrary cap on skill levels while allowing people
to excel to degrees that others haven't approached before.
'''

import math

def practice_to_percent(practice):
    return 

def percent_to_practice(percent):
    return math.tan(percent * 0.01 * math.pi / 2) * practice_unit

practice_unit = 1
practice_unit = 1.0 / percent_to_practice(1)

class Skill(object):
    def __init__(self):
        pass 
