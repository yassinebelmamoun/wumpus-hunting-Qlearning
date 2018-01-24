import numpy as np
import collections

"""
Contains the definition of the agent that will run in an
environment.
"""

ACT_UP    = 1
ACT_DOWN  = 2
ACT_LEFT  = 3
ACT_RIGHT = 4
ACT_TORCH_UP    = 5
ACT_TORCH_DOWN  = 6
ACT_TORCH_LEFT  = 7
ACT_TORCH_RIGHT = 8

class RandomAgent:
    def __init__(self):
        self.lr = .01   # learning rate 
        self.gamma = .9
        self.epsilon = 0.5 
        self.q_table = {}   # state (tuple) : [0, ... , 0] 
        self.iteration = 0
        self.previous_observation = None
        self.episode = 1
        self.step = 0


    def reset(self):
        self.step = 0
        self.episode += 1

    def act(self, observation):
        self.step += 1
        self.epsilon = 0.5
        self.previous_observation = observation
        position, smell, breeze, charges = observation
        
        self.create_state(observation)
        if np.random.uniform() >= self.epsilon or self.episode >= 900:
            state_action = self.q_table[observation]
            action = state_action.index(max(state_action)) + 1 
        else:
            action = np.random.randint(1,8)
        return action 

    def reward(self, observation, action, reward):
        """
            Receive a reward for performing given action on given observation.
            This is where your agent can learn.
        """
        self.learn(s=self.previous_observation,
                a = action - 1,
                r = reward,
                s_= observation,
            ) 
    
    def create_state(self, state):
        """
            If new state, create it in the q_table
        """
        if state not in self.q_table.keys():
            self.q_table[state] = 8 * [0]
    
    def learn(self, s, a, r, s_):
        self.create_state(s_)
        q_predict = self.q_table[s][a]
        q_target = r + self.gamma * max(self.q_table[s_])
        self.q_table[s][a] += self.lr * (q_target - q_predict)

Agent = RandomAgent
