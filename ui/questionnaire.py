"""Mode questionnaire: guide interactif pour recommander une stack."""

from ui.terminal import (
    clear_screen, print_header, print_section, print_menu,
    print_bar, print_bar_simple, press_enter,
)
from ui.colors import (
    colored, BOLD, DIM, BRIGHT_CYAN, BRIGHT_GREEN, BRIGHT_YELLOW,
    BRIGHT_WHITE, BRIGHT_MAGENTA, GREEN, YELLOW, RED, GRAY, CYAN,
)
from engine.questions import QUESTIONS, CATEGORY_NAMES
from engine.scoring import compute_recommendations


def run_questionnaire(all_technologies):
    """Lance le questionnaire interactif et affiche les resultats."""
    clear_screen()
    print_header("Assistant de Recommandation de Stack")
    print(colored("  Je vais te poser quelques questions pour determiner", DIM))
    print(colored("  la stack technologique optimale pour ton projet.", DIM))
    print()
    print(colored("  Tu peux revenir en arriere avec [b] a chaque question.", DIM))
    print()
    press_enter()

    # Collecter les reponses
    answers = _collect_answers()
    if answers is None:
        return  # L'utilisateur a quitte

    # Calculer les recommandations
    results = compute_recommendations(answers, all_technologies)

    # Afficher les resultats
    _display_results(results, all_technologies)

    return results


def _collect_answers():
    """Pose les questions et collecte les reponses. Retourne None si abandon."""
    answers = {}
    question_order = []  # Pour pouvoir revenir en arriere
    i = 0

    while i < len(QUESTIONS):
        q = QUESTIONS[i]
        clear_screen()

        # Progress bar
        progress = f"Question {i + 1}/{len(QUESTIONS)}"
        bar_filled = int((i / len(QUESTIONS)) * 30)
        bar_empty = 30 - bar_filled
        progress_bar = (
            colored("  ", DIM)
            + colored("█" * bar_filled, BRIGHT_GREEN)
            + colored("░" * bar_empty, DIM)
            + colored(f"  {progress}", GRAY)
        )
        print()
        print(progress_bar)
        print()

        options = [opt["label"] for opt in q["options"]]
        choice = print_menu(
            q["text"],
            options,
            allow_back=(i > 0),
            allow_quit=True,
        )

        if choice == "quit":
            return None
        elif choice == "back":
            if i > 0:
                i -= 1
                # Retirer la derniere reponse
                last_qid = QUESTIONS[i]["id"]
                answers.pop(last_qid, None)
            continue

        # Enregistrer la reponse
        selected = q["options"][choice - 1]
        answers[q["id"]] = selected["value"]
        i += 1

    return answers


def _display_results(results, all_technologies):
    """Affiche les resultats de la recommandation."""
    stack = results["stack"]
    categories = results["categories"]

    while True:
        clear_screen()
        print_header("STACK RECOMMANDEE")

        if not stack:
            print(colored("  Aucune recommandation ne correspond a tes criteres.", YELLOW))
            press_enter()
            return

        # Afficher la stack recommandee
        print(colored("  Voici la stack optimale pour ton projet :", BOLD, BRIGHT_WHITE))
        print()

        for cat, tech_info in stack.items():
            cat_display = CATEGORY_NAMES.get(cat, cat.title())
            name = tech_info["name"]
            score = tech_info["score"]

            # Barre de score
            bar_width = 25
            filled = int((score / 100) * bar_width)
            empty = bar_width - filled

            # Couleur selon le score
            if score >= 80:
                bar_color = BRIGHT_GREEN
            elif score >= 60:
                bar_color = BRIGHT_YELLOW
            else:
                bar_color = YELLOW

            bar = colored("█" * filled, bar_color) + colored("░" * empty, DIM)
            cat_fmt = colored(f"  {cat_display:<18}", BOLD, BRIGHT_CYAN)
            name_fmt = colored(f"{name:<20}", BOLD)
            score_fmt = colored(f" {score:.0f}%", bar_color)

            print(f"{cat_fmt} {name_fmt} [{bar}]{score_fmt}")

        print()
        print(colored("  " + "─" * 60, DIM))
        print()

        # Menu des actions
        actions = [
            "Voir le raisonnement detaille",
            "Voir les alternatives par categorie",
            "Voir les scores complets",
            "Retour au menu principal",
        ]

        choice = print_menu("Que veux-tu explorer ?", actions)

        if choice == 1:
            _display_reasoning(stack)
        elif choice == 2:
            _display_alternatives(categories)
        elif choice == 3:
            _display_full_scores(categories)
        elif choice == 4:
            return


def _display_reasoning(stack):
    """Affiche les raisons de chaque recommandation."""
    clear_screen()
    print_header("Pourquoi cette stack ?")

    for cat, tech_info in stack.items():
        cat_display = CATEGORY_NAMES.get(cat, cat.title())
        name = tech_info["name"]
        reasons = tech_info.get("reasons", [])

        print(colored(f"  {cat_display}: {name}", BOLD, BRIGHT_CYAN))

        if reasons:
            for reason in reasons:
                print(colored(f"    -> ", GREEN) + reason)
        else:
            print(colored("    -> Score global eleve pour tes criteres", GREEN))
        print()

    press_enter()


def _display_alternatives(categories):
    """Affiche les alternatives pour chaque categorie."""
    clear_screen()
    print_header("Alternatives par categorie")

    for cat, techs in categories.items():
        cat_display = CATEGORY_NAMES.get(cat, cat.title())
        print(colored(f"  {cat_display}", BOLD, BRIGHT_CYAN))
        print(colored("  " + "─" * 40, DIM))

        for i, tech in enumerate(techs[:5]):  # Top 5 max
            rank = i + 1
            name = tech["name"]
            score = tech.get("normalized", 0)

            if rank == 1:
                prefix = colored(f"    {rank}. ", BRIGHT_GREEN)
                name_fmt = colored(name, BOLD, BRIGHT_GREEN)
                badge = colored(" [RECOMMANDE]", BRIGHT_GREEN)
            elif rank == 2:
                prefix = colored(f"    {rank}. ", BRIGHT_YELLOW)
                name_fmt = colored(name, BRIGHT_YELLOW)
                badge = colored(" [ALTERNATIVE]", BRIGHT_YELLOW)
            else:
                prefix = colored(f"    {rank}. ", DIM)
                name_fmt = name
                badge = ""

            bar_w = 15
            filled = int((score / 100) * bar_w)
            empty = bar_w - filled
            bar = colored("█" * filled, CYAN) + colored("░" * empty, DIM)

            print(f"{prefix}{name_fmt:<20} [{bar}] {score:.0f}%{badge}")

        print()

    press_enter()


def _display_full_scores(categories):
    """Affiche tous les scores detailles."""
    clear_screen()
    print_header("Scores complets")

    for cat, techs in categories.items():
        cat_display = CATEGORY_NAMES.get(cat, cat.title())
        print(colored(f"  {cat_display}", BOLD, BRIGHT_CYAN))
        print()

        for tech in techs:
            name = tech["name"]
            score = tech.get("normalized", 0)
            raw = tech.get("score", 0)

            bar_w = 25
            filled = int((score / 100) * bar_w)
            empty = bar_w - filled

            if score >= 80:
                bar_color = BRIGHT_GREEN
            elif score >= 50:
                bar_color = BRIGHT_YELLOW
            else:
                bar_color = DIM

            bar = colored("█" * filled, bar_color) + colored("░" * empty, DIM)
            print(f"    {name:<20} [{bar}] {score:.0f}% (raw: {raw:.1f})")

        print()

    press_enter()
