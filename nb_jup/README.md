# 📓 Notebooks

## 📌 Organisation

```
notebooks/
├── analysis/          # Analyses supplémentaires / nouvelles hypothèses
├── exploration/       # Tests, prototypes, explorations
└── archive/          # Anciens notebooks de développement
```

---

## ⭐ Notebook Principal

👉 **Ne pas utiliser les notebooks dans ce dossier pour les résultats finaux.**

**Utiliser à la place :** `results/MAIN_ANALYSIS.ipynb`

---

## 📖 Notebooks d'exploration

Utilisez ce dossier pour :
- Tester de nouvelles hypothèses
- Explorer les données
- Prototyper des analyses
- Documenter votre processus de recherche

### Structure recommandée pour nouveaux notebooks

```python
# En-tête
"""
Titre : [Description brève]
Objectif : [Pourquoi ce notebook]
Données : [Sources utilisées]
Auteur : [Nom]
Date : [YYYY-MM-DD]
Statut : [Exploration / En cours / Finalisé]
"""

# Section 1: Import & Setup
import pandas as pd
import numpy as np
# ...

# Section 2: Load Data
df = pd.read_excel("../data/raw/dataset.xlsx")
# ...

# Section 3: Analysis
# ...

# Section 4: Visualization & Results
# ...
```

---

## 📦 Notebooks archivés

Les anciens notebooks (H1, H2, H3, H4, test, v1-v3, etc.) sont conservés dans `archive/` pour référence historique.

**Ces notebooks ne doivent pas être exécutés** car :
- ❌ Les chemins de données pointent vers des dossiers inexistants
- ❌ Certains graphiques utilisent des images en dur (pas générés)
- ❌ Ils représentent une ancienne structure de projet

---

## 🚀 Worklfow recommandé

1. **Lancer l'analyse principale** : `results/MAIN_ANALYSIS.ipynb`
2. **Pour tester quelque chose de nouveau** :
   - Créer `exploration/my_analysis.ipynb`
   - Copier les imports et le setup de MAIN_ANALYSIS
   - Documenter l'objectif en en-tête
3. **Si l'analyse est validée** :
   - La merger dans MAIN_ANALYSIS
   - Ou créer un notebook final dans `analysis/`
   - Archiver la version exploration

---

## 📋 Checklist avant commit

Avant de faire un commit avec un nouveau notebook :

- [ ] Le notebook s'exécute sans erreur
- [ ] Les imports sont déclarés au début
- [ ] Les chemins sont relatifs (`../data/raw/...`)
- [ ] Il y a un commentaire d'en-tête
- [ ] Les graphiques sont exécutés et visibles
- [ ] Pas de cell "In [*]" : tout a été exécuté
