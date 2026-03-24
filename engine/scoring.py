"""Moteur de recommandation: scoring, synergies et generation des resultats."""

from engine.questions import QUESTIONS, SYNERGIES, CATEGORY_NAMES


def compute_recommendations(answers, all_technologies):
    """
    Calcule les recommandations basees sur les reponses du questionnaire.

    Args:
        answers: dict {question_id: selected_value}
        all_technologies: dict {tech_id: tech_data} (toutes les technos)

    Returns:
        dict avec categories triees par score et stack recommandee
    """
    # Etape 1: Determiner les categories pertinentes
    relevant_cats = _get_relevant_categories(answers)

    # Etape 2: Calculer les scores de base
    scores, reasons = _apply_question_scores(answers, all_technologies)

    # Etape 3: Filtrer aux categories pertinentes AVANT les synergies
    relevant_techs = {tid for tid, t in all_technologies.items()
                      if t.get("category") in relevant_cats}

    # Etape 4: Appliquer les bonus de synergie (seulement entre technos pertinentes)
    scores = _apply_synergy_bonuses(scores, all_technologies, relevant_techs)

    # Etape 5: Grouper par categorie et filtrer
    category_scores = _group_by_category(scores, reasons, all_technologies, relevant_cats)

    # Etape 6: Normaliser les scores
    category_scores = _normalize_scores(category_scores)

    # Etape 7: Construire la stack recommandee
    stack = _build_stack(category_scores)

    return {
        "categories": category_scores,
        "stack": stack,
        "relevant_categories": relevant_cats,
    }


def _get_relevant_categories(answers):
    """Determine quelles categories sont pertinentes selon le type de projet."""
    project_type = answers.get("project_type", "web_app")

    for q in QUESTIONS:
        if q["id"] == "project_type":
            return q.get("relevant_categories", {}).get(
                project_type,
                ["language", "backend", "database", "devops"]
            )

    return ["language", "backend", "database", "devops"]


def _apply_question_scores(answers, all_technologies):
    """Premiere passe: applique les poids de chaque question."""
    scores = {tech_id: 0.0 for tech_id in all_technologies}
    reasons = {tech_id: [] for tech_id in all_technologies}

    for question in QUESTIONS:
        qid = question["id"]
        answer_value = answers.get(qid)
        if answer_value is None:
            continue

        weight_map = question.get("weight_map", {})
        answer_weights = weight_map.get(answer_value, {})

        for tech_id, delta in answer_weights.items():
            if tech_id in scores:
                scores[tech_id] += delta
                if delta >= 2:
                    reasons[tech_id].append(
                        _make_reason(qid, answer_value, delta)
                    )

    return scores, reasons


def _make_reason(question_id, answer_value, delta):
    """Genere une raison lisible pour un bonus de score."""
    reason_map = {
        "project_type": {
            "web_app": "Adapte aux applications web",
            "api": "Excellent pour les API",
            "mobile": "Adapte au developpement mobile",
            "desktop": "Bon choix pour le desktop",
            "cli": "Ideal pour les outils CLI",
            "data_ml": "Fort en data science / ML",
            "embedded": "Adapte aux systemes embarques",
            "game": "Utilise dans le jeu video",
        },
        "performance": {
            "low": "Favorise la productivite",
            "medium": "Bon equilibre performance/productivite",
            "high": "Haute performance",
            "extreme": "Performance extreme",
        },
        "team_size": {
            "solo": "Efficace en solo",
            "small": "Adapte aux petites equipes",
            "medium": "Bon pour equipes moyennes",
            "large": "Scale bien en grande equipe",
        },
        "deadline": {
            "prototype": "Prototypage rapide",
            "medium": "Bon rythme de dev",
            "long": "Maintenable a long terme",
            "none": "Investissement technique solide",
        },
        "scalability": {
            "single": "Simple a deployer",
            "horizontal": "Scalabilite horizontale",
            "massive": "Gestion de gros trafic",
        },
        "experience": {
            "beginner": "Accessible aux debutants",
            "intermediate": "Courbe d'apprentissage raisonnable",
            "advanced": "Tire parti de l'experience",
            "expert": "Plein potentiel pour les experts",
        },
        "type_safety": {
            "low": "Flexible et dynamique",
            "medium": "Typage modere",
            "high": "Bon typage statique",
            "critical": "Securite de type maximale",
        },
        "priority": {
            "dx": "Excellente experience developpeur",
            "community": "Grande communaute",
            "jobs": "Fort sur le marche de l'emploi",
            "cutting_edge": "Technologie de pointe",
            "stability": "Mature et stable",
        },
    }

    q_reasons = reason_map.get(question_id, {})
    return q_reasons.get(answer_value, f"{question_id}: {answer_value}")


def _apply_synergy_bonuses(scores, all_technologies, relevant_techs):
    """Deuxieme passe: bonus pour les technos qui marchent bien ensemble.
    Ne considere que les synergies entre technologies pertinentes avec un score minimum."""
    # Seuil: seules les technos avec un score significatif declenchent des synergies
    min_score = 5
    strong_relevant = {t for t in relevant_techs if scores.get(t, 0) >= min_score}

    for (tech_a, tech_b), bonus in SYNERGIES.items():
        if tech_a in strong_relevant and tech_b in strong_relevant:
            scores[tech_a] += bonus * 1.5
            scores[tech_b] += bonus * 1.5

    return scores


def _group_by_category(scores, reasons, all_technologies, relevant_categories):
    """Regroupe les scores par categorie et trie."""
    categories = {}

    for tech_id, tech_data in all_technologies.items():
        cat = tech_data.get("category", "unknown")
        if cat not in relevant_categories:
            continue

        if cat not in categories:
            categories[cat] = []

        score = scores.get(tech_id, 0)
        if score <= 0:
            continue

        categories[cat].append({
            "id": tech_id,
            "name": tech_data["name"],
            "score": score,
            "reasons": reasons.get(tech_id, []),
        })

    # Trier chaque categorie par score decroissant
    for cat in categories:
        categories[cat].sort(key=lambda x: x["score"], reverse=True)

    return categories


def _normalize_scores(category_scores):
    """Normalise les scores en pourcentage dans chaque categorie."""
    for cat, techs in category_scores.items():
        if not techs:
            continue
        max_score = techs[0]["score"]  # Deja trie
        if max_score > 0:
            for tech in techs:
                tech["normalized"] = (tech["score"] / max_score) * 100
        else:
            for tech in techs:
                tech["normalized"] = 0

    return category_scores


def _build_stack(category_scores):
    """Construit la stack recommandee (top 1 par categorie)."""
    stack = {}
    for cat, techs in category_scores.items():
        if techs:
            top = techs[0]
            stack[cat] = {
                "id": top["id"],
                "name": top["name"],
                "score": top["normalized"],
                "reasons": top["reasons"][:3],  # Top 3 raisons
            }
    return stack
