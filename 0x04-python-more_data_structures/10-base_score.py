#!/usr/bin/python3


def best_score(a_dictionary):
    """Returns a key with the biggest integer value"""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    max_key = None
    max_value = float("-inf")

    for key, value in a_dictionary.items():
        if value > max_value:
            max_key = key
            max_value = value
    return max_key
