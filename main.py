from bs4 import BeautifulSoup
import parsing_functions as pf
import excel_functions as ef


'''
# 'Спецификация Tissot Daghaya.xlsx'    B, 10, 64
ef.use_excel_file('Спецификация Tissot Daghaya.xlsx')
'''


vendor_code = 'r18017'
id_number = pf.get_product_id(vendor_code)
print(f'{vendor_code}: {id_number}')
print('___________________________________')
tag = pf.get_properties(id_number)
#print(tag)
