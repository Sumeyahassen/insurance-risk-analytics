import pandas as pd
import numpy as np

def load_raw_data():
    """Load the raw pipe-delimited dataset"""
    df = pd.read_csv('data/insurance_data.csv', sep='|', low_memory=False)
    df.columns = [col.strip() for col in df.columns]
    return df

def create_cleaned_data():
    """Clean the data and save cleaned version"""
    df = load_raw_data()
    
    # Basic cleaning
    df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'])
    
    # Remove rows with missing key values
    df = df.dropna(subset=['TotalPremium', 'TotalClaims', 'Province', 'Gender'])
    
    # Create key metrics
    df['LossRatio'] = df['TotalClaims'] / df['TotalPremium'].replace(0, np.nan)
    df['Margin'] = df['TotalPremium'] - df['TotalClaims']
    df['ClaimOccurred'] = (df['TotalClaims'] > 0).astype(int)
    
    # Save cleaned version
    df.to_csv('data/insurance_data_cleaned.csv', index=False)
    print(f"✅ Cleaned dataset saved with {df.shape[0]} rows and {df.shape[1]} columns")
    return df

# Run this when script is executed directly
if __name__ == "__main__":
    create_cleaned_data()