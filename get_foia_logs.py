#!env/bin/python

import requests, os
from bs4 import BeautifulSoup as bs4

url = 'https://www.aphis.usda.gov/wps/portal/aphis/resources/lawsandregs/sa_foia/ct_foia_logsprint'

if not os.path.exists('logs'):
    os.makedirs('logs')

result = requests.get(url, verify=False)
soup = bs4(result.text,'html.parser')


print soup.prettify().encode('utf-8')
