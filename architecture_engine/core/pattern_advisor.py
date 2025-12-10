def suggest_pattern(user_message):
    msg = user_message.lower()

    if "payment" in msg:
        return "Use the Strategy Pattern for multiple payment methods."

    if "logging" in msg:
        return "Use the Singleton Pattern for a centralized logging manager."

    if "notifications" in msg:
        return "Use the Observer Pattern for push notifications."

    if "database" in msg:
        return "Use the Repository Pattern to abstract data access."

    return "Try asking: 'Which pattern should I use for login, caching, messaging, or notifications?'"
