import os

import constants

import get_hospital_data
import extract_hospitals

os.makedirs(os.path.dirname(constants.DATA_DIRECTORY_PATH), exist_ok=True)
get_hospital_data.get_base_data_from_website()
extract_hospitals.extract_hospitals(get_hospital_data.FILE_PATH)
