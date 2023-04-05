import numpy as np
import math

class StreetWorld:
    def __init__(self, swmap, sim, client, scaler):
        self.swmap = swmap
        self.sim = sim
        self.client = client
        self.scaler = scaler
        self.current_state = []
    def step(self, action):
        # this will get the child script of the manta and
        # allow us to control the manta remotely
        # *** UNTESTED ***
        if action == 'accelerate':
            self.sim.callScriptFunction('controlVehicle', self.sim.getScript(self.sim.scripttype_childscript, self.sim.getObject('Manta')), 1, 0)
        elif action == 'decelerate':
            self.sim.callScriptFunction('controlVehicle', self.sim.getScript(self.sim.scripttype_childscript, self.sim.getObject('Manta')), 0, 0)
        self.client.step()

        # evaluate result of step
        observation = self.sim.callScriptFunction('get_observation', self.sim.getScript(self.sim.scripttype_childscript, self.sim.getObject('Streetworld')))
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
        if loc == 'g':
            goal = 1
        if loc == 'o':
            offroad = 1
        return [goal, offroad]
            



    def reset(self):
        sim.stopSimulation()
        sim.startSimulation()