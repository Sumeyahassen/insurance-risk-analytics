import pandas as pd
import numpy as np
import os

# Get the project root dynamically
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def load_raw_data():
    """Load the raw insurance dataset with absolute path"""
    data_path = os.path.join(PROJECT_ROOT, 'data', 'insurance_data.csv')
    
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Raw data not found at: {data_path}")
    
    df = pd.read_csv(data_path, sep='|', low_memory=False)
    df.columns = [col.strip() for col in df.columns]
    return df


def load_cleaned_data():
    """Load or create cleaned version"""
    cleaned_path = os.path.join(PROJECT_ROOT, 'data', 'insurance_data_cleaned.csv')
    
    try:
        df = pd.read_csv(cleaned_path)
        print("✅ Loaded existing cleaned data")
    except FileNotFoundError:
        print("🛠 Creating cleaned data from raw...")
        df = load_raw_data()
        
        # Cleaning steps
        df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'])
        df = df.dropna(subset=['TotalPremium', 'TotalClaims', 'Province', 'Gender'])
        
        df['LossRatio'] = df['TotalClaims'] / df['TotalPremium'].replace(0, np.nan)
        df['Margin'] = df['TotalPremium'] - df['TotalClaims']
        df['ClaimOccurred'] = (df['TotalClaims'] > 0).astype(int)
        
        # Save cleaned file
        df.to_csv(cleaned_path, index=False)
        print(f"✅ Cleaned dataset created and saved with {df.shape[0]} rows")
    
    return df


# For direct testing
if __name__ == "__main__":
    df = load_cleaned_data()
    print("Final Shape:", df.shape)