from bs4 import BeautifulSoup
import parsing_functions as pf
import excel_functions as ef



# 'Спецификация Tissot Daghaya.xlsx'    B, 10, 64
#ef.use_excel_file('Спецификация Tissot Daghaya.xlsx')


'''<<<https://www.alltime.ru/watch/d1-milano/UTBJ33/659991/>>>
in this request in browser we used only such string of cookies(see below) to get info from 
<<<https://www.alltime.ru/api/ajax/2020/product-mobile.php?ID=659991&version=1.3>>>:

see used cookies below:
------------------------------------------------------------------------------------------------------------------------>
rr-popup-shown=1; srv_id=srv4; PHPSESSID=of44iq19i7th405s2ipduuqle3; ALLTIME_CITY=54736769eec61c79f70f43079869af01; ALLTIME_SESSION_SEEN=2f02c34deb11aab913047d4897d2b977; rr-testCookie=testvalue; rrpvid=391578014125557; _ga_DV4C6GXRL9=GS1.1.1710951527.1.0.1710951527.60.0.0; _ga=GA1.1.1859146796.1710951527; rcuid=65fb0c042878efb288046c93; rr-viewItemId=659991; rrviewed=659991; rrlevt=1710951527373
------------------------------------------------------------------------------------------------------------------------>
try to prettify it:
    +++
    + srv_id=srv4                                                       -> alltime.ru
    + PHPSESSID=of44iq19i7th405s2ipduuqle3                              -> alltime.ru
    + ALLTIME_CITY=54736769eec61c79f70f43079869af01                     -> alltime.ru
    + ALLTIME_SESSION_SEEN=2f02c34deb11aab913047d4897d2b977             -> alltime.ru
    +++
      rr-testCookie=testvalue                                           -> retailrocket
      rrpvid=391578014125557                                            -> retailrocket
      rr-popup-shown=1                                                  -> retailrocket
      
      _ga_DV4C6GXRL9=GS1.1.1710951527.1.0.1710951527.60.0.0             -> google analytics
    
so. we need to do requests for getting these cookies with first connection to server
so. we need to find which children-requests do it after first reqests in this doc-string
'''

pf.get_cookie()
vendor_code = 'T1010103345100'
id_number = pf.get_product_id(vendor_code)
print(f'{vendor_code}: {id_number}')
print('___________________________________')
tag = pf.get_properties(id_number)
print(f'required_properties = {tag}')
print('***********************************')
