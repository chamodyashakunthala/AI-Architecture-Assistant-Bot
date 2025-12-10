# architecture_engine/core/database_designer.py

def generate_database_model(project_name: str) -> str:
    """
    Generates a basic database model idea using entities and relationships.
    """

    return (
        f"Database Model for {project_name}:\n"
        "- Entities:\n"
        "  * User (user_id, name, email)\n"
        "  * Project (project_id, title, description)\n"
        "  * Task (task_id, title, status)\n"
        "- Relationships:\n"
        "  * User 1---N Project\n"
        "  * Project 1---N Task"
    )

