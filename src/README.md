# 🔧 Code source réutilisable

Ce dossier contient les fonctions Python réutilisables pour l'analyse IPO.

## 📝 Fichiers

### analysis.py
Fonctions utilitaires pour :
- Chargement et fusion de données
- Calcul d'underpricing
- Calcul de rendements
- Nettoyage et validation des données
- Tests statistiques
- Génération de graphiques

---

## 🚀 Utilisation

### Dans un notebook
```python
from src.analysis import (
    load_and_merge_data,
    calculate_underpricing,
    calculate_returns,
    test_mann_whitney,
    plot_results
)

# Charger et fusionner les données
df = load_and_merge_data(
    dataset_path="../data/raw/dataset.xlsx",
    ipo_age_path="../data/raw/IPO-age.xlsx",
    daily_returns_path="../data/raw/daily_returns_cache.csv",
    offer_prices_path="../data/raw/offer_prices_from_sec.xlsx"
)

# Calculer l'underpricing
df['underpricing'] = calculate_underpricing(df)

# Calculer rendements 30j et 12m
df['return_30d'] = calculate_returns(df, days=30)
df['return_12m'] = calculate_returns(df, days=365)

# Test statistique
stat, pval = test_mann_whitney(df[df['cohorte'] == '2019-2021']['underpricing'],
                               df[df['cohorte'] == '2022-2024']['underpricing'])
print(f"Mann-Whitney U: stat={stat}, p-value={pval}")
```

---

## 📚 Conventions

### Nommage des fonctions
- `load_*()` : Charger des données
- `calculate_*()` : Calculer une métrique
- `test_*()` : Tests statistiques
- `plot_*()` : Créer des graphiques
- `clean_*()` : Nettoyer/valider des données

### Formats de date
- Format interne : `YYYY-MM-DD`
- Format d'affichage : `%d/%m/%Y` (français)

### Unités
- **Capital** : Millions USD
- **Prix** : USD par action
- **Rendements** : Pourcentages (%)
- **Taux FED** : Pourcentages annuels

---

## 🧪 Tests

*(À ajouter si besoin)*

Créer un fichier `test_analysis.py` avec :
```python
import pytest
from src.analysis import calculate_underpricing, calculate_returns

def test_calculate_underpricing():
    # Test case 1: Underpriced IPO
    result = calculate_underpricing(open=100, close=110)
    assert result == 10.0
    
    # Test case 2: Overpriced IPO
    result = calculate_underpricing(open=100, close=90)
    assert result == -10.0
```

Lancer :
```bash
pytest src/test_analysis.py -v
```

---

## 📦 Importer dans d'autres notebooks

Pour utiliser `src/analysis.py` dans un notebook de `notebooks/exploration/` :

```python
import sys
sys.path.insert(0, '../..')  # Ajouter la racine au path

from src.analysis import *
```

Ou plus simple :
```python
# Depuis notebooks/exploration/my_notebook.ipynb
from src.analysis import load_and_merge_data, calculate_underpricing
```

---

## 🔄 Workflow d'ajout de fonction

1. Créer la fonction dans `analysis.py`
2. Ajouter docstring détaillée
3. Tester dans un notebook d'exploration
4. Si OK, la documenter ici
5. Intégrer dans MAIN_ANALYSIS.ipynb si pertinent

---

## 📌 Points importants

- ✅ Garder les fonctions **génériques** et réutilisables
- ✅ Ajouter des **docstrings** pour chaque fonction
- ✅ Utiliser des **type hints** (Python 3.9+)
- ✅ Tester avant d'intégrer dans MAIN_ANALYSIS
- ❌ Ne pas hardcoder de chemins de fichiers
- ❌ Ne pas dépendre d'une variable globale
