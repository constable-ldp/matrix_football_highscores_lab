import unittest

from src.high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Test
    def setUp(self):
        self.high_score = [400, 600, 450, 700, 900, 300]
        
    
    # Test latest score (the last thing in the list)
    def test_latest_score(self):
        self.assertEqual(300, latest(self.high_score))

    # Test personal best (the highest score in the list)
    def test_personal_best(self):
        self.assertEqual(900, personal_best(self.high_score))

    # Test top three from list of scores
    def test_personal_top_three(self):
        new_high_score = [900, 700, 600, 450, 400, 300]
        self.assertEqual([600, 700, 900], personal_top_three(self.high_score))
        self.assertEqual([600, 700, 900], personal_top_three(new_high_score))
    
    # Test ordered from highest to lowest


    # Test top three when there is a tie
    def test_top_three_if_tie(self):
        new_high_score = [300, 400, 450, 600, 600]
        self.assertEqual([450, 600, 600], personal_top_three(new_high_score))

    # Test top three when there are less than three
    def test_top_three_when_less(self):
        new_high_score = [100]
        self.assertEqual([100], personal_top_three(new_high_score))

    # Test top three when there is only one
    
