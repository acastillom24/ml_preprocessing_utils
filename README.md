# ML Preprocessing Utilities

Colección de utilidades para preprocesamiento de datos en proyectos de Machine Learning.

## Instalación

```bash
pip install git+https://github.com/tu-usuario/ml_preprocessing.git
```

## Características

- Procesamiento de variables numéricas
  - Manejo de valores faltantes
  - Escalado de características
- Procesamiento de variables categóricas
  - Label Encoding
  - One-Hot Encoding
- Procesamiento de texto
  - Limpieza de texto
  - Vectorización
- Utilidades para fechas
  - Extracción de características temporales

## Ejemplo de uso

```python
from ml_preprocessing.numerical import scale_numeric_features
from ml_preprocessing.categorical import encode_categorical_columns

# Escalar variables numéricas
df = scale_numeric_features(df, ['edad', 'salario'])

# Codificar variables categóricas
df = encode_categorical_columns(df, ['departamento'], method='onehot')
```

```python
from ml_preprocessing import (
    encode_categorical_columns,
    handle_missing_numeric,
    scale_numeric_features,
    clean_text,
    extract_datetime_features,
    identify_column_types
)

# Ejemplo de uso
import pandas as pd

# Cargar datos
df = pd.read_csv('tu_dataset.csv')

# Identificar tipos de columnas
column_types = identify_column_types(df)

# Preprocesar datos numéricos
df = handle_missing_numeric(df, column_types['numeric'])
df = scale_numeric_features(df, column_types['numeric'])

# Preprocesar categóricas
df = encode_categorical_columns(df, column_types['categorical'])

# Preprocesar fechas
if column_types['datetime']:
    df = extract_datetime_features(df, column_types['datetime'][0])
```

## Contribuir

1. Fork el repositorio
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -am 'Añade nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crea un Pull Request

## Changelog

### [1.0.0] - 2024-10-27
- Primera versión estable
- Incluye procesamiento básico de variables numéricas y categóricas