# 📦 Archive des anciennes versions

Ce dossier contient tous les fichiers et dossiers de l'ancienne structure du projet, conservés à titre historique.

## Contenu

### Dossiers archivés :
- **`final/`** - Ancienne structure avec le notebook final précédent
- **`images/` & `images_finales/`** - Images générées (ancien système)
- **`outputs/`** - Fichiers de sortie anciens
- **`rapport/`** - Sources LaTeX du rapport (ancien)

### Fichiers archivés :
Les anciens notebooks Jupyter de travail ont été déplacés vers `notebooks/archive/` :
- `H1.ipynb`, `H2.ipynb`, `H3.ipynb`, `H4.ipynb`
- `hypothèse1.ipynb`, `test.ipynb`, `v1.ipynb`, `v2.ipynb`, `v3.ipynb`
- etc.

---

## ⚠️ À ne pas utiliser

**Ne faites pas référence à ces fichiers dans le code actuel.**

Le projet utilise maintenant :
- ✅ Notebook principal : `results/MAIN_ANALYSIS.ipynb`
- ✅ Données brutes : `data/raw/`
- ✅ Figures : `results/figures/`
- ✅ Notebooks de travail : `notebooks/exploration/` ou `notebooks/analysis/`

---

## 🗑️ Suppression sûre

Vous pouvez supprimer ce dossier sans risque une fois assuré que:
- Le notebook `results/MAIN_ANALYSIS.ipynb` fonctionne correctement
- Tous les fichiers de données utilisés sont dans `data/raw/`
- Les figures générées sont dans `results/figures/`
