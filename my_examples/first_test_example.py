# 1/11/17 running an environment according to the tutorial documentation for gym.
# to get this to work using ssh, I used ssh -X and then ran the following:
# xvfb-run -s "-screen 0 1400x900x24" python first_test_example.py
# which allows the code to run.
# export DISPLAY=:0 # doesnt appear to do anything

import gym
import time
game = 'CartPole-v0'
# MountainCar-v0, CartPole-v0, MsPacman-v0
env = gym.make(game)
env.reset()
for i_episode in range(2):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(t, observation)
        time.sleep(1)
        action = env.action_space.sample() # take random action 
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break

# import matplotlib.pyplot as plt
# plt.plot([1,2,3,4])
# plt.ylabel('some numbers')
# plt.show()