# Simplon_MLOps

![CI Status](https://github.com/KiykoHanna/Simplon_MLOPS/actions/workflows/ci.yml/badge.svg)
[![Coverage](https://img.shields.io/badge/coverage-76%25-brightgreen)](https://github.com/KiykoHanna/Simplon_MLOPS)
[![Lint](https://img.shields.io/badge/lint-passing-brightgreen)](https://github.com/KiykoHanna/Simplon_MLOPS)
---

## Description

Simplon_MLOps est un template de projet professionnel pour le Machine Learning et MLOps.  

Il inclut :

- Une structure de code organisée (`app_api/`, `app_front/`, `tests/`, `docs/`)  
- Des docstrings standardisées et génération automatique de documentation avec Sphinx  
- CI/CD automatisé via GitHub Actions  
- Gestion reproductible des dépendances avec `uv`

---

## Installation

1. Cloner le dépôt:

```bash
git clone https://github.com/KiykoHanna/Simplon_MLOPS.git
cd Simplon_MLOPS
```

2. Installer uv (si non installé):

```bash
pip install uv
```

3. Synchroniser les dépendances:

```bash
uv sync
```

4. **Vérification le lancement de l’application**

```bash
# Lancer le backend (API)
uvicorn app_api.main:app

# Lancer le frontend
streamlit run app_front.main.py

## Exécution des tests
uv run pytest

# vérifier le code et l’auto-formatage:
uv run ruff check .
uv run ruff format .
```
---

## Contributeurs

Hanna Kiyko — Developper en IA

---

## Documentation et règles du projet

[Doumentation](https://kiykohanna.github.io/Simplon_MLOPS/)

4. **Code de conduite** : [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)  
5. **Contributing** : [CONTRIBUTING.md](CONTRIBUTING.md)  
6. **Licence** : [LICENSE](LICENSE)

---

## 5. Structure du projet 

```plaintext
.
├── .github/
│   ├── workflows/
│   │   ├── ci.yml         # Linting, Tests, Gitleaks
│   │   └── cd.yml         # Build & Push DockerHub
│   ├── CONTRIBUTING.md
│   └── CODE_OF_CONDUCT.md
├── app_front/             # Service Streamlit
│   ├── main.py
│   ├── pages
│   │   ├── 0_insert.py
│   │   └── 1_read.py  
│   ├── pyproject.toml
│   ├── uv.lock
│   └── Dockerfile
├── app_api/               # Service FastAPI
│   ├── Dockerfile
│   ├── pyproject.toml
│   ├── uv.lock
│   ├── models/            # Dossier contenant le modèle pydantic
│   │   ├── __init__.py
│   │   └── models.py      # modèle pydantic
│   ├── modules/           # Dossier contenant la logique du projet 1
│   │   ├── __init__.py
│   │   ├── connect.py     # Contient les operations de connexion et de CRUD
│   │   └── crud.py        # Contient les operations de CRUD
│   ├── maths/             # Dossier contenant la logique du projet 1
│   │   ├── __init__.py
│   │   └── mon_module.py  # Contient les fonctions add, sub, square, print_data
│   ├── data/              # Dossier contenant les data du projet 1
│   │   └── moncsv.csv     # Données d'entrée pour la démonstration
│   └── main.py            # Point d'entrée de l'application
├── tests/
│   ├── test_api.py
│   └── test_math_csv.py   
├── docker-compose.yml         # Pour le développement (build: .)
├── docker-compose.prod.yml    # Pour la prod (image: user/repo:tag)
├── conftest.py
├── .gitignore
├── .dockerignore
└── .env.example
 

```

---