from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup


driver = None


def create_driver():
    """This func creates driver before using other functions"""
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument('--remote-debugging-port=9223')
    options.add_argument('headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--remote-allow-origins=*')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-infobars')
    # options.add_experimental_option("detach", True)
    driver_path = Service('/home/vitaly/PycharmProjects/autospecification_dinara/chromedriver')
    driver = webdriver.Chrome(service=driver_path, options=options)


def get_product_link(vendor_code):
    """
    This func using search mechanism on alltime.ru
    It returns us link on required vendor code
    """
    if isinstance(vendor_code, str):
        pass
    else:
        vendor_code = str(vendor_code)

    url = 'https://www.alltime.ru/search/?NAME=' + vendor_code
    global driver
    driver.get(url)
    page = driver.page_source
    soup = BeautifulSoup(page, "html.parser")
    # 1. Если soup - это пустой объект, значит сервер вернул пустой ответ, соответственно тут нужно
    # будет в дальнейшем поставить проверку и выводить в логи эту ситуацию при её возникновении.
    try:
        # Мы ничего не нашли по вашему запросу «sary132»
        # Пожалуйста, измените поисковой запрос или посмотрите наши рекомендации.
        # Необходимо на этой стадии ОБЯЗАТЕЛЬНО делать проверку на наличие элемента с вышестоящими двумя строчками,
        # для того чтобы не использовать далее ложную модель часов
        link = soup.find('a', class_='catalog-item-link', href=True).get('href')
        # В будущем можно улучшить сам поиск нужного элемента по странице, используя регулярные выражения.
        # На данный момент берётся первый элемент из поисковой выдачи, тк в 90 % случаев он и является целевым.
        return link
    except AttributeError:
        # 2. Если отрабатывает это исключение, значит,
        # что либо выполнился пункт 1(пока не написана отдельная проверка на него),
        # либо через поиск на сайте не найдено похожих артикулов, т.е. нет ни одного элемента 'а' на странице
        # с классом class='catalog-item-link'
        print(f"Didn't found such vendor code in db: {vendor_code}")
        return ''


def get_properties(link):
    """This function returns a dictionary with properties for that watches,
    which you can get using GET-method on <link>.
    It returns an empty dictionary if link is invalid"""
    if isinstance(link, str) and link != '':
        pass
    else:
        # Если в функцию была передана не валидная ссылка/пустая строка вместо ссылки
        return dict()

    url = 'https://www.alltime.ru' + link
    print(f"Page_url is '{url}'")
    soup = get_target_page(url)
    # В дальнейшем, ВОЗМОЖНО, нужно сделать какую-нибудь проверку на корректность soup
    all_properties = get_info_from_page(soup)
    description = get_main_description(soup)
    all_properties['Описание'] = description
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
            for value in values[ind]:
                if key in required_properties:
                    try:
                        new_value = required_properties[key] + ', ' + all_properties[value]
                        required_properties[key] = new_value
                    except KeyError:
                        required_properties[key] = required_properties[key]
                else:
                    try:
                        required_properties[key] = all_properties[value]
                    except KeyError:
                        required_properties[key] = ''
    except KeyError:
        pass

    return required_properties


def get_info_from_page(soup):
    """Вспомогательная функция. Возвращает словарь из всех свойств часов, путем парсинга хтмл-кода страницы,
    за исключением основного описания"""
    tag = soup.find('dl')
    dt_tags = [dt.text for dt in tag.findAll('dt')]
    soup_for_dd_tags = BeautifulSoup(str(tag.findAll('dd')), 'html.parser')
    while soup_for_dd_tags.div:
        soup_for_dd_tags.div.decompose()
    dd_tags = [dd.text for dd in soup_for_dd_tags.findAll('dd')]
    properties = dict(zip(dt_tags, dd_tags))

    return properties


def get_main_description(soup):
    """Вспомогательная функция для получения основного описания для часов, путем парсинга хтмл-кода страницы,
    возвращает строку описания"""
    # 'Данной модели сейчас нет в наличии. Однако она может появиться в скором времени.
    # Если вы хотите, чтобы вас известили о ее появлении, оставьте свой е-мейл в форме ниже.'
    # Если модели нет в наличии, то будет некорректно отрабатывать парсер и вместо необходимого описания
    # будет выдавать вышестоящие строки. Необходимо это пофиксить
    description = soup.find('div', class_='page-text')
    while description.p or description.dl:
        try:
            description.p.decompose()
            description.dl.decompose()
        except AttributeError:
            continue
    description = description.text
    description = description[:description.find('Инструкция')].strip('\n').strip()
    while '\n' in description:
        description = description.replace('\n', '')

    return description


def get_target_page(url):
    """This function returns us a BeautifulSoup objects, containing parsed html-file with the targeting watch,
    which we can get using GET-method on <url>"""
    global driver
    driver.get(url)
    response = driver.page_source
    soup = BeautifulSoup(response, 'html.parser')
    return soup


def quit_driver():
    """We need to quit driver manually after using it"""
    driver.quit()
