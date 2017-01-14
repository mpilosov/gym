# gym.upload('/tmp/cartpole-experiment-1', api_key=)

import gym
# from gym import wrappers
import time
import pyprind
import numpy as np
env = gym.make('CartPole-v0')
# env = wrappers.Monitor(env, '/tmp/cartpole-experiment-1')
max_time = 200

def run_episode(env, weights, render_option=False):  
    observation = env.reset()
    totalreward = 0
    params = observation
    for time in range(max_time): # max length of game
        if render_option: env.render()
        action = 0 if np.matmul(weights, params) < 0 else 1
        observation, reward, done, info = env.step(action)
        params = observation # update params for next trial
        totalreward += reward
        if done:
            break
    return totalreward

bestweights = None  
bestreward = 0  
num_trials = 100
for trial in range(num_trials):  
    weights = np.random.rand(4) * 2 - 1 
    reward = run_episode(env, weights)
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
                if verify_reward < bestreward: 
                    bestreward = np.min(verify_sol_reward)
                if np.mean(verify_sol_reward) < 195 and verify_loop > 8:
                    print 'stopping after %d attempts'%(verify_loop+1)
                    break # stop scoping out this solution if the mean is low    
            if np.mean(verify_sol_reward) >= 195:
                print '\t Would have passed the online test in %d episodes! \n mean score over 100 consecutive episodes = %d (195 required)'%(trial+1, np.mean(verify_sol_reward))
                break

    
                