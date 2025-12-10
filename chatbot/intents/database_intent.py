from architecture_engine.core.database_designer import generate_database_design

def handle_database_intent(user_message):
    """
    Handles database design requests:
    - 'Generate ER diagram for library system'
    - 'Give database tables for food delivery'
    """
    return generate_database_design(user_message)
