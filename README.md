# Simplon_MLOps

![CI Status](https://github.com/KiykoHanna/Simplon_MLOPS/actions/workflows/python-ci.yml/badge.svg)
![Python CI workflow status badge for main branch on GitHub](https://img.shields.io/github/actions/workflow/status/KiykoHanna/Simplon_MLOPS/python-ci.yml?branch=main&label=Coverage&style=flat-square)

---

## Description

Simplon_MLOps est un template de projet professionnel pour le Machine Learning et MLOps.  
Il inclut :

- Une structure de code organisée (`app/`, `tests/`, `docs/`)  
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

4. Vérifier le lancement de l’application:

```bash
uv run app
```
---
## Exécution des tests

```bash
uv run pytest
```

Pour vérifier le code et l’auto-formatage:

```bash
uv run ruff check .
uv run ruff format .
```
---
## Contributeurs

Hanna Kiyko — Developper en IA

---

## Documentation et règles du projet

4. **Code de conduite** : [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)  
5. **Contributing** : [CONTRIBUTING.md](CONTRIBUTING.md)  
6. **Licence** : [LICENSE](LICENSE)

---
## Structure du projet

```
.
├── app/                    # code source
├── tests/                  # tests unitaires et d’intégration
├── pyproject.toml           # gestion des dépendances (uv)
├── docs/                    # documentation Sphinx
├── uv.lock                  # lock file pour reproductibilité
├── README.md                # vitrine du projet
├── CONTRIBUTING.md          # guide de contribution
├── CODE_OF_CONDUCT.md       # code de conduite
└── LICENSE                  # droits d’utilisation
```

---