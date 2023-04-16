import unittest
from blackjack import BlackjackEnvironment
from games import DeterministicBlackjackGame

class TestBlackjack(unittest.TestCase):

    def test_episode1(self):
        game = DeterministicBlackjackGame()
        env = BlackjackEnvironment(game)       
        state = env.get_current_state()
        self.assertEqual(state, "START")
        actions = env.get_possible_actions()
        self.assertEqual(set(actions), {'deal'})
        env.do_action("deal")
        state = env.get_current_state()
        self.assertEqual(state, ("16", "8"))
        actions = env.get_possible_actions()
        self.assertEqual(set(actions), {'hit', 'stand'})
        env.do_action("hit")
        state = env.get_current_state()
        self.assertEqual(state, ("18", "8"))
        actions = env.get_possible_actions()
        self.assertEqual(set(actions), {'hit', 'stand'})
        env.do_action("stand")
        state = env.get_current_state()
        self.assertEqual(state, "LOSE")
        actions = env.get_possible_actions()
        self.assertEqual(set(actions), set())

    def test_episode2(self):
        game = DeterministicBlackjackGame()
        env = BlackjackEnvironment(game)       
        state = env.get_current_state()
        self.assertEqual(state, "START")
        actions = env.get_possible_actions()
        self.assertEqual(set(actions), {'deal'})
        env.do_action("deal")
        state = env.get_current_state()
        self.assertEqual(state, ("16", "8"))
        actions = env.get_possible_actions()
        self.assertEqual(set(actions), {'hit', 'stand'})
        env.do_action("stand")
        state = env.get_current_state()
        self.assertEqual(state, "WIN")
        actions = env.get_possible_actions()
        self.assertEqual(set(actions), set())

