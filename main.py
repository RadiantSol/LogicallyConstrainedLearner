from zmqRemoteApi import RemoteAPIClient
from Scripts.StreetworldMDP import StreetWorld

if __name__ == "__main__":
    client = RemoteAPIClient()
    s = StreetWorld(client)

    #car = s.sim.getObject('/Manta')
    #print(s.sim.getObjectPosition(car, -1))
    #try:
        #client = RemoteAPIClient()
        #s = StreetWorld()
    #except:
    #    client.getObject('sim').stopSimulation()