from architecture_engine.core.diagram_generator import generate_diagram

def handle_diagram_intent(user_message):
    """
    Handles diagram requests such as:
    - "Draw a class diagram"
    - "Give me an activity diagram for login"
    """
    return generate_diagram(user_message)
