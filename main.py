from zmqRemoteApi import RemoteAPIClient
from Scripts.StreetworldMDP import StreetWorld

if __name__ == "__main__":
    client = RemoteAPIClient()
    s = StreetWorld(client)
