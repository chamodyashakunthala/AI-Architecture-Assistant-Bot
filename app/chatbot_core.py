from .nlp_engine import detect_intent
from .intents.architecture_intent import handle_architecture_intent
from .intents.diagram_intent import handle_diagram_intent
from .intents.pattern_intent import handle_pattern_intent
from .intents.database_intent import handle_database_intent


def chatbot_response(user_message):
    # 1. Detect intent
    intent = detect_intent(user_message)

    # 2. Route to correct handler
    if intent == "architecture_intent":
        return handle_architecture_intent(user_message)

    elif intent == "diagram_intent":
        return handle_diagram_intent(user_message)

    elif intent == "pattern_intent":
        return handle_pattern_intent(user_message)

    elif intent == "database_intent":
        return handle_database_intent(user_message)

    else:
        # fallback
        return (
            "I'm not sure what you mean.\n"
            "Try asking:\n"
            "- 'Suggest architecture for a school app'\n"
            "- 'Generate class diagram for ecommerce'\n"
            "- 'Recommend a design pattern'\n"
        )
