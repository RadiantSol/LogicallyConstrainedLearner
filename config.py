AL_CHOICE = 'ddpg'
DISPLAY_DISABLED = False

# Various hyperparameters for the model
STEP_LENGTH = 10    # number of steps to take in the simulator for each action (CoppeliaSim default sim step is 50ms per step)
DISCOUNT = 0.95     # discount factor for the Q-learning algorithm
ITERATIONS = 18000   # number of iterations to run the Q-learning algorithm for
LEARNING_RATE = 0.05 # learning rate for the Q-learning algorithm
EPISODES = 20000    # number of episodes to run the Q-learning algorithm for