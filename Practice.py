# import LCRL code trainer module
from src.train import train
from Scripts.StreetworldLDBA import StreetworldLDBA
from zmqRemoteApi import RemoteAPIClient
from Scripts.StreetworldMDP import StreetWorld
from config import *

if __name__ == "__main__":
    client = RemoteAPIClient()
    s = StreetWorld(client)

    MDP = s
    LDBA = StreetworldLDBA

# train the agent
task = train(MDP, LDBA,
                     algorithm=AL_CHOICE,
                     episode_num=EPISODES,
                     iteration_num_max=ITERATIONS,
                     discount_factor=DISCOUNT,
                     learning_rate=LEARNING_RATE,
                     )

print(task)