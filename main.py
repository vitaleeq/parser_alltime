from bs4 import BeautifulSoup
import parsing_functions as pf


vendor_code = 'r10018'
id_number = pf.get_product_id(vendor_code)
print(f'{vendor_code}: {id_number}')
print('___________________________________')
tag = pf.get_page(id_number)
#print(tag)

"""
'''
import requests

url = 'https://www.alltime.ru/api/ajax/2020/product-mobile.php?ID=559038&version=1.3'
page = requests.get(url)
print(page.status_code)

#print(page)
soup = BeautifulSoup(page.text, "html.parser")
print(soup)
print('___________________________________')
tag = soup.findAll('dl')
print(tag)'''


import requests

url = "https://www.alltime.ru/api/ajax/2020/product-mobile.php?ID=660626&version=1.3"

payload = {}
headers = {
  'Cookie': '''PHPSESSID=itd28p31t6vkrbpco5sack84r6; ALLTIME_SESSION_SEEN=f37c4bbc930295169cd75a60aa192c5f; rrpvid=216847436182733; _ga=GA1.1.2007646260.1709038380; rcuid=652d82a42169498a428027da; tmr_lvid=d0035b037b781b34ea8fc0715f39f444; tmr_lvidTS=1709038380508; _ym_uid=1709038381989044484; _ym_d=1709038381; rraem=; _userGUID=0:lt4dbqc0:lpX5y6QMnAM6xM6VWW5IMh_9Qg9MqcBK; adid=170903838167497; adrcid=AoB2f_r8dc6Io3-cZS-e4lg; rr-popup-shown=1; ALLTIME_CITY=54736769eec61c79f70f43079869af01; __utmc=260397277; __utmz=260397277.1710152346.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); smartbanner_exited=1; _ym_isad=2; g4c_x=1; srv_id=srv7; searchStartTime=1710437189704; _dvs=0:ltr4jlnd:uqhT78oFYSzeqBDcuRfu~oknsf2v4wXW; __utma=260397277.2007646260.1709038380.1710414353.1710437206.12; _ym_visorc=b; rr-subFormLastView=true; rrviewed=601234%2C666411; __utmb=260397277.6.9.1710437426928; tmr_detect=0%7C1710437434914; digi_uc=W1sidiIsIjYwMTIzNCIsMTcxMDQzNzgzNTgzM10sWyJ2IiwiNjY2NDExIiwxNzEwNDE0MzkzNDU3XSxbInYiLCI2Njg0NTkiLDE3MTA0MTAzODI4OThdLFsidiIsIjU1OTAzOCIsMTcxMDQwODYyOTEyOV0sWyJ2IiwiMzE3ODgwIiwxNzEwNDA4NTk1NTI5XSxbInYiLCI2MzM3MTIiLDE3MTAzMzI4MzYyMDZdLFsidiIsIjMxNzg3OSIsMTcxMDMzMjQxNTExM10sWyJ2IiwiNjQ3MDk1IiwxNzEwMjM3MjEzMjUwXSxbInYiLCI2Njg0NjEiLDE3MTAyMzY5Mzg5MDJdLFsidiIsIjUzNDY0NyIsMTcxMDIzNDk2MTIyNl0sWyJjdiIsIjU5NzM1MyIsMTcxMDQxMDM5NzI1MV0sWyJzdiIsIjYwMTIzNCIsMTcxMDQzNzE5MzIzMl0sWyJzdiIsIjYwMjc0NCIsMTcxMDIzMTg3ODEzMF0sWyJzdiIsIjY2ODQ1MyIsMTcxMDIzMTUwMzkyOF0sWyJzdiIsIjYzMzA5MSIsMTcxMDE2MDk3MTQ3Ml0sWyJzdiIsIjY2ODQ1OSIsMTcxMDE2MDkzNjYxMV1d; _ga_DV4C6GXRL9=GS1.1.1710437205.12.1.1710437850.60.0.0; rr-testCookie=testvalue; rr-viewItemId=601234; rrlevt=1710437850681'''
}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
tag = soup.findAll('dl')
print(tag)
"""