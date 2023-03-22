# Load Model
model = PPO.load('./train/best_model_1000000')
state = env.reset()

# Start Game
state = env.reset()

# Loop Through Game
while True: 
    
    action, _ = model.predict(state)
    state, reward, done, info = env.step(action)
    env.render()
