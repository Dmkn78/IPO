# 📊 IPO Analysis Project — Underpricing & Performance Study (2019-2024)

## 📋 Overview

Ce projet analyse les **Initial Public Offerings (IPO)** cotées aux États-Unis sur la période **2019-2024**, en examinant le phénomène de **underpricing** (sous-évaluation initiale) et les rendements de court/moyen terme. L'analyse compare deux cohortes distinctes :
- **2019-2021** : Période post-COVID, marché haussier
- **2022-2024** : Période de resserrement monétaire et ralentissement économique

### 🎯 Objectifs de recherche

Quatre hypothèses principales sont testées :

| Hypothèse | Description | Métrique |
|-----------|------------|---------|
| **H1** | Le underpricing des IPO varie significativement entre les deux cohortes | Rendement J0 (Open → Close) |
| **H2** | Les entreprises de plus grande taille sont moins sous-évaluées | Corrélation capitalization × underpricing |
| **H3** | Les rendements à 30 jours diffèrent significativement entre cohortes | Return 30j (à partir offer price) |
| **H4** | Les rendements à 12 mois montrent des patterns distincts par secteur | Return 12m par secteur (offer price) |

---

## 📁 Structure du projet

```
IPO/
├── README.md                           # Ce fichier
├── .gitignore                          # Configuration Git
│
├── data/
│   ├── raw/                            # ⚠️ Données brutes originales
│   │   ├── dataset.xlsx                # Données principales IPO (2019-2024)
│   │   ├── IPO-age.xlsx                # Âge et info temporelles IPO
│   │   ├── offer_prices_from_sec.xlsx  # Prix d'offre SEC
│   │   ├── daily_returns_cache.csv     # Rendements journaliers
│   │   └── clean_h4.csv                # Sous-ensemble pour H4
│   │
│   └── processed/                      # Données nettoyées & prétraitées
│       ├── merged_dataset.csv
│       └── [fichiers intermédiaires]
│
├── src/
│   └── analysis.py                     # Fonctions réutilisables (merges, calculs)
│
├── notebooks/
│   ├── exploration/                    # 📖 Notebooks de tests & exploration
│   │   ├── hypothesis_testing.ipynb
│   │   ├── data_quality_check.ipynb
│   │   └── [autres explorations]
│   │
│   └── archive/                        # 🗂️ Anciens notebooks (non prioritaires)
│       ├── H1.ipynb
│       ├── H2.ipynb
│       ├── H3.ipynb
│       ├── H4.ipynb
│       └── [autres versions]
│
├── results/
│   ├── MAIN_ANALYSIS.ipynb             # ⭐ NOTEBOOK FINAL - Analyse complète
│   │
│   ├── figures/                        # 📊 Graphiques générés (PNG, PDF)
│   │   ├── h1_underpricing_*.png
│   │   ├── h2_correlation_*.png
│   │   ├── h3_returns_30d_*.png
│   │   ├── h4_sector_analysis_*.png
│   │   └── [autres visualisations]
│   │
│   └── tables/                         # 📋 Tableaux de résultats (CSV, Excel)
│       ├── hypothesis_tests.csv
│       ├── statistical_summary.csv
│       └── [résultats statistiques]
│
├── docs/
│   ├── rapport.pdf                     # Rapport final complet
│   └── methodology.md                  # Documentation méthodologie
│
└── requirements.txt                    # Dépendances Python
```

---

## 🔬 Méthodologie & Points clés

### 1️⃣ Diagnostic des merges
- **Clé de merge** : `ticker` (symbole boursier)
- **Fichiers fusionnés** : 4 sources (dataset, daily_returns, offer_prices, IPO-age)
- **Risques résiduels documentés** : Non-correspondances et doublons identifiés

### 2️⃣ Calcul du underpricing (H1 & H2)
```
Underpricing = (Close J0 - Open J0) / Open J0
```
- **H1** : Comparaison Mann-Whitney U + tests de proportion entre cohortes
- **H2** : Régression OLS simple : underpricing ~ log(capital_raised)

### 3️⃣ Rendements à 30j (H3)
```
Return 30j (offer) = (Price J30 - Offer Price) / Offer Price
Return 30j (close)  = (Price J30 - Close J0) / Close J0
```
- Deux approches conservées pour comparaison robustesse
- Statistiques par secteur & cohorte

### 4️⃣ Rendements à 12m (H4)
```
Return 12m (offer) = (Price J365 - Offer Price) / Offer Price
Return 12m (close)  = (Price J365 - Close J0) / Close J0
```
- Analyse sectorielle (camemberts, boîtes à moustaches, moyennes/médianes)
- Tests Mann-Whitney U par secteur

### Cohortes
- **2019-2021** : Code couleur `#2C7BB6` (bleu)
- **2022-2024** : Code couleur `#D7191C` (rouge)

---

## 🚀 Quick Start

### Prérequis
```bash
Python 3.10+
pip install -r requirements.txt
```

### Lancer l'analyse complète
1. **Ouvrir le notebook principal** : `results/MAIN_ANALYSIS.ipynb`
2. **Exécuter les cellules** dans l'ordre (2. → 3. → ... → 67.)
3. Les graphiques sont sauvegardés dans `results/figures/`
4. Les résultats sont affichés à chaque hypothèse

### Ou : Reproductibilité complète
```bash
# Depuis le répertoire racine
jupyter notebook results/MAIN_ANALYSIS.ipynb
```

---

## 📊 Résultats clés

*(À remplir après exécution du notebook)*

### H1 : Underpricing par cohorte
- **2019-2021** : Moyenne ±IC95
- **2022-2024** : Moyenne ±IC95
- **Test MW** : p-value, conclusion

### H2 : Impact capitalization
- **Coefficient** : Magnitude & signe
- **R²** : Force du modèle
- **Conclusion** : Relation positive/négative/nulle ?

### H3 : Rendements 30j
- **Médiane 2019-2021** : X%
- **Médiane 2022-2024** : Y%
- **Différence** : Significative ?

### H4 : Rendements 12m par secteur
- **Top 3 secteurs** (2019-2021) : Techno, Finance, Santé
- **Top 3 secteurs** (2022-2024) : [À déterminer]
- **Secteur "worst performer"** : [À déterminer]

---

## 🛠️ Technologies utilisées

| Stack | Détail |
|-------|--------|
| **Langage** | Python 3.10+ |
| **Data** | pandas, numpy, scipy |
| **Stats** | statsmodels (OLS, tests MW, proportions) |
| **Viz** | matplotlib, seaborn |
| **Format** | Jupyter Notebook, Excel, CSV |

---

## 📝 Sources de données

1. **dataset.xlsx** → Données principales IPO (ticker, secteur, capital, etc.)
2. **IPO-age.xlsx** → Dates & informations temporelles
3. **offer_prices_from_sec.xlsx** → Prix d'offre SEC (reference)
4. **daily_returns_cache.csv** → Historique rendements journaliers

**Période couverte** : Janvier 2019 – Décembre 2024
**Univers** : IPO US uniquement (excl. SPACs, DPOs)

---

## ⚠️ Limitations & notes méthodologiques

1. **Limitations résiduelles (documentées dans le notebook)** :
   - Non-correspondances partielles entre sources
   - Tickers dupliqués ou divergents
   - Trous dans les séries temporelles

2. **Choix analytiques** :
   - Alpha = 0.05 pour tous les tests statistiques
   - Mann-Whitney U (non-paramétrique) pour robustesse
   - Régression OLS simple pour H2 (justification dans notebook)

3. **Reproductibilité** :
   - SEED = 42 (pour jitter plots)
   - Versions packages figées dans requirements.txt
   - Chemins relatifs (`../data/...`) depuis `results/`

---

## 📌 Points importants

- ✅ **Notebook final** : `results/MAIN_ANALYSIS.ipynb` (seul fichier nécessaire)
- ✅ **Graphiques** : Auto-sauvegardés dans `results/figures/` lors de l'exécution
- ✅ **Données brutes** : Archivées dans `data/raw/` (ne pas modifier)
- ✅ **Notebooks anciens** : Archivés dans `notebooks/archive/` pour référence
- ⚠️ **Gitignore** : Les fichiers générés (`.png`, `.csv`) dans `results/` sont ignorés

---

## 🤝 Contribution & maintenance

**Auteur** : [Votre nom]  
**Dernier update** : Mai 2026  
**Contact** : [Email]

Pour ajouter des analyses :
1. Créer une branche `feature/your-analysis`
2. Ajouter le notebook dans `notebooks/exploration/`
3. Documenter dans ce README
4. Merger après révision

---

## 📞 Questions fréquentes

**Q: Où sont les résultats finaux ?**  
R: Dans `results/MAIN_ANALYSIS.ipynb` (exécution complète ~2-3 min)

**Q: Comment relancer l'analyse ?**  
R: `jupyter notebook results/MAIN_ANALYSIS.ipynb` puis Run All

**Q: Les anciens notebooks H1/H2/H3/H4 servent à quoi ?**  
R: Archivés pour référence historique. Le notebook final les remplace complètement.

**Q: Les images/tables sont manquantes ?**  
R: C'est normal après un clone. Exécutez le notebook principal pour les générer.

---

## 📄 Licence

[À préciser : MIT, CC-BY, propriétaire, etc.]

---

**Happy analyzing! 📈**
