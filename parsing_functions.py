from bs4 import BeautifulSoup
import requests


#url = 'https://www.alltime.ru'
cookie = '''PHPSESSID=itd28p31t6vkrbpco5sack84r6; ALLTIME_SESSION_SEEN=f37c4bbc930295169cd75a60aa192c5f; rrpvid=216847436182733; _ga=GA1.1.2007646260.1709038380; rcuid=652d82a42169498a428027da; tmr_lvid=d0035b037b781b34ea8fc0715f39f444; tmr_lvidTS=1709038380508; _ym_uid=1709038381989044484; _ym_d=1709038381; rraem=; _userGUID=0:lt4dbqc0:lpX5y6QMnAM6xM6VWW5IMh_9Qg9MqcBK; adid=170903838167497; adrcid=AoB2f_r8dc6Io3-cZS-e4lg; rr-popup-shown=1; ALLTIME_CITY=54736769eec61c79f70f43079869af01; __utmc=260397277; __utmz=260397277.1710152346.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); smartbanner_exited=1; _ym_isad=2; g4c_x=1; srv_id=srv7; searchStartTime=1710437189704; _dvs=0:ltr4jlnd:uqhT78oFYSzeqBDcuRfu~oknsf2v4wXW; __utma=260397277.2007646260.1709038380.1710414353.1710437206.12; _ym_visorc=b; rr-subFormLastView=true; rrviewed=601234%2C666411; __utmb=260397277.6.9.1710437426928; tmr_detect=0%7C1710437434914; digi_uc=W1sidiIsIjYwMTIzNCIsMTcxMDQzNzgzNTgzM10sWyJ2IiwiNjY2NDExIiwxNzEwNDE0MzkzNDU3XSxbInYiLCI2Njg0NTkiLDE3MTA0MTAzODI4OThdLFsidiIsIjU1OTAzOCIsMTcxMDQwODYyOTEyOV0sWyJ2IiwiMzE3ODgwIiwxNzEwNDA4NTk1NTI5XSxbInYiLCI2MzM3MTIiLDE3MTAzMzI4MzYyMDZdLFsidiIsIjMxNzg3OSIsMTcxMDMzMjQxNTExM10sWyJ2IiwiNjQ3MDk1IiwxNzEwMjM3MjEzMjUwXSxbInYiLCI2Njg0NjEiLDE3MTAyMzY5Mzg5MDJdLFsidiIsIjUzNDY0NyIsMTcxMDIzNDk2MTIyNl0sWyJjdiIsIjU5NzM1MyIsMTcxMDQxMDM5NzI1MV0sWyJzdiIsIjYwMTIzNCIsMTcxMDQzNzE5MzIzMl0sWyJzdiIsIjYwMjc0NCIsMTcxMDIzMTg3ODEzMF0sWyJzdiIsIjY2ODQ1MyIsMTcxMDIzMTUwMzkyOF0sWyJzdiIsIjYzMzA5MSIsMTcxMDE2MDk3MTQ3Ml0sWyJzdiIsIjY2ODQ1OSIsMTcxMDE2MDkzNjYxMV1d; _ga_DV4C6GXRL9=GS1.1.1710437205.12.1.1710437850.60.0.0; rr-testCookie=testvalue; rr-viewItemId=601234; rrlevt=1710437850681'''
cookie1 = '''PHPSESSID=itd28p31t6vkrbpco5sack84r6; ALLTIME_SESSION_SEEN=f37c4bbc930295169cd75a60aa192c5f; rrpvid=216847436182733; _ga=GA1.1.2007646260.1709038380; rcuid=652d82a42169498a428027da; tmr_lvid=d0035b037b781b34ea8fc0715f39f444; tmr_lvidTS=1709038380508; _ym_uid=1709038381989044484; _ym_d=1709038381; rraem=; _userGUID=0:lt4dbqc0:lpX5y6QMnAM6xM6VWW5IMh_9Qg9MqcBK; adid=170903838167497; adrcid=AoB2f_r8dc6Io3-cZS-e4lg; rr-popup-shown=1; __utmz=260397277.1710152346.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); g4c_x=1; __utmc=260397277; srv_id=srv4; _ym_isad=2; _dvs=0:ltx70xyk:DArF6Vdhaqa62xTgV6Tj0bQn30wEX49_; __utma=260397277.2007646260.1709038380.1710845048.1710850288.19; _ym_visorc=b; rr-subFormLastView=true; rrviewed=540023%2C668459%2C540024%2C628011%2C648080; __utmb=260397277.6.9.1710851104015; tmr_detect=0%7C1710851111999; digi_uc=W1sidiIsIjYyODAxMSIsMTcxMDg1MTEwMTUxNV0sWyJ2IiwiNTQwMDI0IiwxNzEwODUwMjg4MDgzXSxbInYiLCI2Njg0NTkiLDE3MTA4NDY3NDMxNDldLFsidiIsIjU1OTAzOCIsMTcxMDg0NTYwOTI4N10sWyJ2IiwiNTQwMDIzIiwxNzEwODQ1NDY5ODU1XSxbInYiLCI2NTAyMjIiLDE3MTA4NDQ2OTQ0MTNdLFsidiIsIjU5NzM1MyIsMTcxMDUwMDU0NDAzNF0sWyJ2IiwiNjUwMTU0IiwxNzEwNDkzNzA1NDE2XSxbInYiLCI2NTM5NDIiLDE3MTA0OTM0MzUwNjldLFsidiIsIjYwMTIzNCIsMTcxMDQ5MjYyMTk1N10sWyJjdiIsIjU5NzM1MyIsMTcxMDg0NTYxNTM2NV0sWyJzdiIsIjU0MDAyNCIsMTcxMDg1MDI4MzQ1Nl0sWyJzdiIsIjE4MDE3IiwxNzEwNzYzMDc5NTAzXSxbInN2IiwiNjAxMjM0IiwxNzEwNDM4MjQwMDM4XSxbInN2IiwiNjAyNzQ0IiwxNzEwMjMxODc4MTMwXSxbInN2IiwiNjY4NDUzIiwxNzEwMjMxNTAzOTI4XSxbInN2IiwiNjMzMDkxIiwxNzEwMTYwOTcxNDcyXSxbInN2IiwiNjY4NDU5IiwxNzEwMTYwOTM2NjExXSxbInYiLCI2NDgwODAiLDE3MTA4NTExNTY5ODhdXQ==; rr-testCookie=testvalue; rr-viewItemId=628011; rrlevt=1710852141648; _ga_DV4C6GXRL9=GS1.1.1710850287.20.1.1710852141.60.0.0'''
global_cookie = ''
session = None


def get_cookie():
    url = 'https://www.alltime.ru'
    global session
    session = requests.Session()

    '''Ниже нужно проделать все необходимые запросы для получения нужных куки, после каждого необходимо проверять 
    session.cookies, чтобы понять всё ли дейстительно запиывается в куки текущей сессии'''

    response = session.get(url)#requests.get(url)
    ''' 
        ALLTIME_SESSION_SEEN                'https://www.alltime.ru'
        PHPSESSID                           'https://www.alltime.ru'
        srv_id                              'https://www.alltime.ru'
        
        
    '''
    add_cookies = {'rr-testCookie': 'testvalue',
                   'rrpvid': '391578014125557',
                   'rr-popup-shown': '1',
                   '_ga_DV4C6GXRL9': 'GS1.1.1710951527.1.0.1710951527.60.0.0'}
    print([(x.name, x.value) for x in session.cookies])
    for key, value in add_cookies.items():
        session.cookies.set(name=key, value=value)
    print([(x.name, x.value) for x in session.cookies])
    print(session.cookies)
    print('-----------------------------------')


def get_product_id(vendor_code):
    url = 'https://www.alltime.ru/search/?NAME=' + vendor_code
    #print(url)
    global session
    page = session.get(url)
    print(f'{page.request._cookies}')
    soup = BeautifulSoup(page.text, "html.parser")
    try:
        id_number = soup.find('a', class_='catalog-item-link', href=True).get('href').split('/')[-2]
        return id_number
    except AttributeError:
        print(f"Didn't found such vendor code in db: {vendor_code}")


def get_properties(id_number):
    try:
        url = 'https://www.alltime.ru/api/ajax/2020/product-mobile.php?ID=' + id_number + '&version=1.3'
        print(url)
        global session
        #headers = {'Cookie': session.cookies}
        response = session.get(url)# headers=headers)#requests.request("GET", url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            all_properties = get_info_from_page(soup)
            description = get_main_description(soup)
            all_properties['Описание'] = description
            #print(f'{all_properties=}')
            required_properties = {}
            try:
                keys = ['body', 'back_cover', 'mechanism_type', 'bracelet', 'glass', 'additional_functions', 'insertions']
                values = [['Корпус'],
                          ['Описание'],
                          ['Тип механизма'],
                          ['Браслет'],
                          ['Стекло'],
                          ['Календарь', 'Звуковой сигнал'],
                          ['Камень-вставка']]
                for ind, key in enumerate(keys):
                    #print(key)
                    for value in values[ind]:
                        #print(f'\t\t{value}')
                        if key in required_properties:
                            #print(f'{key=} in required_properties')
                            # Если в required_properties уже есть какое-либо значение по этому ключу
                            try:
                                new_value = required_properties[key] + ', ' + all_properties[value]
                                #print(new_value)
                                required_properties[key] = new_value
                            except KeyError:
                                required_properties[key] = required_properties[key]
                        else:
                            #print(f'{key=} NOT in required_properties')
                            # Если такого ключа пока нет в нашем словаре
                            try:
                                required_properties[key] = all_properties[value]
                            except KeyError:
                                required_properties[key] = ''
                        #print(f'\t\t\t\t{required_properties}')
                '''
                required_properties['body'] = all_properties['Корпус']
                required_properties['back_cover'] = all_properties['Описание']
                required_properties['mechanism_type'] = all_properties['Тип механизма']
                required_properties['bracelet'] = all_properties['Браслет']
                required_properties['glass'] = all_properties['Стекло']
                required_properties['additional_functions'] = all_properties['Календарь'] or all_properties['Будильник']
                required_properties['insertions'] = all_properties['Камень-вставка'] if hasattr()'''
            except KeyError:
                #print(f'{required_properties=}')
                pass

            return required_properties # all_properties

        except AttributeError:
            print(f'Something gone wrong with {id_number=}')
            return {}
        '''
        FIXXX ME LATER
        
        Maybe sometimes there is smth wrong with connection or smth, and server sends the empty response => 
        we had empty soup object for parsing => we got empty properties dictionary
        e.g.
        r10018: 591236 -> sometimes
        r18018: 540023 -> always
        T075.220.11.101.01: 628011 -> sometimes (cookie1 - ok)
        AS.PT-SL3 -> sometimes (cookie1 - ok)
        dt_tags = [dt.text for dt in tag.findAll('dt')]           ----->   line 29
        __________________________________________________________________________
        AttributeError: 'NoneType' object has no attribute 'findAll'
        Необходимо проверять, что после соединения нет пустых или неполных элементов хтмл-разметки,
        для того, чтобы избежать ошибки атрибутa.
        '''
    except TypeError:
        print(f"Didn't found such vendor code in db: {vendor_code=}")


def get_info_from_page(soup):
    tag = soup.find('dl')
    dt_tags = [dt.text for dt in tag.findAll('dt')]
    soup_for_dd_tags = BeautifulSoup(str(tag.findAll('dd')), 'html.parser')
    while soup_for_dd_tags.div:
        soup_for_dd_tags.div.decompose()
    dd_tags = [dd.text for dd in soup_for_dd_tags.findAll('dd')]
    properties = dict(zip(dt_tags, dd_tags))

    return properties


def get_main_description(soup):
    description = soup.find('div', class_='page-text')
    while description.p or description.dl:
        try:
            description.p.decompose()
            description.dl.decompose()
        except AttributeError:
            continue
    description = description.text
    description = description[:description.find('Инструкция')].strip('\n').strip()      # try and test: change strip('\n') method on replace('\n\n\n\n\n', '')

    return description

'''

'''