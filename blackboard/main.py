import random
import unittest


class Blackboard:
    def __init__(self):
        self.knowledge = {}

    def add_knowledge(self, key, value):
        self.knowledge[key] = value

    def get_knowledge(self, key):
        return self.knowledge.get(key)


class Problem:
    def __init__(self, description):
        self.description = description


class Solver:
    def __init__(self, blackboard):
        self.blackboard = blackboard

    def solve_problem(self, problem):
        if "weather" in problem.description:
            self._solve_weather_problem()
        elif "recommendation" in problem.description:
            self._solve_recommendation_problem()
        else:
            print("Solver - Problem not supported")

    def _solve_weather_problem(self):
        temperature = random.randint(20, 40)
        self.blackboard.add_knowledge("temperature", temperature)

    def _solve_recommendation_problem(self):
        recommendations = ["Book", "Movie", "Restaurant"]
        recommendation = random.choice(recommendations)
        print(recommendation)
        self.blackboard.add_knowledge("recommendation", recommendation)


class SolverTest(unittest.TestCase):
    def setUp(self):
        self.blackboard = Blackboard()
        self.solver = Solver(self.blackboard)

    def test_solve_weather_problem(self):
        problem = Problem("What's the current weather?")
        self.solver.solve_problem(problem)
        temperature = self.blackboard.get_knowledge("temperature")
        self.assertIsNotNone(temperature)
        self.assertGreaterEqual(temperature, 20)
        self.assertLessEqual(temperature, 40)

    def test_solve_recommendation_problem(self):
        problem = Problem("Can you recommend something to do?")
        self.solver.solve_problem(problem)
        print(self.blackboard.knowledge)
        recommendation = self.blackboard.get_knowledge("recommendation")
        self.assertEqual(recommendation, None)


if __name__ == '__main__':
    unittest.main()
