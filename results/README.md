# 📊 Résultats de l'analyse IPO

## ⭐ Fichier Principal

👉 **MAIN_ANALYSIS.ipynb** — Le notebook de référence contenant :
- ✅ Diagnostic complet des merges
- ✅ Hypothèse 1 (H1) : Underpricing par cohorte
- ✅ Hypothèse 2 (H2) : Impact de la capitalisatio
- ✅ Hypothèse 3 (H3) : Rendements 30j
- ✅ Hypothèse 4 (H4) : Rendements 12m par secteur
- ✅ Conclusions et limitations

**Status** : ✅ Complet et exécutable  
**Durée d'exécution** : ~2-3 minutes  
**Dépendances** : Voir `requirements.txt`

---

## 📁 Structures des sous-dossiers

### `figures/`
Graphiques générés automatiquement à l'exécution de MAIN_ANALYSIS.ipynb

**Types de fichiers** :
- `h1_underpricing_*.png` — Boîtes à moustaches, distributions
- `h2_correlation_*.png` — Scatter plots, régressions OLS
- `h3_returns_30d_*.png` — Trajectoires, densités
- `h4_sector_analysis_*.png` — Camemberts, moyennes par secteur
- `h4_returns_12m_*.png` — Boîtes à moustaches, distributions

**Format** : PNG haute résolution (110 DPI)

### `tables/`
Tableaux de résultats statistiques

**Format** : CSV, Excel  
**Contenu** :
- Résumés statistiques par hypothèse
- P-values et tests statistiques
- Moyennes, médianes, IC95%

---

## 🔄 Workflow d'exécution

### Pour relancer l'analyse complète :

```bash
cd c:\Users\X515\Documents\GitHub\IPO
jupyter notebook results/MAIN_ANALYSIS.ipynb
```

Puis dans Jupyter :
1. Cliquer sur **Kernel** → **Restart & Run All**
2. Attendre la fin de l'exécution (~2-3 min)
3. Les graphiques et tableaux se remplissent automatiquement

### Résultat :
- ✅ Graphiques dans `results/figures/`
- ✅ Tables dans `results/tables/`
- ✅ Conclusions dans le notebook

---

## 📊 Organisation des graphiques par hypothèse

### H1 : Underpricing (2019-2021 vs 2022-2024)
```
h1_underpricing_boxplot.png        ← Boîtes à moustaches par cohorte
h1_underpricing_distribution.png   ← Distributions de densité
h1_underpricing_ic95.png           ← Intervalles de confiance
h1_underpricing_by_year.png        ← Évolution annuelle
```

### H2 : Impact capitalisatio
```
h2_correlation_scatter.png         ← Scatter plot (capital vs underpricing)
h2_regression_ols.png              ← Droite de régression
h2_coefficients.png                ← Coefficients avec IC95%
```

### H3 : Rendements 30 jours
```
h3_returns_30d_comparison.png      ← Boîtes à moustaches par cohorte
h3_returns_trajectory.png          ← Courbe de performance
h3_sector_returns.png              ← Par secteur
```

### H4 : Rendements 12 mois
```
h4_returns_12m_boxplot.png         ← Distribution complète
h4_sector_pie.png                  ← Répartition sectorielle
h4_sector_comparison.png           ← Moyennes par secteur
h4_fed_rate_comparison.png         ← Impact taux FED
h4_sector_heatmap.png              ← Heatmap secteur × performance
```

---

## 📋 Tableaux de résultats

### Statistical Summary
- Moyennes, médianes, écarts-types pour chaque hypothèse
- Statistiques par cohorte et secteur
- Tailles d'échantillon (n)

### Hypothesis Tests
- Test Mann-Whitney U (p-values)
- Test de proportions pour H1
- OLS Summary pour H2

### Secteur Analysis (H4)
- Moyennes/médianes par secteur et cohorte
- Effectifs par secteur
- Écarts entre cohortes

---

## ✅ Checklist après exécution

Après avoir exécuté MAIN_ANALYSIS.ipynb, vérifiez que :

- [ ] Aucune cellule n'a levé d'erreur
- [ ] Les imports ont tous fonctionné
- [ ] Les fichiers PNG sont présents dans `figures/`
- [ ] Les tableaux CSV/Excel sont dans `tables/`
- [ ] Les graphiques sont clairs et lisibles
- [ ] Les nombres de l'analyse correspondent à vos attentes

**Si un fichier manque** : L'exécution a peut-être échoué. Vérifiez les messages d'erreur dans le notebook.

---

## 🔗 Connexion avec le README principal

Pour plus de contexte sur :
- Le project complet : voir `../README.md`
- Méthodologie : voir `../docs/methodology.md`
- Données brutes : voir `../data/raw/README.md`

---

## 🚀 Comment utiliser les résultats

### Pour une présentation/rapport :
1. Copier les graphiques de `figures/` vers votre document
2. Ajouter les statistiques des tables
3. Inclure les conclusions du notebook

### Pour continuer l'analyse :
1. Utiliser les données du notebook MAIN_ANALYSIS comme base
2. Créer un nouveau notebook dans `notebooks/exploration/`
3. Référencer les variables de MAIN_ANALYSIS si besoin

### Pour archiver :
1. Si modifié : créer une version du notebook avec un suffixe (`_v2`, `_backup`)
2. Documenter les changements dans les comments de cellule
3. Considérer un merge dans MAIN_ANALYSIS si c'est une amélioration majeure
