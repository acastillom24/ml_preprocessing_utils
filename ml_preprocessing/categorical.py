import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

def encode_categorical_columns(df, columns, method='label'):
    """
    Codifica variables categóricas usando Label Encoding u One-Hot Encoding.
    
    Args:
        df (pd.DataFrame): DataFrame de entrada
        columns (list): Lista de columnas a codificar
        method (str): 'label' para Label Encoding, 'onehot' para One-Hot Encoding
        
    Returns:
        pd.DataFrame: DataFrame con las columnas codificadas
    """
    df_copy = df.copy()
    
    if method == 'label':
        le = LabelEncoder()
        for col in columns:
            df_copy[col] = le.fit_transform(df_copy[col])
    
    elif method == 'onehot':
        df_copy = pd.get_dummies(df_copy, columns=columns)
    
    return df_copy