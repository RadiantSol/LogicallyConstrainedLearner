import math
import time
from Scripts.Obs import Observation

# MDP representation from LCRL
class StreetWorld:
    def __init__(self, client):
        self.action_space = [
            "accelerate",
            "decelerate"
        ]
        self.client = client
        self.client.setStepping(True)
        self.sim = self.client.getObject('sim')
        self.sim.startSimulation()

        #Manta/Car
        self.manta_handle = self.sim.getObject('/Manta')
        self.manta_script = self.sim.getScript(self.sim.scripttype_childscript, self.manta_handle)
        self.client.step()
        self.current_state = []
    
    def step(self, action):
        # process action
        if action == 'accelerate':
            self.sim.callScriptFunction('controlVehicle', self.manta_script, 1, 0)
        elif action == 'decelerate':
            self.sim.callScriptFunction('controlVehicle', self.manta_script, 0, 0)
        
        # execute action for 10 steps
        for _ in range(10):
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
        self.client.step()
        self.agent_state = Observation.get_observation(self.sim)
        self.current_state = [self.agent_state]