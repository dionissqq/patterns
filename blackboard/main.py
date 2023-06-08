import random


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
        self.blackboard.add_knowledge("recommendation", recommendation)


# Usage
if __name__ == '__main__':
    # Create an instance of the Blackboard
    blackboard = Blackboard()

    # Create an instance of the Solver with the Blackboard
    solver = Solver(blackboard)

    # Add some knowledge to the Blackboard
    blackboard.add_knowledge("location", "New York")

    # Define a weather problem
    weather_problem = Problem("What's the current weather?")

    # Solve the weather problem using the Solver
    solver.solve_problem(weather_problem)

    # Retrieve the temperature from the Blackboard
    temperature = blackboard.get_knowledge("temperature")

    # Print the temperature
    print("Temperature in New York:", temperature)

    # Define a recommendation problem
    recommendation_problem = Problem("Can you recommend something to do?")

    # Solve the recommendation problem using the Solver
    solver.solve_problem(recommendation_problem)

    # Retrieve the recommendation from the Blackboard
    recommendation = blackboard.get_knowledge("recommendation")

    # Print the recommendation
    print("Recommendation:", recommendation)
