# 🎯 PAR OÙ COMMENCER? — GUIDE D'ORIENTATION

## 🚀 Selon vos besoins

### 📖 "Je veux comprendre le projet"

**Lire dans cet ordre** (20-30 min de lecture):
1. ⭐ **[RECAP.md](RECAP.md)** — Résumé synthétique de la réorganisation
2. **[README.md](README.md)** — Vue d'ensemble complète du projet IPO
3. **[docs/README.md](docs/README.md)** — Méthodologie détaillée avec formules
4. **[STRUCTURE.md](STRUCTURE.md)** — Vue visuelle des dossiers

**Vous saurez alors** : Objectifs du projet, hypothèses testées, méthodologie, résultats attendus

---

### 🔬 "Je veux exécuter l'analyse"

**Suivre ces étapes** (5 min + 2-3 min d'exécution):

```bash
# 1. Installer les dépendances
pip install -r requirements.txt

# 2. Lancer Jupyter
jupyter notebook results/MAIN_ANALYSIS.ipynb

# 3. Dans Jupyter: Kernel → Restart & Run All

# 4. Attendre ~2-3 minutes
# Les résultats s'affichent progressivement

# 5. Vérifier les fichiers générés:
# - results/figures/*.png  (graphiques)
# - results/tables/*.csv   (tableaux)
```

**Résultat** : Tous les graphiques et statistiques régénérés

---

### ➕ "Je veux ajouter une nouvelle analyse"

**Procédure** (10-15 min):

1. **Créer un nouveau notebook**
   ```bash
   # Créer dans le dossier exploration/
   notebooks/exploration/my_hypothesis.ipynb
   ```

2. **Copier le template** (du début de MAIN_ANALYSIS.ipynb):
   ```python
   # Imports
   import pandas as pd
   import numpy as np
   from pathlib import Path
   
   # Charger les données
   df = pd.read_excel("../data/raw/dataset.xlsx")
   # ... (fusionner avec les autres fichiers)
   
   # Votre analyse ici
   ```

3. **Tester localement** dans votre notebook

4. **Si validé** : Intégrer dans `results/MAIN_ANALYSIS.ipynb`

**Voir aussi** : [notebooks/README.md](notebooks/README.md) — Workflow détaillé

---

### 🚀 "Je veux pousser sur GitHub"

**Checklist pré-push** (10 min):

- [ ] Lire [NOTICE.md](NOTICE.md) complètement
- [ ] Exécuter `results/MAIN_ANALYSIS.ipynb` (vérifier 0 erreur)
- [ ] Vérifier fichiers générés dans `results/figures/` et `results/tables/`
- [ ] Commiter les changements:
  ```bash
  git add .
  git commit -m "refactor: Réorganisation complète du projet IPO"
  ```
- [ ] Pousser:
  ```bash
  git push origin main
  ```

**Résultat** : Projet visible sur GitHub, prêt pour portfolio

---

### 📊 "Je veux extraire les résultats pour un rapport"

**Fichiers à copier**:

```
Du dossier:          Vers votre rapport:
results/figures/     → Graphiques (PNG, PDF)
results/tables/      → Tableaux (CSV, Excel)
docs/Livrable2.pdf   → Rapport complet
```

**Ou** exporter directement depuis `results/MAIN_ANALYSIS.ipynb`:
- Copier les cellules de résultats
- Exporter en PDF (Jupyter menu)

**Voir aussi** : [results/README.md](results/README.md) — Description complète

---

## 🗺️ Carte mentale des fichiers

```
Débutant?           → RECAP.md → README.md → docs/README.md
Cherche la structure? → STRUCTURE.md
Veut exécuter?      → NOTICE.md → requirements.txt → results/MAIN_ANALYSIS.ipynb
Veut contribuer?     → notebooks/README.md → notebooks/exploration/
Veut les données?    → data/raw/README.md
Veut du code?        → src/README.md
Veut tout savoir?    → Lire TOUS les README.md
```

---

## 📚 Index complet des fichiers de documentation

### 📄 Racine (5 fichiers)
| Fichier | Contenu | Audience |
|---------|---------|----------|
| **README.md** | Vue d'ensemble du projet | Tous |
| **RECAP.md** | Résumé de la réorganisation | Débutants |
| **NOTICE.md** | Instructions pour le push | Développeurs |
| **STRUCTURE.md** | Carte visuelle des dossiers | Tous |
| **requirements.txt** | Dépendances Python | Développeurs |

### 📚 Sous-dossiers (6 fichiers README)
| Dossier | Fichier | Contenu |
|---------|---------|---------|
| `data/raw/` | README.md | Description fichiers données |
| `notebooks/` | README.md | Workflow notebooks |
| `results/` | README.md | Guide résultats & graphiques |
| `docs/` | README.md | Méthodologie & formules |
| `src/` | README.md | Code réutilisable |
| `_archive_old/` | README.md | Info sur archives |

### 📓 Notebook
| Fichier | Localisation | Statut |
|---------|-------------|--------|
| **MAIN_ANALYSIS.ipynb** | results/ | ⭐ UTILISEZ CELUI-CI |
| Anciens notebooks | notebooks/archive/ | 🗂️ Référence seulement |

---

## 💡 Cas d'usage typiques

### Cas 1: Juste regarder les résultats
```
Temps: 5 min
Lire: docs/Livrable2.pdf
Voir: results/figures/*.png
```

### Cas 2: Comprendre et reproduire
```
Temps: 30 min
Lire: README.md + docs/README.md
Exécuter: results/MAIN_ANALYSIS.ipynb (Restart & Run All)
Vérifier: Pas d'erreur, graphiques générés
```

### Cas 3: Modifer ou ajouter analyses
```
Temps: 1-2h
Lire: notebooks/README.md + src/README.md
Créer: notebooks/exploration/my_analysis.ipynb
Tester: Exécuter le notebook
Intégrer: Merger dans MAIN_ANALYSIS si c'est bon
```

### Cas 4: Pousser sur GitHub
```
Temps: 15 min
Lire: NOTICE.md
Tester: results/MAIN_ANALYSIS.ipynb
Commiter: git add . && git commit -m "..."
Pousser: git push
```

---

## 🎯 Vue d'ensemble rapide

```
Projet: Analyse IPO (Initial Public Offerings) 2019-2024
Objectif: 4 hypothèses sur underpricing & rendements
Données: 4 sources Excel/CSV fusionnées
Analyse: 1 notebook complet (MAIN_ANALYSIS.ipynb)
Résultats: 100+ graphiques, tableaux statistiques
Documentation: 10 fichiers README

État: ✅ Prêt pour GitHub
```

---

## 🆘 Questions fréquentes

**Q: Par quel fichier je commence?**  
R: Si nouveau projet → RECAP.md, puis README.md. Si vous voulez exécuter → NOTICE.md.

**Q: Comment lancer l'analyse?**  
R: `pip install -r requirements.txt` puis `jupyter notebook results/MAIN_ANALYSIS.ipynb`

**Q: Je dois modifier les données?**  
R: Non! Les données dans `data/raw/` ne doivent jamais être modifiées. Créer des données traitées dans `data/processed/` si besoin.

**Q: Je peux exécuter les anciens notebooks?**  
R: Non, ils sont archivés. Utilisez `results/MAIN_ANALYSIS.ipynb` qui est le seul maintenu.

**Q: Comment ajouter une analyse?**  
R: Créer `notebooks/exploration/my_analysis.ipynb`, puis intégrer dans MAIN_ANALYSIS si validé.

**Q: C'est bon pour GitHub?**  
R: Oui! Structure professionnelle, bien documentée, prête pour le push. Voir NOTICE.md pour les dernières étapes.

---

## 🚀 Vous êtes prêt!

Choisissez votre prochaine action:

1. **Débutant** → Lire [RECAP.md](RECAP.md)
2. **Développeur** → Lire [NOTICE.md](NOTICE.md)  
3. **Data scientist** → Exécuter `jupyter notebook results/MAIN_ANALYSIS.ipynb`
4. **Portfolio** → Consulter `docs/Livrable2.pdf` + images

---

**Document créé** : Mai 2026  
**Projet** : Réorganisation complète terminée ✅
