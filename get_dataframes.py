import kaggle

def get_dataframe(dataframe):
    # Autenticando con la api de kaggle, se conecta gracias a las variables seteadas en gh actions
    print("Nos autenticamos con la API de kaggle...")
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(dataframe, path='dataframes/', unzip=True)
    # Se descarga el dataframe descomprimido en la carpeta dataframes
    print("Descargado el dataframe en la carpeta dataframes")


def main():
    # Para descargar más df simplemente añadir la llamada al csv
    get_dataframe('himanshunakrani/student-study-hours')

if __name__ == "__main__":
    main()