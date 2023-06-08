import unittest


# Layer 1: Presentation Layer
class GameController:
    def __init__(self, game_service):
        self.game_service = game_service

    def start_game(self, player_name):
        # Validate input
        if not player_name:
            return "Please enter a player name."

        # Call the service layer to start a new game
        game_id = self.game_service.start_game(player_name)
        if game_id:
            return f"Game started! ID: {game_id}"
        else:
            return "Failed to start the game."


# Layer 2: Service Layer
class GameService:
    def __init__(self, game_repository):
        self.game_repository = game_repository

    def start_game(self, player_name):
        # Create a new game and save to repository
        game = Game(player_name)
        return self.game_repository.save_game(game)


# Layer 3: Data Access Layer
class GameRepository:
    def __init__(self):
        self.games = {}
        self.next_id = 1

    def save_game(self, game):
        game_id = self.next_id
        self.games[game_id] = game
        self.next_id += 1
        return game_id


# Domain Model
class Game:
    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0


# Unit Tests
class GameControllerTest(unittest.TestCase):
    def setUp(self):
        repository = GameRepository()
        service = GameService(repository)
        self.controller = GameController(service)

    def test_start_game_with_valid_player_name(self):
        result = self.controller.start_game("Alice")
        self.assertTrue("Game started!" in result)
        self.assertTrue("ID:" in result)

    def test_start_game_with_empty_player_name(self):
        result = self.controller.start_game("")
        self.assertEqual(result, "Please enter a player name.")

    def test_start_game_with_no_player_name(self):
        result = self.controller.start_game(None)
        self.assertEqual(result, "Please enter a player name.")


if __name__ == '__main__':
    unittest.main()
