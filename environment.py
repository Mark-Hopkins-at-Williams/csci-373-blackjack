from abc import ABC, abstractmethod


class Environment(ABC):
    @abstractmethod
    def reset(self):
        """Resets the environment to the beginning of a game."""

    @abstractmethod
    def get_current_state(self):
        """Returns the current state."""
    
    @abstractmethod
    def get_current_reward(self):
        """Returns the reward associated with the current state."""
        
    @abstractmethod
    def get_possible_actions(self):
        """Returns a list of possible actions in the current state."""

    @abstractmethod
    def do_action(self, action):
        """Updates the environment after performing the specified action."""

 