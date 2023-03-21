# Import Game
import gym_super_mario_bros
# Import Joypad Wrapper
from nes_py.wrappers import JoypadSpace
# Import SIMPLIFIED Controls
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

# Setup Game
env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env, SIMPLE_MOVEMENT)

# Make Flag: determines whether the game restarts
done = True
# Frame Loop
for step in range(100000):
  # Initial Game Start
  if done:
    # Start Game
    env.reset()
  # Random Action
  state, reward, done, info = env.step(env.action_space.sample())
  # Show Game
  env.render()
# Close Game
env.close()
