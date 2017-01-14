# 1/11/17 running an environment according to the tutorial documentation for gym.
# to get this to work using ssh, I used ssh -X and then ran the following:
# xvfb-run -s "-screen 0 1400x900x24" python first_test_example.py
# which allows the code to run.
# export DISPLAY=:0 # doesnt appear to do anything
import gym
import time
import pyprind
import numpy as np
game = 'CartPole-v0'
max_time = 200
num_episodes = 10
render_option = False
# MountainCar-v0, CartPole-v0, MsPacman-v0
env = gym.make(game)

def run_episode(env, weights, render_option=False):  
    observation = env.reset()
    totalreward = 0
    params = np.r_[observation, np.zeros(observation.shape)]
    for time in range(max_time): # max length of game
        if render_option: env.render()
        action = 0 if np.matmul(weights, params) < 0 else 1
        observation_new, reward, done, info = env.step(action)
        params = np.r_[ observation_new, params[ 0:observation.shape[0] ] ] # update params for next trial
        totalreward += reward
        if done:
            break
    return totalreward
    
bestweights = None  
bestreward = 0  
num_trials = 100
verify_trials = 25
reward_sum = []
for trial in range(num_trials):  
    weights = np.random.rand(8) * 2 - 1
    reward = run_episode(env, weights)
    reward_sum.append(reward)
    print '%3d   %5d'%(trial+1, reward)
    if reward > bestreward:
        bestreward = reward
        bestweights = weights
        print('updating weights')
        # considered solved if the agent lasts 200 timesteps
        if reward == 200:
            print 'Scoping out a potential winner.'
            verify_sol_reward = []
            for verify_loop in range(100):
                verify_reward = run_episode(env, bestweights,render_option=False)
                verify_sol_reward.append(verify_reward)    
            if np.mean(verify_sol_reward) >= 195:
                print 'This would have passed the online test in %d episodes! \n mean score over 100 consecutive episodes = %d (195 required)'%(trial+1, np.mean(verify_sol_reward))
                break
                
print bestweights

