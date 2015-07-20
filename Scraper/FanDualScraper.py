__author__ = 'Mike'

# anchor extraction from html document
from bs4 import BeautifulSoup
import urllib2
import re
import json
import base64
import requests
import cookielib

username = 'michaeliden90@gmail.com'
password = 'igQpbdE3GtouQNG8h'

fanduelurl = 'https://www.fanduel.com/c/CCAuth'

fan_duel_game_url = 'https://www.fanduel.com/e/Game/12564'

# data= {
#     'cc_session_id': 'qleqcfn08cmcq5tldjhn8f0if3',
#     'cc_action': 'cca_login',
#     'cc_failure_url': 'https://www.fanduel.com/p/LoginPp',
#     'cc_success_url': 'https://www.fanduel.com/',
#     'email': username,
#     'password': password,
#     'login': 'Log in',
#     'checkbox_remember': '1'
#     }
#
#
# print requests.get(fanduelurl, data=data).text

webpage = urllib2.urlopen(fan_duel_game_url)
soup = BeautifulSoup(webpage)
script = soup.find('script', text=re.compile('FD\.playerpicker\.allPlayersFullData'))

json_text = re.search(r'^\s*FD\.playerpicker\.allPlayersFullData\s*=\s*({.*?})\s*;\s*$',
                      script.string, flags=re.DOTALL | re.MULTILINE).group(1)

data = json.loads(json_text)

print json.dumps(data,indent=1)
# data.keys()
# for key in data.keys(): print key





