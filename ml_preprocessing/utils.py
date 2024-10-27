import pandas as pd
import numpy as np

def identify_column_types(df):
    """
    Identifica los tipos de columnas en el DataFrame.
    
    Args:
        df (pd.DataFrame): DataFrame de entrada
        
    Returns:
        dict: Diccionario con tipos de columnas
    """
    column_types = {
        'numeric': [],
        'categorical': [],
        'datetime': [],
        'text': []
    }
    
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            column_types['numeric'].append(column)
        elif pd.api.types.is_datetime64_any_dtype(df[column]):
            column_types['datetime'].append(column)
        elif df[column].dtype == 'object':
            # Verificar si es texto largo (posiblemente texto libre)
            if df[column].str.len().mean() > 50:
                column_types['text'].append(column)
            else:
                column_types['categorical'].append(column)
                
    return column_types

def check_missing_values(df):
    """
    Analiza valores faltantes en el DataFrame.
    
    Args:
        df (pd.DataFrame): DataFrame de entrada
        
    Returns:
        pd.DataFrame: Resumen de valores faltantes
    """
    missing = pd.DataFrame({
        'missing_count': df.isnull().sum(),
        'missing_percentage': (df.isnull().sum() / len(df)) * 100
    })
    
    return missing[missing['missing_count'] > 0].sort_values('missing_count', ascending=False)