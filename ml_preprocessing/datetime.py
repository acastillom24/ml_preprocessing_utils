import pandas as pd

def extract_datetime_features(df, datetime_column):
    """
    Extrae características de una columna datetime.
    
    Args:
        df (pd.DataFrame): DataFrame de entrada
        datetime_column (str): Nombre de la columna datetime
        
    Returns:
        pd.DataFrame: DataFrame con características extraídas
    """
    df_copy = df.copy()
    
    # Convertir a datetime si no lo está
    df_copy[datetime_column] = pd.to_datetime(df_copy[datetime_column])
    
    # Extraer características
    df_copy[f'{datetime_column}_year'] = df_copy[datetime_column].dt.year
    df_copy[f'{datetime_column}_month'] = df_copy[datetime_column].dt.month
    df_copy[f'{datetime_column}_day'] = df_copy[datetime_column].dt.day
    df_copy[f'{datetime_column}_dayofweek'] = df_copy[datetime_column].dt.dayofweek
    df_copy[f'{datetime_column}_hour'] = df_copy[datetime_column].dt.hour
    
    return df_copy