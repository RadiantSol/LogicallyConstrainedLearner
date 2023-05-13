import math
import time
from Scripts.ObsPioneer import Observation
from Scripts.TargetHandler import move_target
import numpy as np
from config import STEP_LENGTH, DISPLAY_DISABLED

# MDP representation from LCRL
class StreetWorld:
    def __init__(self, client):
        self.action_space = [
            "north",
            "north_east",
            "east",
            "south_east",
            "south",
            "south_west",
            "west",
            "north_west",
            "stay"
        ]
        self.client = client
        self.client.setStepping(True)
        self.sim = self.client.getObject('sim')
        self.sim.startSimulation()

        #Pioneer/Car
        self.car_handle = self.sim.getObject('/PioneerP3DX')
        self.car_script = self.sim.getScript(self.sim.scripttype_childscript, self.car_handle)
        self.client.step()
        self.current_state = np.array([])
    
    def step(self, action):
        # process action
        target_handle = self.sim.getObject('/Target')
        if action == "north":
            move_target(self.sim,0,self.car_handle,target_handle, self.client)
        elif action == 'north_east':
            move_target(self.sim,1,self.car_handle,target_handle, self.client)
        elif action == 'east':
            move_target(self.sim,2,self.car_handle,target_handle, self.client)
        elif action == 'south_east':
            move_target(self.sim,3,self.car_handle,target_handle, self.client)
        elif action == 'south':
            move_target(self.sim,4,self.car_handle,target_handle, self.client)
        elif action == 'south_west':
            move_target(self.sim,5,self.car_handle,target_handle, self.client)
        elif action == 'west':
            move_target(self.sim,6,self.car_handle,target_handle, self.client)
        elif action == 'north_west':
            move_target(self.sim,7,self.car_handle,target_handle, self.client)
        elif action == 'stay':
            move_target(self.sim,8,self.car_handle,target_handle, self.client)
        
        # x, y, _ = self.sim.getObjectPosition(self.car_handle, target_handle)
        # startTime = self.sim.getSimulationTime()
        # wait for car to reach target
        # if it has been longer than about 20 seconds, target is unreachable and loop should end prematurely
        # while (abs(x) > 0.25 and abs(y) > 0.25):
        #     x, y, _ = self.sim.getObjectPosition(self.car_handle, target_handle)
        #     if startTime + 20 < self.sim.getSimulationTime():
        #         print("Movement time limit reached")
        #         break
        #     elif self.sim.getStringSignal("Collision") == "true":
        #         print("Collision detected")
        #         break
        #     if abs(x) <= 0.25 and abs(y) <= 0.25:
        #         print("Target reached")
        # execute action and take steps
        # for _ in range(STEP_LENGTH):
        #     self.client.step()

        # check for obstacles

        # update agent state
        self.agent_state = np.array(Observation.get_observation(self.sim))

        # return the MDP state
        mdp_state = self.agent_state
        # print(mdp_state)
        self.current_state = mdp_state
        return mdp_state
    
    def state_label(self, state):
        #check if in goal
        if Observation.check_goal(self.sim):
            if Observation.check_red(self.sim):
                return ["goal", "red"]
            else:
                return ["goal"]
        else:
            if Observation.check_off_map(self.sim):
                return["off"]
            else:
                if Observation.check_red(self.sim):
                    if Observation.check_moving(self.sim):
                        return ["red","moving","road"]
                    else:
                        return ["red","road"]
                else:
                    return ["road"]
            
    def reset(self):
        self.sim.stopSimulation()
        time.sleep(0.5)
        self.sim.startSimulation()
        self.sim.setShapeColor(self.sim.getObject('/Light'), None, self.sim.colorcomponent_ambient, [1, 0, 0])
        self.sim.setStringSignal("TrafficLight", "red")
        self.sim.setStringSignal("Collision", "false")
        if DISPLAY_DISABLED:
            self.sim.setBoolParam(self.sim.boolparam_display_enabled, False)
        self.client.step()
        self.agent_state = np.array(Observation.get_observation(self.sim))
        self.current_state = self.agent_state