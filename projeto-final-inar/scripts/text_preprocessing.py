# scripts/text_preprocessing.py
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Função de limpeza de texto
def clean_text(text):
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    # Remove caracteres especiais e números, mantendo apenas letras
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Tokeniza o texto
    words = word_tokenize(text.lower())
    # Remove stopwords
    words = [word for word in words if word not in stopwords.words('english')]
    # Junta as palavras limpas em uma string novamente
    return ' '.join(words)

# Carregar os dados
gossipcop_data = pd.read_csv('../dataset/FakeNewsNet/gossipcop_fake.csv')

# Filtrar apenas colunas que têm dados do tipo string
text_columns = gossipcop_data.select_dtypes(include='object').columns

# Aplicar a limpeza de texto em todas as colunas de texto
for column in text_columns:
    gossipcop_data[f'{column}_cleaned'] = gossipcop_data[column].apply(clean_text)

# Salvar o resultado em um novo arquivo CSV
gossipcop_data.to_csv('../dataset/processed/gossipcop_cleaned.csv', index=False)
