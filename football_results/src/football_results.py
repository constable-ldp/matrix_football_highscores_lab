'''
Input: final_score (dict).  Dictionary of home score and away score.
Method: Take the dictionary and work out whether it is a Home Win, Away Win, or Draw.
Output: Home Win, Away Win or Draw (str) 

'''


def get_result(final_score):
    if final_score["home_score"] > final_score["away_score"]:
        return "Home Win"
    elif final_score["home_score"] < final_score["away_score"]:
        return "Away Win"
    else:
        return "Draw"

def get_results(final_scores):
    return [get_result(result) for result in final_scores]
    # (You could try and use a list comprehension for this)