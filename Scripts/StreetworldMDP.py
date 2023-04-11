import math
import time
from Scripts.Obs import Observation
from config import STEP_LENGTH

# MDP representation from LCRL
class StreetWorld:
    def __init__(self, client):
        self.action_space = [
            "accelerate0",
            "accelerate1",
            "accelerate2",
            "accelerate3",
            "accelerate4",
            #"decelerate0",
            #"decelerate1",
            #"decelerate2",
            #"decelerate3",
            #"decelerate4",
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
    
    # 10 total actions
    # accelerate/decelerate 1 m/s^2
    # set steering angle to -30/-15/0/15/30
    # controlVehicle(acceleration, steering angle)
    def step(self, action):
        # process action
        if action == 'accelerate0':
            self.sim.callScriptFunction('controlVehicle', self.manta_script, 1, 0)
        elif action == 'decelerate0':
            self.sim.callScriptFunction('controlVehicle', self.manta_script, 0, 0)
        elif action == 'accelerate1':
            self.sim.callScriptFunction('controlVehicle', self.manta_script, 1, 1)
        elif action == 'decelerate1':
            self.sim.callScriptFunction('controlVehicle', self.manta_script, 0, 1)
        elif action == 'accelerate2':
            self.sim.callScriptFunction('controlVehicle', self.manta_script, 1, 2)
        elif action == 'decelerate2':
            self.sim.callScriptFunction('controlVehicle', self.manta_script, 0, 2)
        elif action == 'accelerate3':
            self.sim.callScriptFunction('controlVehicle', self.manta_script, 1, 3)
        elif action == 'decelerate3':
            self.sim.callScriptFunction('controlVehicle', self.manta_script, 0, 3)
        elif action == 'accelerate4':
            self.sim.callScriptFunction('controlVehicle', self.manta_script, 1, 4)
        elif action == 'decelerate4':
            self.sim.callScriptFunction('controlVehicle', self.manta_script, 0, 4)
        
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
        self.sim.setBoolParam(self.sim.boolparam_display_enabled, False)
        self.client.step()
        self.agent_state = Observation.get_observation(self.sim)
        self.current_state = [self.agent_state]