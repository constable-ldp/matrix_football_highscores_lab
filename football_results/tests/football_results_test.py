import unittest
from src.football_results import get_result, get_results

class FootballResultsTest(unittest.TestCase):
    def setUp(self):
        self.scores_home_win = {
            'home_score': 2,
            'away_score': 1
        }
        self.scores_away_win = {
            'home_score': 1,
            'away_score': 2
        }
        self.scores_draw = {
            'home_score': 0,
            'away_score': 0
        }
        self.scores_list = [{
            'home_score': 2,
            'away_score': 1
        },
        {
            'home_score': 1,
            'away_score': 2
        },
        {
            'home_score': 0,
            'away_score': 0
        }]
    # Test we get the right result string for a final score dictionary representing -

        # Home win
        # Away win
        # Draw

    def test_final_scores(self):
        self.assertEqual('Home Win', get_result(self.scores_home_win))
        self.assertEqual('Away Win', get_result(self.scores_away_win))
        self.assertEqual('Draw', get_result(self.scores_draw))

    def test_final_scores_list(self):
        self.assertEqual(['Home Win', 'Away Win', 'Draw'], get_results(self.scores_list))

    # Test we get right list of result strings for a list of final score dictionaries. 


if __name__ == "__main__":
    unittest.main()
