import random


def get_response(user_input: str) -> str:

    confused_responses = ["????", "what are you talking about", "...?", "what????", "`confused = True`"]
    random_response = random.choice(confused_responses)

    lowered: str = user_input.lower()

    if lowered == ".":
        return "..."
    elif "hello" in lowered or "hi" in lowered:
        return "hi"
    elif "what" in lowered:
        return "what"
    elif "bye" in lowered:
        return "bye"
    else:
        return random_response
