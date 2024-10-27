import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def handle_missing_numeric(df, columns, method='mean'):
    """
    Maneja valores faltantes en columnas numéricas.
    
    Args:
        df (pd.DataFrame): DataFrame de entrada
        columns (list): Lista de columnas numéricas
        method (str): 'mean', 'median', o 'zero'
        
    Returns:
        pd.DataFrame: DataFrame con valores faltantes tratados
    """
    df_copy = df.copy()
    
    for col in columns:
        if method == 'mean':
            df_copy[col].fillna(df_copy[col].mean(), inplace=True)
        elif method == 'median':
            df_copy[col].fillna(df_copy[col].median(), inplace=True)
        elif method == 'zero':
            df_copy[col].fillna(0, inplace=True)
            
    return df_copy

def scale_numeric_features(df, columns, method='standard'):
    """
    Escala características numéricas.
    
    Args:
        df (pd.DataFrame): DataFrame de entrada
        columns (list): Lista de columnas a escalar
        method (str): 'standard' para StandardScaler, 'minmax' para MinMaxScaler
        
    Returns:
        pd.DataFrame: DataFrame con columnas escaladas
    """
    df_copy = df.copy()
    
    if method == 'standard':
        scaler = StandardScaler()
    elif method == 'minmax':
        scaler = MinMaxScaler()
        
    df_copy[columns] = scaler.fit_transform(df_copy[columns])
    return df_copy