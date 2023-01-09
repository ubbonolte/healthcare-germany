from bs4 import BeautifulSoup
import re
import pandas as pd
import constants

RAW_ADDRESS_ROWS_DATA = constants.RAW_ADDRESS_ROWS_DATA



def extract_adress_rows(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Extract the rows from the table
    rows = []
    for tr in soup.find_all('tr'):
        has_address_tag = False
        cells = []
        for td in tr.find_all('td'):
            if td.find('address'):
                has_address_tag = True
                link = td.find('a', href=True)
                if(link):
                    cells.append([link['href']])
            cells.append(split_string_by_regex(td.text.strip()))

        if has_address_tag:
            rows.append(flatten(cells))
    return rows


def flatten(l):
    return [item for sublist in l for item in sublist]


def split_string_by_regex(string, pattern=r'[\n\t]+'):
    return re.split(pattern, string)


def extract_hospitals(input_file):
    with open(input_file, 'r') as base_search_source:
        rows = extract_adress_rows(base_search_source)
        df: pd.DataFrame = pd.DataFrame(rows)
        df.to_csv(RAW_ADDRESS_ROWS_DATA)


if __name__ == "__main__":
    extract_hospitals(constants.RAW_HOSPITAL_ADDRESS_DATA)