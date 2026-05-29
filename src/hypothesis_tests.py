
import scipy.stats as stats
import pandas as pd

def test_provinces(df):
    """Test 1: Risk differences across provinces (using Claim Frequency)"""
    contingency = pd.crosstab(df['Province'], df['ClaimOccurred'])
    chi2, p, dof, expected = stats.chi2_contingency(contingency)
    return {"test": "Chi-Square", "statistic": chi2, "p_value": p}

def test_gender(df):
    """Test 4: Risk difference between Male and Female"""
    male = df[df['Gender'] == 'Male']['LossRatio'].dropna()
    female = df[df['Gender'] == 'Female']['LossRatio'].dropna()
    
    t_stat, p_value = stats.ttest_ind(male, female, equal_var=False)
    return {"test": "T-Test", "statistic": t_stat, "p_value": p_value}

def test_margin_zipcode(df, zip1, zip2):
    """Test 3: Margin difference between two zip codes"""
    group1 = df[df['PostalCode'] == zip1]['Margin']
    group2 = df[df['PostalCode'] == zip2]['Margin']
    
    t_stat, p_value = stats.ttest_ind(group1, group2, equal_var=False)
    return {"test": "T-Test", "statistic": t_stat, "p_value": p_value}
