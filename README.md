# IPO Analysis Project

Projet d’analyse des IPO américaines entre 2019 et 2024.

Le travail porte principalement sur :
- l’underpricing au premier jour ;
- les rendements à court terme ;
- les rendements à 12 mois ;
- la comparaison entre les périodes 2019-2021 et 2022-2024.

## Structure du projet

```text
IPO/
├── README.md
├── .gitignore
├── requirements.txt
│
├── data/
│   ├── raw/
│   │   ├── dataset.xlsx
│   │   ├── IPO-age.xlsx
│   │   ├── offer_prices_from_sec.xlsx
│   │   ├── daily_returns_cache.csv
│   │   └── clean_h4.csv
│   │
│   └── processed/
│       ├── merged_dataset.csv
│       └── autres fichiers nettoyés
│
├── src/
│   └── analysis.py
│
├── notebooks/
│   ├── exploration/
│   │   ├── hypothesis_testing.ipynb
│   │   ├── data_quality_check.ipynb
│   │   └── autres notebooks de test
│   │
│   └── archive/
│       ├── H1.ipynb
│       ├── H2.ipynb
│       ├── H3.ipynb
│       ├── H4.ipynb
│       └── anciennes versions
│
├── results/
│   ├── MAIN_ANALYSIS.ipynb
│   │
│   ├── figures/
│   │   └── graphiques générés
│   │
│   └── tables/
│       └── tableaux de résultats
│
└── docs/
    ├── rapport.pdf
    └── methodology.md
