import os

def load(df, dataset_path="data/processed/"):
    """Salva o dataset limpo na pasta de dados processados."""
    os.makedirs(dataset_path, exist_ok=True)  # Garante que a pasta existe

    cleaned_csv_path = os.path.join(dataset_path, "spotify_cleaned.csv")
    df.to_csv(cleaned_csv_path, index=False)
    
    print(f"✅ Dataset limpo salvo em: {cleaned_csv_path}")
    return cleaned_csv_path

if __name__ == "__main__":
    # Importa o transform.py e roda a limpeza antes de salvar
    from transform import transform
    
    df = transform()  # Limpa os dados
    load(df)  # Salva no formato final