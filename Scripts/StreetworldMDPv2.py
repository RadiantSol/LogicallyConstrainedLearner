import math
import time
from Scripts.Obs import Observation
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
        self.current_state = []
    
    def step(self, action):
        # process action
        if action == "north":
            self.sim.callScriptFunction('controlVehicle', self.car_script, 0)
        elif action == 'north_east':
            self.sim.callScriptFunction('controlVehicle', self.car_script, 1)
        elif action == 'east':
            self.sim.callScriptFunction('controlVehicle', self.car_script, 2)
        elif action == 'south_east':
            self.sim.callScriptFunction('controlVehicle', self.car_script, 3)
        elif action == 'south':
            self.sim.callScriptFunction('controlVehicle', self.car_script, 4)
        elif action == 'south_west':
            self.sim.callScriptFunction('controlVehicle', self.car_script, 5)
        elif action == 'west':
            self.sim.callScriptFunction('controlVehicle', self.car_script, 6)
        elif action == 'north_west':
            self.sim.callScriptFunction('controlVehicle', self.car_script, 7)
        elif action == 'stay':
            self.sim.callScriptFunction('controlVehicle', self.car_script, 8)
        
        # execute action and take steps
        for _ in range(STEP_LENGTH):
            self.client.step()

        # check for obstacles

        # update agent state
        self.agent_state = Observation.get_observation(self.sim)

        # return the MDP state
        mdp_state = self.agent_state
        self.current_state = mdp_state
        return [mdp_state]
    
    def state_label(self, state):
        #check if in goal
        if Observation.check_goal(self.sim):
            return ["goal"]
        else:
            if Observation.check_off_map(self.sim):
                return["off"]
            else:
                return ["road"]
            
    def reset(self):
        self.sim.stopSimulation()
        time.sleep(1)
        self.sim.startSimulation()
        if DISPLAY_DISABLED:
            self.sim.setBoolParam(self.sim.boolparam_display_enabled, False)
        self.client.step()
        self.agent_state = Observation.get_observation(self.sim)
        self.current_state = [self.agent_state]