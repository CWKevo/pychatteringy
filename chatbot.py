from json import dumps
from random import choice
from typing import Union
from intents import INTENTS_ROOT, Intent, intent_generator
from string_operations import are_strings_similar


def get_possible_intent(query: str) -> Union[Intent, None]:
    for intent in intent_generator():
        for possible_query in intent.user:
            if are_strings_similar(query, possible_query):
                return intent


def get_response(query: str, fallback: str="Sorry, I don't understand that yet.") -> str:
    intent = get_possible_intent(query)

    if not intent:
        return fallback

    if intent.condition.state == True:
        response = choice(intent.bot)

    elif intent.condition.state == False:
        if intent.condition.else_responses:
            response = choice(intent.condition.else_responses)

        else:
            return fallback
    else:
        response = choice(intent.bot)

    return response


if __name__ == "__main__":
    print(get_response(input("You: ")))
