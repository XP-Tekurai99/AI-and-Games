# Import Frame Stacker Wrapper and GrayScale Wrapper
from gym.wrappers import GrayScaleObservation
# Import Vectorization Wrappers
from stable_baselines3.common.vec_env import VecFrameStack, DummyVecEnv
# Import Matplotlib
from matplotlib import pyplot as plt

# 1. Base Environement
env = gym_super_mario_bros.make('SuperMarioBros-v0')
# 2. Control Simplification
env = JoypadSpace(env, SIMPLE_MOVEMENT)
# 3. Grayscale
env = GrayScaleObservation(env, keep_dim=True)
# 4. Dummy Environment
env = DummyVecEnv([lambda: env])
# 5. Stack Frames
env = VecFrameStack9env, 6, channels_order='last'

# Show Frame with Matplotlib
plt.imshow(state[0])

plt.figure(figsize=(20,16))
for idx in range(state.shape[3]):
  plt.subplot(1,4,idx+1)
  plt.imshow(state[0][:,:,idx])
plt.show()
