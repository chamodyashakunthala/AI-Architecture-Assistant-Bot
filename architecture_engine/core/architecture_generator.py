def generate_architecture(user_message):
    """
    Very simple rule-based architecture generator.
    You can improve this later.
    """

    msg = user_message.lower()

    if "microservice" in msg:
        return (
            "🧩 Microservices Architecture\n"
            "- API Gateway\n"
            "- Multiple independent services\n"
            "- Database per service\n"
            "- Service registry\n"
            "- Message broker (Kafka / RabbitMQ)"
        )

    if "3 tier" in msg or "three tier" in msg:
        return (
            "🏛 3-Tier Architecture\n"
            "1. Presentation Layer (React/Flutter)\n"
            "2. Application Layer (FastAPI/Node.js)\n"
            "3. Database Layer (MySQL/MongoDB)"
        )

    if "monolithic" in msg:
        return (
            "📦 Monolithic Architecture\n"
            "- Single codebase for all modules\n"
            "- MVC structure\n"
            "- Shared database"
        )

    return "I can generate microservices, monolithic, or 3-tier architectures. Try asking: 'Give microservices architecture for a hospital system'."
