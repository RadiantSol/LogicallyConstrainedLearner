import time
from zmqRemoteApi import RemoteAPIClient
import StreetWorld
import numpy as np
import math

client = RemoteAPIClient()
sim = client.getObject('sim')

client.setStepping(True)
sim.startSimulation()
client.step()
sim.callScriptFunction('generateTrack', sim.getScript(sim.scripttype_childscript, sim.getObject('/Streetworld')), 0)
client.step()
# print(swmap)
# print(scaler)
# StreetWorld(swmap, sim, client, scaler)