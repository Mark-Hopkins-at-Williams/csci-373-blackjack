import unittest

from mdp import ClashMdp
from qlearning import QLearningAgent

class TestQLearning(unittest.TestCase):

    def test_value_iteration(self):
        mdp = ClashMdp()
        agent = QLearningAgent(mdp, rollout_length=10, discount=0.5)
        for _ in range(20000):
            agent.perform_rollout()
        policy = agent.get_policy()
        self.assertEqual(policy['A'], 'stay')
        self.assertEqual(policy['B'], 'go')
        self.assertAlmostEqual(agent.get_qvalue('A', 'stay'), 0.82, places=1)
        self.assertAlmostEqual(agent.get_qvalue('A', 'go'), 0.24, places=1)
        self.assertAlmostEqual(agent.get_qvalue('B', 'stay'), -1.75, places=1)
        self.assertAlmostEqual(agent.get_qvalue('B', 'go'), -1.52, places=1)

    def test_value_iteration2(self):
        mdp = ClashMdp()
        agent = QLearningAgent(mdp, rollout_length=10, discount=0.3)
        for _ in range(20000):
            agent.perform_rollout()
        policy = agent.get_policy()
        self.assertEqual(policy['A'], 'stay')
        self.assertEqual(policy['B'], 'go')
        self.assertAlmostEqual(agent.get_qvalue('A', 'stay'), 0.96, places=1)
        self.assertAlmostEqual(agent.get_qvalue('A', 'go'), 0.63, places=1)
        self.assertAlmostEqual(agent.get_qvalue('B', 'stay'), -1.37, places=1)
        self.assertAlmostEqual(agent.get_qvalue('B', 'go'), -1.23, places=1)
        
        

if __name__ == "__main__":
    unittest.main()   