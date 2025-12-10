def generate_diagram(user_message):
    msg = user_message.lower()

    if "class" in msg:
        return (
            "📘 Class Diagram (simplified)\n"
            "\n"
            "[User]\n"
            " - id\n"
            " - name\n"
            " - email\n"
            "\n"
            "[Appointment]\n"
            " - id\n"
            " - time\n"
            " - date\n"
            "\n"
            "User 1 --- * Appointment"
        )

    if "sequence" in msg:
        return (
            "📗 Sequence Diagram (login)\n"
            "\n"
            "User → UI: enter credentials\n"
            "UI → Backend: validate\n"
            "Backend → DB: query user\n"
            "DB → Backend: return result\n"
            "Backend → UI: success"
        )

    return "I can generate class or sequence diagrams. Try: 'Draw class diagram for school system'."
