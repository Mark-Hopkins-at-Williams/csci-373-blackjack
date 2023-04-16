import numpy
from numpy.random import default_rng
from collections import defaultdict
from environment import Environment

class Mdp(Environment):
    def __init__(self, states, actions, transition_weights,
                 initial_state, final_states, rewards):
        self.states = states
        self.actions = actions
        self.initial_state = initial_state
        self.final_states = final_states
        self.weights = transition_weights
        self.successor_prob = defaultdict(list)
        for transition in self.weights:
            state, action, successor = transition
            self.successor_prob[(state, action)].append((successor, self.weights[transition]))
        self.rewards = rewards
        self.current_state = self.initial_state
        self.rng = default_rng()

    def get_states(self):
        return self.states

    def get_actions(self):
        return self.actions

    def get_initial_state(self):
        return self.initial_state

    def get_final_states(self):
        return self.final_states

    def get_successor_probs(self, state, action):
        return {successor: weight for (successor, weight) in self.successor_prob[(state, action)]}

    def get_reward(self, state):
        return self.rewards[state]

    def reset(self):
        self.current_state = self.initial_state

    def get_current_state(self):
        return self.current_state

    def get_current_reward(self):
        return self.rewards[self.current_state]

    def get_possible_actions(self):
        return self.actions

    def do_action(self, action):
        successor_probs = self.successor_prob[(self.current_state, action)]
        successors = [successor for successor, _ in successor_probs]
        probs = [prob for _, prob in successor_probs]
        self.current_state = self.rng.choice(successors, p=probs)
        if type(self.current_state) == numpy.ndarray:
            self.current_state = tuple(self.current_state)
        return self.current_state


class ClashMdp(Mdp):
    def __init__(self):
        super().__init__(states=["A", "B"],
                         actions=["stay", "go"],
                         transition_weights={("A", "stay", "A"): 0.5,
                                             ("A", "stay", "B"): 0.5,
                                             ("A", "go", "B"): 1.0,
                                             ("B", "stay", "B"): 1.0,
                                             ("B", "go", "A"): 0.2,
                                             ("B", "go", "B"): 0.8},
                         initial_state="A",
                         final_states=[],
                         rewards={"A": 1, "B": -1})

