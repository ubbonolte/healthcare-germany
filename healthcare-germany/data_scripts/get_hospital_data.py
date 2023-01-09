import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import constants

BASE_URL = constants.BASE_URL
RAW_HOSPITAL_ADDRESS_DATA = constants.RAW_HOSPITAL_ADDRESS_DATA


def get_base_data_from_website():
    with webdriver.Chrome(executable_path='../../resources/chromedriver') as driver:
        driver.get(BASE_URL)

        # Open search
        driver.find_element(By.ID, 'search_send').click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'js_search'))).click()

        # Create link to fetch 3000 elements
        execu = f'''
        var a = document.createElement('a');
        a.id = "thisisunique";
        a.class = "page-link";
        a.setAttribute("onclick", "filterPagination(1,3000);return false;");
        a.href="#";
        a.text="lets get it";
        document.body.appendChild(a);
        '''
        driver.execute_script(execu)
        driver.find_element(By.ID, 'thisisunique')
        custom_link = driver.find_element(By.LINK_TEXT, 'lets get it')
        driver.execute_script("arguments[0].click();", custom_link)

        # Wait for data to be loaded
        time.sleep(30)

        # Save file
        with open(RAW_HOSPITAL_ADDRESS_DATA, 'w') as f:
            f.write(driver.page_source)


if __name__ == "__main__":
    os.makedirs(os.path.dirname(RAW_HOSPITAL_ADDRESS_DATA), exist_ok=True)
    get_base_data_from_website()
