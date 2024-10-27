from setuptools import setup, find_packages

setup(
    name="ml_preprocessing",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'numpy>=1.19.0',
        'pandas>=1.2.0',
        'scikit-learn>=0.24.0'
    ],
    author="Alín Castillo",
    author_email="alincastillo1995@gmail.com",
    description="Utilidades de preprocesamiento para proyectos de Machine Learning",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/alincastillo21/ml_preprocessing_utils",
)