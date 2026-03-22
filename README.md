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

2. Créer le fichier .env à la racine :

```
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=mydb
API_PORT=8000
FRONT_PORT=8501
```

## Migration des données SQLite → PostgreSQL

```bash
docker-compose up -d postgres
docker exec -it api python /app/migrate.py
```

## Lancer le projet avec Docker Compose

1. Construire et lancer tous les services :

```bash
docker-compose up -d --build
```

2. Vérifier que les conteneurs sont actifs :

```bash
docker ps
```

## Tester l’API

Une fois que votre API est lancée via Docker (docker-compose up -d), ouvre votre navigateur et va à :
(http://localhost:8000/docs)

Tester les requêtes GET et POST directement depuis cette interface.

## Accéder au front (Streamlit)

- Dans le navigateur : (http://localhost:8501)
- Le front se connecte automatiquement à l’API "http://api:8000" via Docker Compose.
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

```
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
└── .env
 

```

---