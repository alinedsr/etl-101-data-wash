import pandas as pd
import os

def find_csv_file(path):
    """Procura um arquivo CSV dentro do diretório especificado."""
    for file in os.listdir(path):
        if file.endswith(".csv"):
            return os.path.join(path, file)
    raise FileNotFoundError("❌ Nenhum arquivo CSV encontrado em data/raw/")

def transform(dataset_path="data/raw/"):
    """Limpa e transforma os dados do Spotify."""
    print("\n🔍 Iniciando limpeza dos dados...")

    # Encontrar automaticamente o CSV correto
    csv_file = find_csv_file(dataset_path)

    # Carregar o CSV no Pandas
    df = pd.read_csv(csv_file)
    print(f"✅ Dataset carregado: {csv_file}")

    # ✅ Remover valores nulos
    df.dropna(inplace=True)

    # ✅ Remover duplicatas
    df.drop_duplicates(inplace=True)

    # ✅ Padronizar os nomes das colunas
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    print("✅ Dados limpos!")
    
    # Retorna o DataFrame limpo
    return df

if __name__ == "__main__":
    df = transform()
    print(df.head())  # Mostra um preview dos dados limpos