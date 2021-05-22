from typing import Union

from string import punctuation
from jellyfish import jaro_distance
import time

def remove_punctuation(string: str) -> str:
    return string.translate(str.maketrans('', '', punctuation))


def has_punctuation_only(string: str) -> bool:
    return all(i in punctuation for i in string)


def string_ratio(correct: str, attempt: str) -> float:
    s1 = correct.lower().strip()
    s2 = attempt.lower().strip()

    if has_punctuation_only(s1) or has_punctuation_only(s2):
        dist = jaro_distance(s1, s2) * 100
        return round(dist)

    dist = jaro_distance(remove_punctuation(s1), remove_punctuation(s2)) * 100
    return round(dist)


def strings_similarity(correct: str, attempt: str, threshold: int=65) -> Union[int, None]:
    ratio = string_ratio(correct, attempt)

    if ratio >= threshold:
        return ratio
    else:
        return None


def __test_strings():
    print("Punctuation test:")
    punct_test = ["...", "!?", "Ah.", "Indeed..."]
    for string in punct_test:
        print(f"{string} - {has_punctuation_only(string)}")

    correct = "Today I have walked into a house."
    guesses = ["I have walked in a house today.", "I walked in the house!", "The house is mine...", "I walked in a house today!", "Today I walked?"]

    print("\nJaro distance:")
    start = time.time()

    for guess in guesses:
        print(f"{guess} - {strings_similarity(correct, guess)}")

    end = time.time()
    print("Jaro distance took:", end - start) # 0.000x - 0.003x - Levenshtein distance is a bit slower

if __name__ == "__main__":
    __test_strings()
