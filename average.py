def average_scores(scores_dict):
    if not isinstance(scores_dict, dict):
        raise TypeError("The input is not a dictionary")
    if not scores_dict:
        raise ValueError("The dictionary is empty")
    total = 0
    for score in scores_dict.values():
        total += score
    return total / len(scores_dict)