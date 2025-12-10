def generate_database_design(user_message):
    msg = user_message.lower()

    if "library" in msg:
        return (
            "📚 Library Database Design\n"
            "Entities:\n"
            "- Book(book_id, title, author_id)\n"
            "- Author(author_id, name)\n"
            "- Member(member_id, name)\n\n"
            "Relationships:\n"
            "- Author 1 --- * Book\n"
            "- Member * --- * Book (borrow)"
        )

    if "school" in msg:
        return (
            "🏫 School Database Design\n"
            "Entities:\n"
            "- Student(id, name, grade)\n"
            "- Teacher(id, name, subject)\n"
            "- Class(id, room)\n\n"
            "Relationships:\n"
            "- Teacher 1 --- * Class\n"
            "- Student * --- 1 Class"
        )

    return "Try: 'Create database for hospital/library/school/e-commerce'."
