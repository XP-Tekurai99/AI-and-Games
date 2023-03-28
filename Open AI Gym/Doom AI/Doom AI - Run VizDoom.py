# Import vizdoom: Game Environment
from vizdoom import *
# Import random: Action Sampling
import random
# Import time: Sleeping
import time
# Import numpy: Identity Matrix
import numpy as np

# Setup Game
game = vizdoom.DoomGame()
game.load('github/VizDoom/scenarios/basic.cfg')
game.init()

# Set of Potential Actions
actions = np.identity(3, dtype=np.uint8)
random.choice(actions)

game.new_episode()
game.is_episode_finished()
game.make_action(random.choice(actions))

episodes = 50
for episode in range(episodes):
    game.new_episode()
    while not game.is_episode_finished():
        # Get the game state 
        state = game.get_state()
        # Get the game image 
        img = state.screen_buffer
        # Get the game variables - ammo
        info = state.game_variables
        # Take an action
        reward = game.make_action(random.choice(actions),4)
        # Print rewward 
        print('reward:', reward) 
        time.sleep(0.02)
    print('Result:', game.get_total_reward())
    time.sleep(2)

game.close()
