#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ***** BEGIN LICENSE BLOCK *****
# This file is part of EV3WebController.
# Copyright (c) 2014-2015 Cédric Bonhomme.
# All rights reserved.
#
#
#
# ***** END LICENSE BLOCK *****

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2015/11/05$"
__revision__ = "$Date: 2015/11/05 $"
__copyright__ = "Copyright (c) 2014-2015 Cédric Bonhomme"
__license__ = ""

import time
from ev3.ev3dev import Motor

from web import button

def stop(motorA, motorB):
    """
    Stop the motors.
    """
    motorA.stop()
    motorB.stop()

def run_position_limited(motorA, motorB, position):
    """
    Run for a limitied position.
    """
    motorA.position = 0
    motorA.run_position_limited(position_sp=position, speed_sp=800,
                   stop_mode=Motor.STOP_MODE.BRAKE, ramp_up_sp=1000,
                   ramp_down_sp=1000)
    motorB.position = 0
    motorB.run_position_limited(position_sp=position, speed_sp=800,
                   stop_mode=Motor.STOP_MODE.BRAKE, ramp_up_sp=1000,
                   amp_down_sp=1000)
    # Wait for the completion of the command before sending the result
    while "running" in motorA.state.split(" ") and \
                        "running" in motorB.state.split(" "):
        time.sleep(0.1)
        if button.is_pushed:
            stop(motorA, motorB)
            return "hit_wall"
    return "OK"