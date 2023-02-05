import kaggle
import webbrowser
import os

# VARIABLES
PATH = "dataframes/"
GITHUB_ACTIONS = os.getenv('GITHUB_ACTIONS')
DIR = os.listdir(PATH)


# FUNCIONES
def get_dataframe(dataframe):
    # Autenticando con la api de kaggle, se conecta gracias a las variables seteadas en gh actions
    print("Nos autenticamos con la API de kaggle...")
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(dataframe, path=PATH, unzip=True)
    # Se descarga el dataframe descomprimido en la carpeta dataframes
    print("Descargado el dataframe en la carpeta dataframes")

def get_dataframe_from_local():
    if len(DIR) > 0:
        print("Ya tienes el dataframe en local")
        return
    else:
        print("Necesitas descargar el dataframe en local y descomprimirlo en la carpeta dataframes")
        print("Abriendo url de descarga...")
        url = 'https://www.kaggle.com/himanshunakrani/student-study-hours'
        webbrowser.open(url, new=2)

def main():
    if GITHUB_ACTIONS == 'true':
        # Para descargar más df simplemente añadir la llamada al csv
        get_dataframe('himanshunakrani/student-study-hours')
    else:
        get_dataframe_from_local()

if __name__ == "__main__":
    main()