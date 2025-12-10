# architecture_engine/core/pattern_advisor.py

def recommend_pattern(problem_type: str) -> str:
    """
    Recommends design patterns based on the problem described.
    """

    problem_type = problem_type.lower()

    if "database" in problem_type:
        return "Recommended Pattern: Repository Pattern"

    if "ui" in problem_type or "interface" in problem_type:
        return "Recommended Pattern: MVC or MVVM"

    if "object creation" in problem_type:
        return "Recommended Pattern: Factory Pattern"

    if "algorithm" in problem_type:
        return "Recommended Pattern: Strategy Pattern"

    return "Recommended Pattern: Adapter or Facade (general purpose)"
