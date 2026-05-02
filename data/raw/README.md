# 📊 Données brutes (Raw Data)

Ce dossier contient l'ensemble des fichiers de données brutes nécessaires pour l'analyse IPO.

## 📋 Fichiers utilisés (Principaux)

| Fichier | Description | Format | Utilisation |
|---------|------------|--------|------------|
| **dataset.xlsx** | Données IPO principales (2019-2024) | Excel | Source de base (tickers, secteurs, capitalisations, etc.) |
| **IPO-age.xlsx** | Informations temporelles IPO | Excel | Dates IPO, âge des entreprises |
| **offer_prices_from_sec.xlsx** | Prix d'offre SEC (reference) | Excel | Référence de prix pour H3 & H4 |
| **daily_returns_cache.csv** | Historique rendements journaliers | CSV | Calcul rendements 30j et 12m |

## 📦 Fichiers de référence/test (Additionnels)

| Fichier | Description |
|---------|------------|
| **clean_h4.csv** | Sous-ensemble nettoyé pour H4 |
| **edgar_sectors.xlsx** | Nomenclature des secteurs |
| **fred_annual.xlsx** | Taux d'intérêt FED annuels |
| **fred_monthly.xlsx** | Taux d'intérêt FED mensuels |

## 🛠️ Fichiers intermédiaires (Versions alternatives)

Ces fichiers sont des variantes du dataset principal créées lors de l'exploration :

- `dataset_complet_final.xlsx`
- `dataset_complet_filled_corrige_IPO_age.xlsx`
- `dataset_complet_filled_v1.xlsx`
- `dataset_final_filtered.xlsx`
- `datasetv2.xlsx`
- `ipo_prices.csv`

⚠️ **À documenter** : Vérifier laquelle de ces variantes est réellement utilisée dans le notebook final.

---

## 🔄 Flux de données

```
dataset.xlsx
  ├─ → Fusion avec IPO-age.xlsx (clé: ticker)
  ├─ → Fusion avec offer_prices_from_sec.xlsx (clé: ticker)
  └─ → Fusion avec daily_returns_cache.csv (clé: ticker)
        ↓
    [Dataset consolidé en mémoire dans MAIN_ANALYSIS.ipynb]
        ↓
    results/figures/ ← Graphiques PNG générés
    results/tables/  ← Tableaux de résultats
```

---

## ✅ Checklist pour validation

- [ ] Tous les fichiers Excel et CSV sont lisibles
- [ ] Les clés de merge (ticker) sont présentes dans tous les fichiers
- [ ] Pas de doublons de tickers
- [ ] Les données couvrent bien la période 2019-2024
- [ ] Les rendements journaliers couvrent la période requise (+30j, +365j)

---

## 📝 Notes

- **Ne pas modifier** ces fichiers bruts
- En cas de changement de données, créer des fichiers dans `data/processed/`
- Documenter toute transformation de données dans le notebook
