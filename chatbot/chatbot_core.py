from chatbot.nlp_engine import NLPEngine
from chatbot.intents.architecture_intent import handle_architecture_intent
from chatbot.intents.diagram_intent import handle_diagram_intent
from chatbot.intents.pattern_intent import handle_pattern_intent
from chatbot.intents.database_intent import handle_database_intent


class ChatbotCore:

    def __init__(self):
        self.nlp = NLPEngine()

    def process_message(self, user_message):
        # 1. Detect intent
        intent = self.nlp.detect_intent(user_message)

        # 2. Route intent
        if intent == "architecture_intent":
            return handle_architecture_intent(user_message)

        elif intent == "diagram_intent":
            return handle_diagram_intent(user_message)

        elif intent == "pattern_intent":
            return handle_pattern_intent(user_message)

        elif intent == "database_intent":
            return handle_database_intent(user_message)

        else:
            return "I'm not sure what you mean. Can you rephrase?"
