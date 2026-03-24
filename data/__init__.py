"""Registre central de toutes les technologies."""

from data.languages import TECHNOLOGIES as LANG
from data.frontend import TECHNOLOGIES as FRONT
from data.backend import TECHNOLOGIES as BACK
from data.mobile import TECHNOLOGIES as MOBILE
from data.databases import TECHNOLOGIES as DB
from data.desktop import TECHNOLOGIES as DESK
from data.devops import TECHNOLOGIES as DEVOPS
from data.game_engines import TECHNOLOGIES as GAME
from data.ml import TECHNOLOGIES as ML
from data.messaging import TECHNOLOGIES as MSG

# Registre par nom de categorie (pour le navigateur)
REGISTRY = {
    "Langages de Programmation": LANG,
    "Frameworks Frontend Web": FRONT,
    "Frameworks Backend Web": BACK,
    "Developpement Mobile": MOBILE,
    "Bases de Donnees": DB,
    "Frameworks Desktop": DESK,
    "Outils DevOps": DEVOPS,
    "Moteurs de Jeu": GAME,
    "Frameworks ML / IA": ML,
    "Message Queues / Streaming": MSG,
}


def get_all_technologies():
    """Retourne un dict plat de toutes les technologies par id."""
    all_tech = {}
    for category_techs in REGISTRY.values():
        all_tech.update(category_techs)
    return all_tech


def get_technology(tech_id):
    """Recherche une technologie par id dans toutes les categories."""
    for category_techs in REGISTRY.values():
        if tech_id in category_techs:
            return category_techs[tech_id]
    return None
