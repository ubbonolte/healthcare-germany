import datetime

DATA_DIRECTORY_PATH = f'../../data/{datetime.date.today()}/'
BASE_URL = 'https://dkgev.deutsches-krankenhaus-verzeichnis.de/app/suche'
RAW_HOSPITAL_ADDRESS_DATA = f'{DATA_DIRECTORY_PATH}base_search_source.html'
RAW_ADDRESS_ROWS_DATA = f'{DATA_DIRECTORY_PATH}df_raw_data_rows.csv'