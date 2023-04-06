import math
from Obs import Observation

# MDP representation from LCRL
class StreetWorld:
    def __init__(self, client):
        self.client = client
        self.client.setStepping(True)
        self.sim = self.client.getObject('sim')
        self.sim.startSimulation()

        #Manta
        self.manta_handle = self.sim.getObject('/Manta')
        self.manta_script = self.sim.getScript(self.sim.scripttype_childscript, self.manta_handle)


        self.current_state = []
    
    def step(self, action):
        # this will get the child script of the manta and
        # allow us to control the manta remotely
        # *** UNTESTED ***
        if action == 'accelerate':
            self.sim.callScriptFunction('controlVehicle', self.manta_script, 1, 0)
        elif action == 'decelerate':
            self.sim.callScriptFunction('controlVehicle', self.manta_script, 0, 0)
        self.client.step()

        # evaluate result of step
        observation = self.sim.callScriptFunction('get_observation', self.track_script)
        # reversing scaled values using given scaler
        coords = self.scaler.inverse_transform([observation[0][0], observation[0][1]])
        # round to 0 decimal places just in case
        coords[0] = math.round(coords[0])
        coords[1] = math.round(coords[1])
        carpos = self.swmap[coords[0]][coords[1]]
        # calculate distance from center of track
        for i in self.swmap[coords[0]]:
            if i == 'c':
                center = self.swmap[coords[0]].index(i)
        dist = abs(center - coords[1])
        self.current_state = self.current_state + [dist, math.round(observation[1])]
        return self.current_state
    
    def state_label(state):
        goal = False
        offroad = False
        #this is wrong
        loc = state
        if loc == 'g':
            goal = 1
        if loc == 'o':
            offroad = 1
        return [goal, offroad]
            
    def reset(self):
        self.sim.stopSimulation()
        self.sim.startSimulation()