# Imports
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import datetime

# %matplotlib inline

vietinbank_url = 'https://www.vietinbank.vn/web/home/vn/lai-suat'

# Use requests to retrieve data from a given URL
vietinbank_response = requests.get(vietinbank_url)

# Parse the whole HTML page using BeautifulSoup
vietinbank_soup = BeautifulSoup(vietinbank_response.text, 'html.parser')

laisuat_table = vietinbank_soup.find("table", id='hor-ex-b')

vietinbank_laisuat = []

laisuat_table_data = laisuat_table.find_all("tr")  # contains 2 rows
for row in laisuat_table_data[3:]:
  tds = row.find_all("td")
  ky_han, canhan_vnd, canhan_usd, canhan_eur, tochuc_vnd, tochuc_usd, tochuc_eur = tds[0].text.strip(), tds[1].text.strip(), tds[2].text.strip(), tds[3].text.strip(), tds[4].text.strip(), tds[5].text.strip(),  tds[6].text.strip()
  vietinbank_laisuat.append((ky_han, canhan_vnd,  canhan_usd, canhan_eur, tochuc_vnd, tochuc_usd, tochuc_eur))  
print(vietinbank_laisuat)

headers = ['Kỳ hạn', 'Cá nhân VND', 'Cá nhân USD', 'Cá nhân EUR', 'Tổ chức VND', 'Tổ chức USD', 'Tổ chức Euro']
vietinbank_laisuat_df = pd.DataFrame(vietinbank_laisuat, columns=headers)
today = datetime.datetime.now()
output_filename = 'data/' + str(today) + '_laisuat_vietinbank.csv'
vietinbank_laisuat_df.to_csv(output_filename, index=None)
