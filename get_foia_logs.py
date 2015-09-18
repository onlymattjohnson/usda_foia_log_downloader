#!env/bin/python
from datetime import datetime, date
import requests, os

BASE_URL = 'https://www.aphis.usda.gov/foia/foia_logs'
START_YEAR = 2010
START_MONTH = 'October'

def get_urls():
    """ Return a list of all the urls we need """
    # We need the current year to set the range
    current_year = datetime.now().year

    # We need the current month to set the final download
    current_month = datetime.now().strftime("%B")

    years = [n for n in range(START_YEAR,current_year+1)]
    months = [date(2000,s,1).strftime("%B") for s in range(1,13)]

    # Loop through years and months
    url_list = []

    for year in years:
        start_num = 0
        end_num = 12
        if year == START_YEAR:
            # Start with start month
            start_num = months.index(START_MONTH)
        if year == current_year:
            # End with last month
            end_num = months.index(current_month)
        for month in months[start_num:end_num]:
            url_list.append(make_url(year, month))

    return url_list

def make_url(year, month):
    """ Return URL of file for year and month """
    return "%s/%s/%s.xlsx" % (BASE_URL, str(year), month)   

print get_urls()
