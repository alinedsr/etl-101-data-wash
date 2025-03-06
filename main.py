from app.extract import extract
from app.transform import transform
from app.load import load

def main():
    print("🚀 Iniciando Pipeline ETL...")

    # 🔹 Etapa 1: Extração
    dataset_path = extract()

    # 🔹 Etapa 2: Transformação
    df = transform(dataset_path)

    # 🔹 Etapa 3: Carga
    load(df)

    print("✅ ETL finalizado com sucesso!")

if __name__ == "__main__":
    main()