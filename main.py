from zmqRemoteApi import RemoteAPIClient
from Scripts.StreetworldMDP import StreetWorld

if __name__ == "__main__":
    client = RemoteAPIClient()
    s = StreetWorld(client)
    #try:
        #client = RemoteAPIClient()
        #s = StreetWorld()
    #except:
    #    client.getObject('sim').stopSimulation()