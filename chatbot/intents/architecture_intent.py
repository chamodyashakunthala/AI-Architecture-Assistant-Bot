from architecture_engine.core.architecture_generator import generate_architecture

def handle_architecture_intent(user_message):
    """
    Handles architecture-related requests.
    Example:
    - "Give me a 3-tier architecture for an e-commerce system"
    - "Create a microservices architecture for hospital management"
    """
    return generate_architecture(user_message)
