import re

class NLPEngine:

    def __init__(self):
        # Predefined keyword → intent mapping
        self.intent_map = {
            "class diagram": "diagram_intent",
            "use case diagram": "diagram_intent",
            "activity diagram": "diagram_intent",
            "state diagram": "diagram_intent",
            "sequence diagram": "diagram_intent",

            "architecture": "architecture_intent",
            "system design": "architecture_intent",
            "high level design": "architecture_intent",

            "pattern": "pattern_intent",
            "design pattern": "pattern_intent",

            "database": "database_intent",
            "er diagram": "database_intent",
            "data model": "database_intent"
        }

    def clean_text(self, text):
        text = text.lower().strip()
        text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
        return text

    def extract_keywords(self, text):
        words = text.split()
        return words

    def detect_intent(self, text):
        cleaned = self.clean_text(text)

        for key in self.intent_map:
            if key in cleaned:
                return self.intent_map[key]

        # Fallback
        return "unknown_intent"
