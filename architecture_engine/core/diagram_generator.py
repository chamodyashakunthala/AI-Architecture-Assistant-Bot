# architecture_engine/core/diagram_generator.py

def generate_ascii_diagram(diagram_type: str) -> str:
    """
    Generate basic ASCII diagrams for architecture visualization.
    """
    if diagram_type == "3-tier":
        return (
            "+------------------------+\n"
            "|    Presentation Layer  |\n"
            "+------------------------+\n"
            "            |\n"
            "+------------------------+\n"
            "|   Application Layer    |\n"
            "+------------------------+\n"
            "            |\n"
            "+------------------------+\n"
            "|       Data Layer       |\n"
            "+------------------------+"
        )

    if diagram_type == "client-server":
        return (
            "+-----------+      +-----------+\n"
            "|   Client  | ---> |  Server   |\n"
            "+-----------+      +-----------+"
        )

    return "Diagram type not recognized."

