from typing import Union

from string import punctuation
from fuzzywuzzy import fuzz


def remove_punctuation(string: str) -> str:
    return string.translate(str.maketrans('', '', punctuation))


def string_ratio(correct: str, attempt: str) -> float:
    s1 = remove_punctuation(correct)
    s2 = remove_punctuation(attempt)
    return fuzz.ratio(s1.lower(), s2.lower())


def strings_similarity(correct: str, attempt: str, threshold: int=65) -> Union[int, None]:
    ratio = string_ratio(correct, attempt)

    if ratio >= threshold:
        return ratio
    else:
        return None


if __name__ == "__main__":
    correct = "Today I have walked into a house."
    guesses = ["I have walked in a house today.", "I walked in the house!", "The house is mine...", "I walked in a house today!", "Today I walked?"]

    for guess in guesses:
        print(f"{guess} - {are_strings_similar(correct, guess)}")
