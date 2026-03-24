# StackAdvisor

Outil CLI interactif pour choisir la stack technologique optimale selon les besoins d'un projet. Inclut une base de connaissances detaillee sur 47 technologies.

## Fonctionnalites

### Recommandation de Stack
Un questionnaire de 12 questions analyse tes besoins (type de projet, performance, scalabilite, equipe, deadline, deploiement...) et recommande une stack complete avec scores, raisonnement detaille et alternatives.

### Encyclopedie Technologique
Parcours librement la theorie de chaque technologie :
- Vue d'ensemble et philosophie
- Histoire et evolution
- Architecture interne
- Avantages et inconvenients
- Cas d'utilisation concrets
- Ecosysteme et outillage
- Entreprises utilisatrices
- Exemples de code idiomatiques
- Caracteristiques de performance
- Scores techniques (radar sur 8 axes)

### Comparateur
Compare deux technologies cote a cote sur 8 criteres : performance, vitesse de developpement, courbe d'apprentissage, ecosysteme, surete du typage, concurrence, securite memoire, scalabilite.

## Technologies couvertes (47)

| Categorie | Technologies |
|-----------|-------------|
| **Langages** | C, C++, Python, JavaScript, TypeScript, Rust, Go, Java, C#, Swift, Kotlin, Ruby, PHP, Elixir |
| **Frontend Web** | React, Vue.js, Angular, Svelte, Next.js |
| **Backend Web** | Express.js, Django, Flask, FastAPI, Spring Boot, Ruby on Rails, Laravel, Gin, Actix Web, Phoenix |
| **Mobile** | React Native, Flutter, SwiftUI, Jetpack Compose |
| **Bases de donnees** | PostgreSQL, MySQL, MongoDB, Redis, SQLite, Cassandra |
| **Desktop** | Electron, Tauri, Qt, GTK |
| **DevOps** | Docker, Kubernetes, Terraform, GitHub Actions |

## Utilisation

```bash
python3 main.py
```

Aucune dependance externe requise. Python 3.6+ suffit.

## Structure du projet

```
StackAdvisor/
├── main.py              # Point d'entree et mode comparaison
├── ui/
│   ├── colors.py        # Constantes ANSI et helpers
│   ├── terminal.py      # Primitives de rendu (menus, pagination, barres)
│   ├── questionnaire.py # Wizard de recommandation
│   └── browser.py       # Navigateur de theorie
├── engine/
│   ├── questions.py     # 12 questions avec poids de scoring et synergies
│   └── scoring.py       # Algorithme de recommandation (2 passes + synergies)
└── data/
    ├── __init__.py      # Registre central
    ├── languages.py     # 14 langages de programmation
    ├── frontend.py      # 5 frameworks frontend
    ├── backend.py       # 10 frameworks backend
    ├── mobile.py        # 4 plateformes mobile
    ├── databases.py     # 6 bases de donnees
    ├── desktop.py       # 4 frameworks desktop
    └── devops.py        # 4 outils DevOps
```

## Algorithme de recommandation

Le moteur fonctionne en deux passes :

1. **Scoring par questions** : chaque reponse attribue des points aux technologies selon des poids predetermines
2. **Bonus de synergie** : les technologies qui fonctionnent naturellement ensemble (ex: TypeScript + React + Next.js, Python + FastAPI + PostgreSQL) recoivent un bonus de coherence

Les resultats sont ensuite filtres par categories pertinentes selon le type de projet, normalises en pourcentage, et presentes avec le raisonnement detaille.
