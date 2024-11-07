import pandas as pd

# Função para carregar os dados dos arquivos CSV
def load_data():
    gossipcop_real_file = '../data/raw/gossipcop_real.csv'
    gossipcop_fake_file = '../data/raw/gossipcop_fake.csv'
    politifact_real_file = '../data/raw/politifact_real.csv'
    politifact_fake_file = '../data/raw/politifact_fake.csv'

    # Carregar os datasets
    gossipcop_real_df = pd.read_csv(gossipcop_real_file)
    gossipcop_fake_df = pd.read_csv(gossipcop_fake_file)
    politifact_real_df = pd.read_csv(politifact_real_file)
    politifact_fake_df = pd.read_csv(politifact_fake_file)

    # Exibir as primeiras linhas dos datasets para análise
    print("Gossipcop Real Dataset Head:")
    print(gossipcop_real_df.head())
    print("\nGossipcop Fake Dataset Head:")
    print(gossipcop_fake_df.head())
    print("\nPolitifact Real Dataset Head:")
    print(politifact_real_df.head())
    print("\nPolitifact Fake Dataset Head:")
    print(politifact_fake_df.head())

    return gossipcop_real_df, gossipcop_fake_df, politifact_real_df, politifact_fake_df

# Função para combinar os dados (real + fake) de cada conjunto
def merge_data(real_df, fake_df):
    # Adicionar coluna de label para distinguir entre 'real' e 'fake'
    real_df['label'] = 'real'
    fake_df['label'] = 'fake'
    
    # Concatenar os datasets real e fake
    merged_df = pd.concat([real_df, fake_df], ignore_index=True)
    return merged_df

# Função de limpeza dos dados
def clean_data(df):
    # Exemplo de limpeza básica: remover colunas desnecessárias e lidar com valores ausentes
    df = df.dropna()  
    df = df.drop_duplicates()  
    return df

if __name__ == '__main__':
    # Carregar os dados
    gossipcop_real, gossipcop_fake, politifact_real, politifact_fake = load_data()

    # Mesclar os dados
    gossipcop_merged = merge_data(gossipcop_real, gossipcop_fake)
    politifact_merged = merge_data(politifact_real, politifact_fake)

    # Limpar os dados
    gossipcop_merged_cleaned = clean_data(gossipcop_merged)
    politifact_merged_cleaned = clean_data(politifact_merged)

    # Salvar os dados limpos e mesclados em novos arquivos CSV
    gossipcop_merged_cleaned.to_csv('../data/processed/gossipcop_merged.csv', index=False)
    politifact_merged_cleaned.to_csv('../data/processed/politifact_merged.csv', index=False)

    # print("Dados limpos e mesclados salvos com sucesso!")
