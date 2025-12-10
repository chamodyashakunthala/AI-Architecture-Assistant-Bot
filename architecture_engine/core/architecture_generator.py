# architecture_engine/core/architecture_generator.py

def generate_architecture(project_type: str) -> str:
    """
    Generate a high-level software architecture description
    based on the project type.
    """
    if "mobile" in project_type.lower():
        return (
            "Mobile App Architecture:\n"
            "- Client Layer (React Native / Flutter)\n"
            "- API Gateway\n"
            "- Backend Service Layer (FastAPI / Node.js)\n"
            "- Database Layer\n"
            "- Optional: Authentication Service"
        )

    if "web" in project_type.lower():
        return (
            "Web Application Architecture:\n"
            "- Frontend (React / Vue)\n"
            "- Backend REST API (FastAPI)\n"
            "- Service Layer\n"
            "- Database Layer (PostgreSQL)"
        )

    if "microservice" in project_type.lower():
        return (
            "Microservice Architecture:\n"
            "- API Gateway\n"
            "- Multiple independent services\n"
            "- Event-driven communication (Kafka)\n"
            "- Centralized logging + monitoring"
        )

    return (
        "Standard 3-Tier Architecture:\n"
        "- Presentation Layer\n"
        "- Application Layer\n"
        "- Data Layer"
    )
