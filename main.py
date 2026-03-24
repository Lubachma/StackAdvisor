#!/usr/bin/env python3
"""Stack Advisor - Guide interactif pour choisir ta stack technologique."""

import sys


def main():
    from ui.terminal import clear_screen, print_banner, print_menu, print_header
    from ui.colors import colored, DIM, BRIGHT_CYAN, BOLD
    from data import REGISTRY, get_all_technologies
    from ui.questionnaire import run_questionnaire
    from ui.browser import run_browser

    all_technologies = get_all_technologies()

    while True:
        print_banner()

        options = [
            "Recommandation de Stack (questionnaire guide)",
            "Parcourir les Technologies (theorie detaillee)",
            "Comparer deux technologies",
            "Quitter",
        ]

        choice = print_menu("Que veux-tu faire ?", options)

        if choice == 1:
            run_questionnaire(all_technologies)
        elif choice == 2:
            run_browser(REGISTRY)
        elif choice == 3:
            _compare_mode(all_technologies)
        elif choice == 4:
            clear_screen()
            print(colored("\n  A bientot ! Bonne chance avec ton projet.\n", BRIGHT_CYAN, BOLD))
            sys.exit(0)


def _compare_mode(all_technologies):
    """Mode comparaison entre deux technologies."""
    from ui.terminal import clear_screen, print_header, print_menu, print_bar, press_enter
    from ui.colors import colored, BOLD, DIM, BRIGHT_CYAN, BRIGHT_GREEN, BRIGHT_YELLOW, GRAY, RED

    clear_screen()
    print_header("Comparer deux Technologies")

    tech_list = sorted(all_technologies.keys())
    tech_names = [f"{all_technologies[t]['name']} ({all_technologies[t].get('category', '?')})" for t in tech_list]

    print(colored("  Premiere technologie :", BOLD))
    choice1 = print_menu("", tech_names, allow_back=True)
    if choice1 == "back":
        return

    print(colored("  Deuxieme technologie :", BOLD))
    choice2 = print_menu("", tech_names, allow_back=True)
    if choice2 == "back":
        return

    tech_a_id = tech_list[choice1 - 1]
    tech_b_id = tech_list[choice2 - 1]
    tech_a = all_technologies[tech_a_id]
    tech_b = all_technologies[tech_b_id]

    clear_screen()
    print_header(f"{tech_a['name']} vs {tech_b['name']}")

    traits_a = tech_a.get("traits", {})
    traits_b = tech_b.get("traits", {})

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

    all_traits = set(list(traits_a.keys()) + list(traits_b.keys()))

    print(colored(f"  {'Critere':<22} {tech_a['name']:<15} {tech_b['name']:<15} {'Gagnant'}", BOLD, DIM))
    print(colored("  " + "─" * 65, DIM))

    score_a = 0
    score_b = 0

    for trait in trait_labels:
        va = traits_a.get(trait)
        vb = traits_b.get(trait)
        label = trait_labels.get(trait, trait)

        # Skip si aucune des deux technos n'a ce trait
        if va is None and vb is None:
            continue

        # Gerer les traits manquants
        if va is None:
            va_display = colored("  N/A     ", DIM)
            vb_bar = colored("█" * vb + "░" * (10 - vb), BRIGHT_YELLOW)
            winner = colored(f"{tech_b['name']} >>", BRIGHT_YELLOW)
            score_b += 1
            print(f"  {label:<22} [{va_display}]        vs  [{vb_bar}] {vb}/10  {winner}")
            continue
        if vb is None:
            vb_display = colored("  N/A     ", DIM)
            va_bar = colored("█" * va + "░" * (10 - va), BRIGHT_GREEN)
            winner = colored(f"<< {tech_a['name']}", BRIGHT_GREEN)
            score_a += 1
            print(f"  {label:<22} [{va_bar}] {va}/10  vs  [{vb_display}]        {winner}")
            continue

        if va > vb:
            winner = colored(f"<< {tech_a['name']}", BRIGHT_GREEN)
            score_a += 1
        elif vb > va:
            winner = colored(f"{tech_b['name']} >>", BRIGHT_YELLOW)
            score_b += 1
        else:
            winner = colored("Egalite", DIM)

        va_bar = colored("█" * va + "░" * (10 - va), BRIGHT_GREEN if va >= vb else DIM)
        vb_bar = colored("█" * vb + "░" * (10 - vb), BRIGHT_YELLOW if vb >= va else DIM)

        print(f"  {label:<22} [{va_bar}] {va}/10  vs  [{vb_bar}] {vb}/10  {winner}")

    print()
    print(colored("  " + "─" * 65, DIM))
    print(colored(f"  Resultat: ", BOLD) +
          colored(f"{tech_a['name']} {score_a}", BRIGHT_GREEN) +
          colored(" - ", DIM) +
          colored(f"{score_b} {tech_b['name']}", BRIGHT_YELLOW))
    print()

    press_enter()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n")
        sys.exit(0)
