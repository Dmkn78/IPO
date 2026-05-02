"""
analysis.py — Fonctions réutilisables pour l'analyse IPO

Contient les utilitaires pour :
- Chargement et fusion de données
- Calculs de métriques (underpricing, rendements)
- Tests statistiques
- Génération de graphiques
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Tuple, Optional
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# ============================================================================
# 1. CHARGEMENT & FUSION DE DONNÉES
# ============================================================================

def load_and_merge_data(
    dataset_path: str,
    ipo_age_path: str,
    daily_returns_path: str,
    offer_prices_path: str,
    merge_key: str = "ticker"
) -> pd.DataFrame:
    """
    Charge et fusionne tous les fichiers source en un seul DataFrame.
    
    Parameters
    ----------
    dataset_path : str
        Chemin vers dataset.xlsx
    ipo_age_path : str
        Chemin vers IPO-age.xlsx
    daily_returns_path : str
        Chemin vers daily_returns_cache.csv
    offer_prices_path : str
        Chemin vers offer_prices_from_sec.xlsx
    merge_key : str
        Clé de fusion (default: "ticker")
    
    Returns
    -------
    pd.DataFrame
        DataFrame fusionné avec toutes les colonnes
    
    Example
    -------
    >>> df = load_and_merge_data(
    ...     "../data/raw/dataset.xlsx",
    ...     "../data/raw/IPO-age.xlsx",
    ...     "../data/raw/daily_returns_cache.csv",
    ...     "../data/raw/offer_prices_from_sec.xlsx"
    ... )
    >>> print(df.shape, df.columns)
    """
    # À implémenter selon la structure exacte des fichiers
    pass


# ============================================================================
# 2. CALCUL DE MÉTRIQUES
# ============================================================================

def calculate_underpricing(
    open_price: float,
    close_price: float
) -> float:
    """
    Calcule l'underpricing pour un IPO donné.
    
    Underpricing = (Close J0 - Open J0) / Open J0
    
    Parameters
    ----------
    open_price : float
        Prix d'ouverture du J0
    close_price : float
        Prix de clôture du J0
    
    Returns
    -------
    float
        Underpricing en pourcentage
    
    Example
    -------
    >>> underpricing = calculate_underpricing(open=100, close=110)
    >>> print(underpricing)
    10.0
    """
    if open_price <= 0:
        return np.nan
    return ((close_price - open_price) / open_price) * 100


def calculate_returns(
    price_start: float,
    price_end: float,
    reference_price: Optional[float] = None
) -> float:
    """
    Calcule le rendement entre deux prix.
    
    Return = (Price_end - Price_start) / Price_start
    
    Parameters
    ----------
    price_start : float
        Prix initial
    price_end : float
        Prix final
    reference_price : float, optional
        Si fourni, utilise cette référence au lieu de price_start
    
    Returns
    -------
    float
        Rendement en pourcentage
    
    Example
    -------
    >>> ret = calculate_returns(100, 110)
    >>> print(ret)
    10.0
    """
    if reference_price is not None:
        price_start = reference_price
    
    if price_start <= 0:
        return np.nan
    return ((price_end - price_start) / price_start) * 100


# ============================================================================
# 3. TESTS STATISTIQUES
# ============================================================================

def test_mann_whitney(
    group1: pd.Series,
    group2: pd.Series,
    alternative: str = "two-sided"
) -> Tuple[float, float]:
    """
    Test Mann-Whitney U entre deux groupes.
    
    Parameters
    ----------
    group1 : pd.Series
        Données du groupe 1
    group2 : pd.Series
        Données du groupe 2
    alternative : str
        Type de test: "two-sided", "less", "greater"
    
    Returns
    -------
    Tuple[float, float]
        (Statistique U, p-value)
    
    Example
    -------
    >>> stat, pval = test_mann_whitney(group1, group2)
    >>> if pval < 0.05:
    ...     print("Différence significative")
    """
    group1_clean = group1.dropna()
    group2_clean = group2.dropna()
    
    stat, pval = stats.mannwhitneyu(
        group1_clean,
        group2_clean,
        alternative=alternative
    )
    
    return stat, pval


# ============================================================================
# 4. UTILITAIRES DE NETTOYAGE
# ============================================================================

def clean_numeric_column(
    series: pd.Series,
    remove_outliers: bool = False,
    method: str = "iqr"
) -> pd.Series:
    """
    Nettoie une colonne numérique (gère les NaN, outliers, etc).
    
    Parameters
    ----------
    series : pd.Series
        Colonne à nettoyer
    remove_outliers : bool
        Si True, supprime les outliers
    method : str
        Méthode pour détecter outliers: "iqr" ou "zscore"
    
    Returns
    -------
    pd.Series
        Série nettoyée
    """
    # Supprimer les NaN
    clean_series = series.dropna()
    
    if remove_outliers:
        if method == "iqr":
            Q1 = clean_series.quantile(0.25)
            Q3 = clean_series.quantile(0.75)
            IQR = Q3 - Q1
            mask = (clean_series >= Q1 - 1.5 * IQR) & (clean_series <= Q3 + 1.5 * IQR)
            clean_series = clean_series[mask]
        elif method == "zscore":
            z_scores = np.abs(stats.zscore(clean_series))
            clean_series = clean_series[z_scores < 3]
    
    return clean_series


# ============================================================================
# 5. GRAPHIQUES
# ============================================================================

def plot_distribution_comparison(
    group1: pd.Series,
    group2: pd.Series,
    label1: str = "Group 1",
    label2: str = "Group 2",
    title: str = "Distribution Comparison",
    xlabel: str = "Value",
    figsize: Tuple[int, int] = (10, 6)
) -> None:
    """
    Crée un graphique de comparaison de distributions (boxplot + violin).
    
    Parameters
    ----------
    group1, group2 : pd.Series
        Données des deux groupes
    label1, label2 : str
        Libellés des groupes
    title : str
        Titre du graphique
    xlabel : str
        Libellé de l'axe X
    figsize : Tuple
        Taille de la figure
    """
    fig, axes = plt.subplots(1, 2, figsize=figsize)
    
    # Boxplot
    data_to_plot = [group1.dropna(), group2.dropna()]
    axes[0].boxplot(data_to_plot, labels=[label1, label2])
    axes[0].set_title(f"{title} - Boxplot")
    axes[0].set_ylabel(xlabel)
    axes[0].grid(alpha=0.3)
    
    # Violin plot
    df_temp = pd.DataFrame({
        'Value': pd.concat([group1, group2]),
        'Group': [label1] * len(group1) + [label2] * len(group2)
    })
    sns.violinplot(data=df_temp, x='Group', y='Value', ax=axes[1])
    axes[1].set_title(f"{title} - Violin")
    axes[1].set_ylabel(xlabel)
    axes[1].grid(alpha=0.3, axis='y')
    
    plt.suptitle(title, fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()


# ============================================================================
# 6. VALIDATION DES DONNÉES
# ============================================================================

def validate_merge_keys(
    df_list: list,
    key_names: list,
    expected_key: str = "ticker"
) -> dict:
    """
    Valide la qualité des clés de fusion entre DataFrames.
    
    Parameters
    ----------
    df_list : list
        Liste de DataFrames
    key_names : list
        Noms des DataFrames
    expected_key : str
        Clé attendue pour la fusion
    
    Returns
    -------
    dict
        Rapport de validation
    """
    report = {}
    
    for df, name in zip(df_list, key_names):
        if expected_key in df.columns:
            report[name] = {
                'has_key': True,
                'n_unique': df[expected_key].nunique(),
                'n_duplicates': df[expected_key].duplicated().sum(),
                'n_missing': df[expected_key].isna().sum()
            }
        else:
            report[name] = {'has_key': False}
    
    return report


# ============================================================================
# Fin du module
# ============================================================================

if __name__ == "__main__":
    # Tests simples
    print("Module analysis.py chargé avec succès!")
    
    # Exemple: calculate_underpricing
    up = calculate_underpricing(open_price=100, close_price=110)
    print(f"Underpricing (100→110): {up:.2f}%")
    
    # Exemple: calculate_returns
    ret = calculate_returns(price_start=100, price_end=130)
    print(f"Rendement (100→130): {ret:.2f}%")
