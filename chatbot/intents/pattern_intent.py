from architecture_engine.core.pattern_advisor import suggest_pattern

def handle_pattern_intent(user_message):
    """
    Handles design pattern advice:
    - 'Which pattern is best for messaging?"
    - 'What pattern should I use for scalability?"
    """
    return suggest_pattern(user_message)
