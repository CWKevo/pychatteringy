from typing import List, Union

import parse
from jellyfish import jaro_distance

punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`|~""" # excluded curly brackets for variables


def remove_punctuation(string: str) -> str:
    punct = punctuation.replace("{", '').replace("}", '') # exclude curly brackets for variables
    return string.translate(str.maketrans('', '', punct))


def has_punctuation_only(string: str) -> bool:
    return all(i in punctuation for i in string)


def string_ratio(correct: str, attempt: str) -> int:
    s1 = correct.lower().strip()
    s2 = attempt.lower().strip()

    if has_punctuation_only(s1) or has_punctuation_only(s2):
        dist = jaro_distance(s1, s2) * 100
        return round(dist)

    dist = jaro_distance(remove_punctuation(s1), remove_punctuation(s2)) * 100
    return round(dist)


def strings_similarity(correct: str, attempt: str, threshold: int=80) -> Union[int, None]:
    ratio = string_ratio(correct, attempt)

    if ratio >= threshold:
        return ratio
    else:
        return None


def simplify_template(template: str, exclude_a: bool=True, words_around: int=2) -> str:
    template_words = template.split(" ")
    
    if exclude_a:
        template_words_no_a = []
        for word in template_words:
            if word != "a" or word != "an":
                template_words_no_a.append(word)

        template_words = template_words_no_a

    sliced_template = str()

    for word_set in template_words:
        index = template_words.index(word_set)

        if "{" and "}" in word_set:
            for word in template_words[index - words_around:index + words_around]:
                if word not in sliced_template:
                    sliced_template += f"{word} "

    return sliced_template.strip()


def extract_entities(templates: List[str], query: str, **kwargs) -> dict:
    for template in templates:
        stripped_template = simplify_template(template, **kwargs)
        all_entities = parse.search(stripped_template, query + ".") # appending dot will prevent failure, if there is no dot

        if all_entities:
            return all_entities.named

        else:
            return dict()


def __test_strings(entities: bool=False):
    templates = ["I'd like to buy a {thing} for {price}.", "Can I have a {thing} for {price}?", "I want {thing}."]
    users = [
        "Can I have a boat for 1 €?",
        "I want something tasty.",
        "Technically I pose the right amount of money to buy a really nice house for quite some amount of money."
    ]

    if entities:
        for template in templates:
            for user in users:
                entities = extract_entities(template, user)

                if entities:
                    print(f"Template: {template}\nUser: {user}")
                    print("Entities:", entities, end="\n\n")

        return

    else:
        import time # you only need to import it when running this function

        print("Punctuation test:")
        punct_test = ["...", "!?", "Ah.", "Indeed..."]
        for string in punct_test:
            print(f"{string} - {has_punctuation_only(string)}")

        correct = "Today I have walked into {{place}}."
        guesses = ["I have walked in a house today.", "I walked in the house!", "The house is mine...", "I walked in a house today!", "Today I walked?"]

        print("\nJaro distance:")
        start = time.time()

        for guess in guesses:
            print(f"{guess} - {string_ratio(correct, guess)}")

        end = time.time()
        return print("Jaro distance took:", end - start) # 0.000x - 0.003x - Levenshtein distance is a bit slower


if __name__ == "__main__":
    __test_strings(entities=True)
