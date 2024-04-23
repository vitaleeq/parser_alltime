import parsing_functions as pf
import excel_functions as ef
from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


"""
pf.create_driver()
vendor_code = 'SARY213'
link = pf.get_product_link(vendor_code)
print(f'{vendor_code}: {link}')
print('___________________________________')
properties = pf.get_properties(link)
print(f'required_properties = {properties}')
print('***********************************')
pf.quit_driver()
"""


# 'Спецификация Tissot Daghaya.xlsx'    B, 10, 64
ef.use_excel_file('Спецификация Tissot Daghaya.xlsx')
