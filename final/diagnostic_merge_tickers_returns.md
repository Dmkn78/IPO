# Diagnostic des merges et stratégie retenue

## 1. Contexte

Le projet IPO compare deux cohortes (2019-2021 et 2022-2024) à partir de plusieurs fichiers sources. Les analyses précédentes ont reposé sur un merge ticker uniquement, ce qui pose un risque de mauvais appariement (tickers réutilisés après radiation, SPACs, IPO secondaires). Ce document récapitule le diagnostic et fixe la stratégie de merge utilisée dans le notebook corrigé.

## 2. Table de diagnostic

| Fichier | Lignes | Tickers uniques | Doublons ticker | CUSIP | Date d'IPO fiable |
|---|---|---|---|---|---|
| `dataset_4_.xlsx` | 407 | 407 | 0 | non | non (col `Date` mélange filing / IPO ancien) |
| `daily_returns_cache.csv` | 230 550 | 780 | 0 (par cohorte) | non | oui (min(date) par ticker) |
| `offer_prices_from_sec_1_.xlsx` | 318 | 318 | 0 | non | non (col `ipo_date` corrompue, `ipo_date_fmp` vide) |
| `IPO-age_2019_2024.xlsx` | 2 284 | 2 271 | 12 (10 tickers concernés) | oui (2 282/2 284) | oui (`offer date` au format YYYYMMDD) |

### 2.1 Recouvrements

| Croisement | Matches | Sur |
|---|---|---|
| `dataset_4` ∩ `daily_returns` | 406 | 407 |
| `dataset_4` ∩ `IPO-age` | 351 | 407 |
| `dataset_4` ∩ `offer_prices` | 258 | 407 |

- 1 ticker de `dataset_4` est absent de `daily_returns` : **HCWB**.
- 56 tickers de `dataset_4` sont absents de `IPO-age` (typiquement IPO arrivées après l'extraction d'IPO-age, SPACs ou émissions hors périmètre Ritter).

### 2.2 Doublons de ticker dans IPO-age

10 tickers correspondent à plusieurs entreprises (SPACs réutilisés). Aucun n'apparaît dans `dataset_4`, donc aucun risque de mauvais match côté `dataset_4`.

| Ticker | Nombre d'entreprises |
|---|---|
| HYACU | 3 |
| KCAC. | 3 |
| ACACU | 2 |
| ASPCU | 2 |
| GIGGU | 2 |
| LCAHU | 2 |
| MCACU | 2 |
| MLACU | 2 |
| NHICU | 2 |
| PANA | 2 |

### 2.3 Cinq exemples de lignes problématiques

**Exemple 1 — HCWB.** Présent dans `dataset_4` (year = 2021, OfferPrice = 8 $) mais absent de `daily_returns`. Le `close_px` rapporté (252 $) est incompatible avec un OfferPrice de 8 $ sans split ; aucune série de prix ne permet de recalculer ses rendements à 30 j ou 12 mois. → **observation exclue** des analyses H3/H4 avec justification.

**Exemple 2 — DOLE.** La colonne `Date` de `dataset_4` indique 2009-10-26, alors que `daily_returns` montre une 1ère cotation au 2021-07-30 et `IPO-age` confirme une « offer date » au 2021-07-30. La colonne `Date` de `dataset_4` n'est donc **pas** la date de 1ère cotation, c'est probablement une date de filing antérieur ou un IPO précédent (DOLE est un nouveau listing de Dole Plc en 2021). → conséquence : on ne peut pas se servir de `Date` comme date d'IPO. Pour les rendements, on utilise la 1ère cotation depuis `daily_returns`.

**Exemple 3 — DUO (Fangdd Network Group).** OfferPrice = 13 $, mais `close_px` = 46 800 $ dans `dataset_4`, ce qui produit un underpricing apparent de 3 599 (360 000 %). Cohérent avec les valeurs visibles dans `daily_returns` (toutes les lignes sont en milliers de dollars). C'est un effet d'ajustement post-split appliqué rétroactivement à la série de prix, alors que l'OfferPrice reste au prix d'IPO nominal. → idem ARBK (×241), BCAB (×86), COOK (×61), YJ (×51), KRRO (×49), BIRD (×38). Sept observations sont concernées par ce phénomène ; elles sont identifiées dans le notebook et documentées.

**Exemple 4 — Tickers réutilisés (HYACU, PANA).** Dans `IPO-age`, le ticker HYACU correspond à trois entreprises distinctes (Haymaker II, III, IV). Aucune n'apparaît dans `dataset_4`. Le risque théorique est qu'un merge sur ticker seul produise un match arbitraire ; ici le risque est nul puisque les tickers en doublon ne sont pas dans le périmètre.

**Exemple 5 — Tickers absents d'IPO-age mais présents dans `dataset_4`** : GOTU, JFU, QNCX, AMTD, JMIA, ALRS, KRRO, FUTU, etc. (56 cas). Ces tickers correspondent souvent à des IPO de sociétés étrangères (ADR) ou très récentes. Le rapport conserve ces observations dans `dataset_4` (offer price disponible) et dans `daily_returns`, mais on ne pourra pas leur attribuer de CUSIP venant d'IPO-age.

## 3. Clé de merge retenue

La priorité demandée est la suivante :

1. **CUSIP / CIK** : *non disponible* dans `dataset_4`, `daily_returns` et `offer_prices`. Seul `IPO-age` le contient. → impossible à utiliser comme clé entre les deux fichiers principaux.
2. **Ticker + date d'IPO** : possible *en théorie*, mais la colonne `Date` de `dataset_4` n'est pas fiable (cf. exemple DOLE, 57 cas d'écart > 7 jours avec la 1ère cotation). La date d'IPO réelle se reconstruit depuis `daily_returns` (min(date) par ticker). → utilisable comme **vérification croisée** plutôt que comme clé.
3. **Ticker + nom d'entreprise** : `dataset_4` ne contient pas de colonne nom. → impossible.
4. **Ticker seul** : retenu en pratique, car `dataset_4` n'a aucun ticker en doublon (407 tickers uniques sur 407 lignes), et `daily_returns` ne contient qu'une seule cohorte par ticker sur le périmètre. Le risque est limité aux tickers réutilisés dans `IPO-age`, mais aucun de ces tickers n'est dans `dataset_4`.

**Clé retenue : `ticker` seul, avec deux contrôles documentés** :
- vérification que `dataset_4['ticker']` est unique ;
- vérification que la 1ère cotation `daily_returns` correspond bien à la cohorte attribuée dans `dataset_4`.

L'ajout de la colonne CUSIP depuis `IPO-age` reste possible pour les 351 tickers communs et est effectué dans le notebook (à titre informatif, pas comme clé).

## 4. Tickers non matchés et traitement

| Ticker | Problème | Traitement |
|---|---|---|
| HCWB | Absent de `daily_returns` | Conservé dans `df_final`, exclu des analyses H3 et H4 (rendements `NaN`). Justification : pas de série de prix pour recalculer les rendements depuis l'offer price. |
| 56 tickers absents d'IPO-age | Pas de CUSIP | Conservés (ces fichiers ne sont pas la source primaire des analyses) ; CUSIP simplement laissé `NaN`. |

Aucune observation n'est exclue silencieusement. Toute exclusion est commentée dans le notebook.

## 5. Limites résiduelles du merge

- **Pas de clé stable (CUSIP/CIK)** entre `dataset_4` et `daily_returns`. Le merge ticker reste exposé à un risque résiduel si l'extraction yfinance a renvoyé des données pour un ticker homonyme. Ce risque est mitigé par la vérification cohorte ↔ 1ère cotation.
- **OfferPrice ajusté ou non ?** Sur 7 tickers (DUO, ARBK, BCAB, COOK, YJ, KRRO, BIRD…), les `close_px` issus de `daily_returns` sont des prix ajustés post-split alors que l'OfferPrice reste au niveau nominal d'IPO. Cela rend le calcul brut `(Price_30d − OfferPrice) / OfferPrice` aberrant pour ces observations. Le notebook calcule les rendements depuis l'offer price puis identifie ces outliers et les présente séparément (cf. cellule dédiée).
- **Date d'IPO de `dataset_4` non fiable** : la colonne `Date` mélange dates de filing et d'IPO antérieures. La date d'IPO réelle utilisée dans le notebook corrigé est la 1ère date de cotation issue de `daily_returns`.
- **Fichier `offer_prices_from_sec_1_.xlsx`** : les colonnes `offer_price_fmp` et `ipo_date_fmp` sont entièrement vides. Ce fichier ne sert finalement pas de source d'OfferPrice ; la seule colonne d'offer price utilisable est `dataset_4['OfferPrice']`.
