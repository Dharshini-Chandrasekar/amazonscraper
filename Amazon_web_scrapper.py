from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = 'https://www.amazon.com/s?k=latest+mobile+phones+2024&crid=2QTG7U0BOQ80C&sprefix=latest+mobile%2Caps%2C392&ref=nb_sb_ss_ts-doa-p_1_13'

HEADERS = ({'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36','Assemble_Language' : 'en-US, en;q=0.5'})
webpage = requests.get(URL,headers=HEADERS)
webpage
soup = BeautifulSoup(webpage.content,"html.parser")

