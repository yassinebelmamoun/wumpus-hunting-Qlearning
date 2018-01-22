# Introduction

## The problem
The Wumpus world is a well-known toy problem in artificial intelligence popularized by the reference book of Russell and Norvig, 2003. The game consists in a grid world where an agent is looking for a treasure while avoiding the deadly Wumpus and some holes. We assume that the time is discretized and that the agent can take only one action per time step. The agent can explore the grid by moving in the four cardinal directions. Also, it has a flashlight with a limited number of power units that can be used to kill the Wumpus. For the project, the Wumpus world will be our benchmark problem for studying reinforcement learning (RL) algorithms. Moreover, these algorithms are general enough to be applied to different problems (environment).

## Explanation

In the RL framework, we define an environment, which specifies the information to be used by the agent to take some actions. For the Wumpus world, the environment is partially observable since the locations of the holes, the Wumpus and the treasure are unknown to the agent. However, the environment provides some signals to the agent:

* if the agent is adjacent to the Wumpus, it receives a _smell_ signal
* if the agent is adjacent to the hole, it receives a _breeze_ signal
* the location of the agent is _deterministically_ determined by the initial position and the actions
* the number of _power units_ is known

At each time step, the agent can choose one of 8 different actions:

* Up
* Down
* Left
* Right
* FlashUp
* FlashDown
* FlashLeft
* FlashRight.

Attempting to move through the bounding walls of the arena results in nothing happening.

Each time step can lead to 5 different outcomes, in terms of reward for your agent:

* The treasure is found: __reward +100 and the game ends__
* You kill the Wumpus: __reward +10__
* The Wumpus catches you: __reward −10 and the game ends__
* You fall into a hole: __reward −10 and the game ends__
* Nothing happens: __reward −1__


__Question 1__

Why is it interesting to give a negative reward for the ”nothing happens” event ?

The observations available to the agent can be summed up as the following observation space: O = (X, Y, S, B, F)

* __X__ and __Y__ are the coordinates of the location of the agent
* __S__ is a boolean value indicating the presence of the smell signal
* __B__ is a boolean value indicating the presence of the Breeze signal
* __F__ the number of remaining charges for the flashlight.

This observation and some previously saved information by your agent can form its __state s__.


__Question 2__

Run the provided random agent. You can activate the __--verbose__ flag to see a map of the world printed to observe the dynamics. 

What do you observe on its __cumulative reward__?

During this exercise, we will study RL algorithms for learning the optimal __POLICY__ that __maps each state to an action__.
For a given state s, we are interested in the expected reward __Ep(r|s,a)__ [r] where p(r|s, a) is the probability to obtain a reward r given that the agent takes action a in state s. 

However, p(r|s, a) is unknown to the agent, but we can still approximate it with empirical averages. For this, each time the agent is in state s, it chooses an action a, records the observed reward (history) and updates the average Q(s, a).
In the contextual bandit framework, each state s is considered as a different context, leading (in the simplest framework) to as many independent bandit problems as there are states. The arms of the bandit s are the possible actions the agent can perform in that state s.

__Question 3__

Implement a contextual bandit algorithm with one of the policies we studied:

* Optimistic
* Greedy
* Softmax
* UCB

and display its cumulative rewards.

What is the limitation of modeling the problem with contextual bandits?

Possibly consider different state spaces such as:
* S = (B, S, F)
* S = (Aprevious, B, S, F) (i.e. remembering the previous action)
* S = (X, Y, B, S, F)

and study the relation between the grid size, the number of states, the amount of history, ... and the performance of the policy. In order to obtain statistics on the performances, you can run the training algorithm many times using the __--batch__ argument.


__Question 4__

Implement the Q-learning algorithm.


## Code structure

The only files we have action on are: agent.py and main.py.

1 - agent.py:

This one is the file containing the strategy.

2 - main.py:

This one is the program that will actually run the agent.
You can run it with the command:
```python
python main.py
```

It also accepts a few command-line arguments:

* --ngames N will run the agent for N games against in the same environment (the same initial grid setup) and report the total cumulative reward
* --niter N maximum number of iterations allowed for each game
* --batch B will run B instances of the game (B different Wumpus worlds, i.e. with the same rules but different initial grid setups)
* --verbose will print details at each step of what your agent did. In particular, it will show in ASCII art its current location on the grid as well as the one of the Wumpus (which is moving).

The running of your agent follows a general procedure that will be shared for all later practicals:
* The environment generates an observation
* This observation is provided to your agent via the act method which chooses an action


## Solution:

* TO DO *
