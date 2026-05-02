# 📚 Documentation

## 📋 Fichiers du dossier

### Livrable2.pdf
**Rapport final complet** de l'analyse IPO  
- Résumé exécutif
- Méthodologie détaillée
- Résultats par hypothèse
- Discussions et limitations
- Conclusions

---

## 📖 Méthodologie

### Synthèse des 4 hypothèses

#### **H1 : Le underpricing varie entre 2019-2021 et 2022-2024**

**Définition du underpricing** :
```
Underpricing = (Close J0 - Open J0) / Open J0 × 100 %
```

**Méthodologie** :
- Test Mann-Whitney U (non-paramétrique) entre cohortes
- Test de proportion (% d'IPO en underpricing)
- Calcul d'intervalles de confiance 95%

**Cohortes** :
- 2019-2021 : Marché haussier post-COVID
- 2022-2024 : Resserrement monétaire & ralentissement

---

#### **H2 : Les grandes entreprises sont moins sous-évaluées**

**Formule** :
```
Underpricing = α + β × ln(Capital Raised) + ε
```

**Méthodologie** :
- Régression OLS simple
- Variable indépendante : log(capital levé)
- Variable dépendante : underpricing (%)
- Test de significativité du coefficient β

**Interprétation** :
- β > 0 → Les grandes entreprises sont moins sous-évaluées ✓
- β < 0 → Les grandes entreprises sont plus sous-évaluées ✗
- β ≈ 0 → Aucun effet de taille → Rejet H2

---

#### **H3 : Les rendements à 30 jours diffèrent par cohorte**

**Calcul des rendements** :
```
Return 30j = (Price J30 - Price Référence) / Price Référence × 100 %
```

Deux approches :
- **Offer price** : Rendement depuis le prix d'offre SEC (recommandé)
- **Close J0** : Rendement depuis la clôture du premier jour

**Méthodologie** :
- Test Mann-Whitney U entre cohortes
- Analyse par secteur
- Courbes de performance (trajectoires cumulées)

---

#### **H4 : Les rendements 12 mois montrent des patterns sectoriels**

**Calcul** :
```
Return 12m = (Price J365 - Price Référence) / Price Référence × 100 %
```

**Méthodologie** :
- Analyse sectorielle (11 secteurs)
- Boîtes à moustaches par secteur
- Moyennes/médianes par secteur et cohorte
- Heatmap secteur × performance
- Corrélation avec taux d'intérêt FED

**Secteurs** :
Energy, Materials, Industrials, Consumer Discretionary, Consumer Staples, Health Care, Financials, Information Technology, Communication Services, Real Estate, Utilities

---

## 🔬 Détails statistiques

### Tests utilisés

| Test | Quand | Null Hypothesis |
|------|-------|-----------------|
| **Mann-Whitney U** | Comparaison 2 cohortes | Les distributions sont identiques |
| **Régression OLS** | Relation linéaire | Le coefficient est nul (pas de relation) |
| **Test de proportion** | % d'IPO positives | Pas de différence de proportion entre cohortes |

### Seuil de significativité
- **α = 0.05** pour tous les tests
- **IC 95%** pour les intervalles de confiance
- **Two-tailed** pour tous les tests

---

## 📊 Variables clés

### Variables principales du dataset

| Variable | Description | Type | Source |
|----------|-------------|------|--------|
| `ticker` | Symbole boursier (ex: AAPL) | String | dataset |
| `date_ipo` | Date IPO | Date | IPO-age |
| `sector` | Secteur d'activité | String | dataset |
| `capital_raised` | Capital levé (en millions USD) | Float | dataset |
| `open_price` | Prix d'ouverture J0 | Float | dataset |
| `close_price` | Prix de clôture J0 | Float | dataset |
| `offer_price` | Prix d'offre SEC (reference) | Float | offer_prices |
| `price_30d` | Prix à J30 | Float | daily_returns |
| `price_365d` | Prix à J365 | Float | daily_returns |
| `cohorte` | 2019-2021 ou 2022-2024 | String | Calculée |

---

## 🔧 Détails techniques

### Reproducinctivité
- **Seed** : 42 (pour jitter plots)
- **DPI** : 110 (résolution des graphiques)
- **Format** : PNG sans compression (lossless)

### Dépendances Python
```
pandas >= 2.0.0      # Data manipulation
numpy >= 1.24.0      # Numerical computations
scipy >= 1.10.0      # Statistical tests
statsmodels >= 0.14  # OLS, Mann-Whitney U
matplotlib >= 3.7.0  # Plotting
seaborn >= 0.13.0    # Styled plots
```

---

## ⚠️ Limitations & Notes méthodologiques

1. **Data quality** :
   - Non-correspondances partielles entre sources
   - Tickers dupliqués (rare)
   - Trous dans les séries temporelles (jours de marché fermé, halts)

2. **Choix analytiques** :
   - Mann-Whitney U choisi pour robustesse (pas d'assumption de normalité)
   - Régression OLS simple pour H2 (peut être enrichie : variables de contrôle)
   - Analyse par secteur uniquement pour H4 (pas de contrôle par taille)

3. **Périodes couvertes** :
   - **IPO** : 2019-01-01 à 2024-12-31
   - **Rendements 30j** : Données jusqu'à J30 après IPO
   - **Rendements 12m** : Données jusqu'à J365 après IPO
   - **Taux FED** : Données annuelles/mensuelles correspondant aux IPO

---

## 🔗 Références croisées

- Voir aussi : `../README.md` (Overview du projet)
- Données brutes : `../data/raw/README.md`
- Notebooks : `../notebooks/README.md`
- Résultats : `../results/README.md`
