"""Mode navigation: parcourir la theorie de chaque technologie."""

from ui.terminal import (
    clear_screen, print_header, print_section, print_menu,
    print_paginated, print_pros_cons, print_bar, press_enter,
)
from ui.colors import colored, BOLD, BRIGHT_CYAN, BRIGHT_YELLOW, BRIGHT_GREEN, DIM, GREEN, RED, GRAY


def run_browser(registry):
    """Lance le mode navigation des technologies."""
    while True:
        clear_screen()
        print_header("Parcourir les Technologies")

        cat_names = list(registry.keys())
        choice = print_menu(
            "Choisis une categorie",
            cat_names,
            allow_quit=True,
        )

        if choice == "quit":
            return

        cat_name = cat_names[choice - 1]
        techs = registry[cat_name]

        if not _browse_category(cat_name, techs):
            continue


def _browse_category(cat_name, techs):
    """Parcourt les technos d'une categorie. Retourne False pour remonter."""
    while True:
        clear_screen()
        print_header(cat_name)

        tech_names = [f"{t['name']} ({t.get('year_created', '?')})" for t in techs.values()]
        tech_ids = list(techs.keys())

        choice = print_menu(
            "Choisis une technologie",
            tech_names,
            allow_back=True,
        )

        if choice == "back":
            return False

        tech_id = tech_ids[choice - 1]
        tech = techs[tech_id]

        if not _browse_technology(tech):
            continue

    return True


def _browse_technology(tech):
    """Affiche les sections d'une techno. Retourne False pour remonter."""
    sections_menu = [
        ("overview", "Vue d'ensemble"),
        ("history", "Histoire et evolution"),
        ("architecture", "Architecture et philosophie"),
        ("pros_cons", "Avantages et inconvenients"),
        ("use_cases", "Cas d'utilisation"),
        ("ecosystem", "Ecosysteme et outils"),
        ("companies", "Entreprises utilisatrices"),
        ("code_example", "Exemple de code"),
        ("performance", "Caracteristiques de performance"),
        ("learning_meta", "Apprentissage et marche"),
        ("traits", "Scores techniques (radar)"),
    ]

    while True:
        clear_screen()
        _print_tech_header(tech)

        menu_labels = [s[1] for s in sections_menu]
        choice = print_menu(
            "Choisis une section",
            menu_labels,
            allow_back=True,
        )

        if choice == "back":
            return False

        section_key = sections_menu[choice - 1][0]
        section_label = sections_menu[choice - 1][1]
        _display_section(tech, section_key, section_label)

    return True


def _print_tech_header(tech):
    """Affiche l'en-tete resume d'une technologie."""
    name = tech.get("name", "?")
    year = tech.get("year_created", "?")
    creator = tech.get("creator", "?")
    paradigm = ", ".join(tech.get("paradigm", []))
    typing = tech.get("typing", "?")

    print(colored(f"  {name}", BOLD, BRIGHT_CYAN) + colored(f"  ({year})", DIM))
    print(colored(f"  Cree par: ", GRAY) + creator)
    print(colored(f"  Paradigme: ", GRAY) + paradigm)
    print(colored(f"  Typage: ", GRAY) + typing)
    print()


def _display_section(tech, section_key, section_label):
    """Affiche une section specifique d'une technologie."""
    sections = tech.get("sections", {})

    if section_key == "pros_cons":
        _display_pros_cons(tech, section_label)
    elif section_key == "companies":
        _display_companies(tech, section_label)
    elif section_key == "performance":
        _display_performance(tech, section_label)
    elif section_key == "learning_meta":
        _display_learning_meta(tech, section_label)
    elif section_key == "traits":
        _display_traits(tech, section_label)
    elif section_key == "code_example":
        _display_code(tech, section_label)
    elif section_key in sections:
        content = sections[section_key]
        if isinstance(content, str):
            print_paginated(f"{tech['name']} - {section_label}", content)
        else:
            print_paginated(f"{tech['name']} - {section_label}", str(content))
    else:
        clear_screen()
        print_header(f"{tech['name']} - {section_label}")
        print(colored("  Section non disponible.", RED))
        press_enter()


def _display_pros_cons(tech, label):
    """Affiche les avantages et inconvenients."""
    clear_screen()
    print_header(f"{tech['name']} - {label}")

    pros_cons = tech.get("sections", {}).get("pros_cons", {})
    pros = pros_cons.get("pros", [])
    cons = pros_cons.get("cons", [])

    print_pros_cons(pros, cons)
    press_enter()


def _display_companies(tech, label):
    """Affiche les entreprises utilisatrices."""
    clear_screen()
    print_header(f"{tech['name']} - {label}")

    companies = tech.get("sections", {}).get("companies", [])
    if companies:
        print(colored("  Entreprises notables utilisant " + tech["name"] + " :", BOLD))
        print()
        for i, company in enumerate(companies, 1):
            print(colored(f"    {i}. ", BRIGHT_YELLOW) + company)
    else:
        print(colored("  Pas d'information disponible.", DIM))
    print()
    press_enter()


def _display_performance(tech, label):
    """Affiche les caracteristiques de performance."""
    clear_screen()
    print_header(f"{tech['name']} - {label}")

    perf = tech.get("sections", {}).get("performance", {})
    if perf:
        print(colored("  Caracteristiques de performance :", BOLD))
        print()
        for key, value in perf.items():
            key_display = key.replace("_", " ").title()
            print(colored(f"    {key_display:<25}", BRIGHT_CYAN) + str(value))
    else:
        print(colored("  Pas d'information disponible.", DIM))
    print()
    press_enter()


def _display_learning_meta(tech, label):
    """Affiche les infos d'apprentissage et marche."""
    clear_screen()
    print_header(f"{tech['name']} - {label}")

    sections = tech.get("sections", {})
    info = {
        "Courbe d'apprentissage": sections.get("learning_curve", "N/A"),
        "Taille de la communaute": sections.get("community_size", "N/A"),
        "Marche de l'emploi": sections.get("job_market", "N/A"),
    }

    for key, value in info.items():
        print(colored(f"    {key:<30}", BRIGHT_CYAN) + str(value))

    print()
    press_enter()


def _display_traits(tech, label):
    """Affiche les scores techniques sous forme de barres."""
    clear_screen()
    print_header(f"{tech['name']} - {label}")

    traits = tech.get("traits", {})
    if traits:
        trait_labels = {
            "performance": "Performance",
            "developer_speed": "Vitesse de dev",
            "learning_curve": "Difficulte",
            "ecosystem_size": "Ecosysteme",
            "type_safety": "Surete du typage",
            "concurrency": "Concurrence",
            "memory_safety": "Securite memoire",
            "scalability": "Scalabilite",
        }

        print(colored("  Scores techniques (sur 10) :", BOLD))
        print()
        for trait_key, trait_value in traits.items():
            display_name = trait_labels.get(trait_key, trait_key)
            print_bar(display_name, trait_value, max_value=10)
    else:
        print(colored("  Pas de scores disponibles.", DIM))

    print()
    press_enter()


def _display_code(tech, label):
    """Affiche l'exemple de code."""
    clear_screen()
    print_header(f"{tech['name']} - {label}")

    code = tech.get("sections", {}).get("code_example", "")
    if code:
        print(colored("  Exemple de code :", BOLD))
        print()
        for line in code.strip().split("\n"):
            print(colored(f"    {line}", GREEN))
    else:
        print(colored("  Pas d'exemple disponible.", DIM))

    print()
    press_enter()
