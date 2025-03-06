import os
from kaggle.api.kaggle_api_extended import KaggleApi

def check_kaggle_api():
    """Verifica se a API do Kaggle está configurada corretamente."""
    kaggle_config_path = os.path.expanduser("~/.kaggle/kaggle.json")  # Linux/macOS
    kaggle_config_path_win = os.path.expanduser("~/AppData/Roaming/Kaggle/kaggle.json")  # Windows

    if not os.path.exists(kaggle_config_path) and not os.path.exists(kaggle_config_path_win):
        print("❌ ERRO: A API do Kaggle não está configurada!")
        print("\n🔹 Como configurar a API do Kaggle:")
        print("1️⃣ Acesse: https://www.kaggle.com/settings")
        print("2️⃣ Role até a seção 'API' e clique em 'Create New Token'")
        print("3️⃣ Um arquivo 'kaggle.json' será baixado.")
        print("4️⃣ Mova o arquivo para:")
        print("   - Linux/Mac: ~/.kaggle/kaggle.json")
        print("   - Windows: C:\\Users\\SEU_USUARIO\\.kaggle\\kaggle.json")
        print("5️⃣ No Linux/Mac, rode: chmod 600 ~/.kaggle/kaggle.json")
        print("\n⚠️ Depois de configurar, tente rodar o script novamente.")
        exit(1)  # Encerra o programa com erro

def extract():
    """Baixa o dataset do Kaggle e move para a pasta local do projeto."""
    check_kaggle_api()  # Verifica se a API está configurada

    dataset_name = "vitoriarodrigues/spotifycsv-file-modified-for-data-cleaning"
    local_path = "data/raw/"
    os.makedirs(local_path, exist_ok=True)

    # Inicializa a API do Kaggle
    api = KaggleApi()
    api.authenticate()

    print("🚀 Baixando dataset do Kaggle...")

    # Baixa o dataset para a pasta local
    api.dataset_download_files(dataset_name, path=local_path, unzip=True)
    print(f"✅ Dataset baixado e extraído em: {local_path}")

    # Verifica se os arquivos realmente foram baixados
    files = os.listdir(local_path)
    if not files:
        print(f"❌ Erro: Nenhum arquivo encontrado em {local_path}.")
        exit(1)

    print("📂 Arquivos baixados:")
    for file in files:
        print(f"   - {file}")

    return local_path

if __name__ == "__main__":
    extract()