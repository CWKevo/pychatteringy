from typing import Union

from string import punctuation
from fuzzywuzzy import fuzz


def remove_punctuation(string: str) -> str:
    return string.translate(str.maketrans('', '', punctuation))


def has_punctuation_only(string: str) -> bool:
    return all(i in punctuation for i in string)


def string_ratio(correct: str, attempt: str) -> float:
    if has_punctuation_only(correct) or has_punctuation_only(attempt):
        return fuzz.ratio(correct.lower(), attempt.lower())

    s1 = remove_punctuation(correct).lower()
    s2 = remove_punctuation(attempt).lower()
    return fuzz.ratio(s1, s2)


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

    print("\nLevenshtein fuzzy matching ratio test:")
    for guess in guesses:
        print(f"{guess} - {strings_similarity(correct, guess)}")


if __name__ == "__main__":
    __test_strings()
