"""Scrape Stock Data."""
import configparser
import glob
import json
import os
import requests
from selenium import webdriver
import time


def integrate_csv(dfolder, code, years):
    """Integrate CSV by Code."""
    infile = f'{dfolder}/{code}_*.csv'
    outfile = f'{dfolder}/{code}.csv'

    seconds = 10
    for i in range(1, seconds + 1):
        if len(glob.glob(infile)) == len(years):
            break
        time.sleep(1)
    if i == seconds:
        print (f'timeout. [code][{code}]')
    else:
        # make header
        os.system(f'head -n 2 {dfolder}/{code}_{years[0]}.csv > {outfile}')
        # add body
        os.system(f'tail -n +3 {infile} | grep -v "==>" >> {outfile}')


def main():
    """Main Fuction."""
    # read settings
    config = configparser.ConfigParser()
    config.read('config.ini')
    dfolder = config.get("settings", "dfolder")
    codes = json.loads(config.get("list", "codes"))
    years = json.loads(config.get("list", "years"))

    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    for code in codes:
        try:
            for year in years:
                url = f'https://kabuoji3.com/stock/{code}/{year}/'
                driver.get(url)
                # move to download page
                driver.find_element_by_name('csv').submit()
                # download csv
                driver.find_element_by_name('csv').submit()
        except Exception as e:
            print (f'{code} get failed.')
        else:
            integrate_csv(dfolder, code, years)
        finally:
            os.system(f'rm {dfolder}/{code}_*.csv 2> /dev/null')
    driver.quit()


if __name__ == '__main__':
    main()
