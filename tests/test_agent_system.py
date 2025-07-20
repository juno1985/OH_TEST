


import unittest
from agents.planner.main import PlannerAgent

class TestAgentSystem(unittest.TestCase):
    def setUp(self):
        self.agent = PlannerAgent()

    def test_coding_agent_routing(self):
        result = self.agent.execute("Implement a function that adds two numbers")
        self.assertEqual(result["status"], "success")
        self.assertIn("implementation", result)

    def test_ci_agent_routing(self):
        result = self.agent.execute("Set up CI pipeline")
        self.assertEqual(result["status"], "success")
        self.assertIn("message", result)
        self.assertIn("CI pipeline setup simulated", result["message"])

if __name__ == "__main__":
    unittest.main()


