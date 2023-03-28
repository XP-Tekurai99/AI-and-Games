# Import Environment Base Class from OpenAI Gym
from gym import Env
# Import Gym Spaces 
from gym.spaces import Discrete, Box
# Import opencv 
import cv2

game.get_state().screen_buffer.shape

# Create Vizdoom OpenAI Gym Environment
class VizDoomGym(Env): 
    # Function That is Called on Environment Start
    def __init__(self, render=False): 
        # Inherit from Env
        super().__init__()
        # Setup Game
        self.game = DoomGame()
        self.game.load_config('github/VizDoom/scenarios/basic.cfg')
        
        # Render Frame Logic
        if render == False: 
            self.game.set_window_visible(False)
        else:
            self.game.set_window_visible(True)
        
        # Start Game 
        self.game.init()
        
        # Create Action Space and Observation Space
        self.observation_space = Box(low=0, high=255, shape=(100,160,1), dtype=np.uint8) 
        self.action_space = Discrete(3)
        
    # Take a Step in the Environment
    def step(self, action):
        # Specify Action and Take Step 
        actions = np.identity(3)
        reward = self.game.make_action(actions[action], 4) 
        
        # Get Remaining Return Info 
        if self.game.get_state(): 
            state = self.game.get_state().screen_buffer
            state = self.grayscale(state)
            ammo = self.game.get_state().game_variables[0]
            info = ammo
        else: 
            state = np.zeros(self.observation_space.shape)
            info = 0 
        
        info = {"info":info}
        done = self.game.is_episode_finished()
        
        return state, reward, done, info 
    
    # Define Rendering
    def render(): 
        pass
    
    # What Happens Upon Game Start
    def reset(self): 
        self.game.new_episode()
        state = self.game.get_state().screen_buffer
        return self.grayscale(state)
    
    # Grayscale Game Frame and Resize
    def grayscale(self, observation):
        gray = cv2.cvtColor(np.moveaxis(observation, 0, -1), cv2.COLOR_BGR2GRAY)
        resize = cv2.resize(gray, (160,100), interpolation=cv2.INTER_CUBIC)
        state = np.reshape(resize, (100,160,1))
        return state
    
    # Close Game
    def close(self): 
        self.game.close()
