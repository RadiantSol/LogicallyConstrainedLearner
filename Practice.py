# import LCRL code trainer module
from src.train import train
from Scripts.StreetworldLDBA import StreetworldLDBA
from zmqRemoteApi import RemoteAPIClient
from Scripts.StreetworldMDP import StreetWorld

if __name__ == "__main__":
    client = RemoteAPIClient()
    s = StreetWorld(client)

    MDP = s
    LDBA = StreetworldLDBA

# train the agent
task = train(MDP, LDBA,
                     algorithm='nfq',
                     episode_num=500,
                     iteration_num_max=4000,
                     discount_factor=0.80,
                     learning_rate=0.9
                     )

print(task)