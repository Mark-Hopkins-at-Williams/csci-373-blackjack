import random
from collections import defaultdict


class QLearningAgent:
  
    def __init__(self, env, epsilon=0.7, discount=1.0, rollout_length=10):
        """Initializes a QLearningAgent.
        
        Parameters
        ----------
        env : environment.Environment
            the Environment we want to learn to navigate
        epsilon : float
            percentage of the time that we "explore", i.e. try a random action
        discount : float
            discount factor
        rollout_length : int
            maximum number of actions taken in each rollout        
        """
        self._env = env
        self._epsilon = epsilon
        self._discount = discount
        self._rollouts_so_far = 0
        self._rollout_length = rollout_length
        self._qvalues = defaultdict(float)
        self._num_samples = defaultdict(int)

    def perform_rollout(self):
        """Performs a single rollout.
        
        A rollout consists of resetting the Environment, and then doing actions
        (i.e. calling the .do_action method of the Environment) until one of
        the following conditions hold:
        - we have done the maximum number of actions (as specified by self._rollout_length)
        - we have arrived in a state where no actions are possible

        After doing each action, the self._qvalues and self._num_samples attributes 
        should be updated according to the q-learning algorithm.
        """
        self._env.reset()
        # TODO: complete this method (Question One)

    def explore_or_exploit(self):
        """Chooses an action based on an 'exploration' or 'exploitation' strategy.
        
        'Exploration' means to choose an action at random from the set of possible
        actions available in our current state.

        'Exploitation' means to choose the best action (according to our current
        best policy) for our current state.

        Exploration will always be the chosen strategy if our current best policy
        doesn't have an action associated with the current state. Otherwise, 
        exploration will be the chosen strategy X percent of the time, where
        X = self._epsilon.        
        """
        random_action = random.choice(self._env.get_possible_actions())
        if random.random() < self._epsilon:
            action = random_action
        else:
            policy = self.get_policy()
            action = policy.get(self._env.get_current_state(), random_action)
        return action

    def get_policy(self):
        """Computes the current best policy.
        
        For each state, we associate the action such that self.get_qvalue(state, action)
        is maximized. 

        Returns
        -------
        dict
            A dictionary associating each state with an action        
        """
        policy = dict()
        best_qvalue = dict()
        for (state, action) in self._qvalues:
            qvalue = self._qvalues[(state, action)]
            if qvalue > best_qvalue.get(state, float('-inf')):
                best_qvalue[state] = qvalue
                policy[state] = action
        return policy

    def get_qvalue(self, state, action):
        """Returns the current q-value for the specified (state, action) pair."""
        return self._qvalues[(state, action)]

    def get_rollouts_so_far(self):
        """Returns the number of times that .perform_rollout has been called so far."""
        return self._rollouts_so_far

