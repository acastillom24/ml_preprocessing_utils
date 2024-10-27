import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def clean_text(text):
    """
    Limpia texto eliminando caracteres especiales y convirtiendo a minúsculas.
    
    Args:
        text (str): Texto a limpiar
        
    Returns:
        str: Texto limpio
    """
    # Convertir a minúsculas
    text = str(text).lower()
    
    # Eliminar caracteres especiales
    text = re.sub(r'[^\w\s]', '', text)
    
    # Eliminar espacios múltiples
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def vectorize_text(df, text_column, method='tfidf', max_features=1000):
    """
    Vectoriza texto usando CountVectorizer o TfidfVectorizer.
    
    Args:
        df (pd.DataFrame): DataFrame de entrada
        text_column (str): Nombre de la columna de texto
        method (str): 'tfidf' o 'count'
        max_features (int): Número máximo de características
        
    Returns:
        pd.DataFrame: DataFrame con el texto vectorizado
    """
    if method == 'tfidf':
        vectorizer = TfidfVectorizer(max_features=max_features)
    else:
        vectorizer = CountVectorizer(max_features=max_features)
        
    text_features = vectorizer.fit_transform(df[text_column])
    
    # Convertir a DataFrame
    feature_names = vectorizer.get_feature_names_out()
    return pd.DataFrame(text_features.toarray(), columns=feature_names)