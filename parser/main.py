import os
import csv
import sys
import time
import re
import pickle

from sys import platform
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

"""Settings."""

DRIVER_PATH = './drivers/geckodriver_'
HEADLESS = True
TABLE_PATH = './tables/'
URL = 'https://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/?brand=apple'
LOAD_TIMEOUT = 5

"""HTML elements."""

# 'block': ['class', 'tag', 'tag_class' (optional)]
elements = {
  'name': ['catalog-product__name', 'span'],
  'price': ['product-buy__price-wrap', 'div', 'product-buy__price']
}

content_class = 'catalog-products'

"""Table"""

columns = {
  'name': ['model', 'capacity', 'display', 'color', 'chip', 'ram', 'sim_card', 'resolution', 'camera', 'battery'],
  'price': ['price', 'old_price']
}

patterns = {
  'name': '^(?P<display>.+)" Смартфон Apple iPhone (?P<model>.+) (?P<capacity>\d+) ГБ (?P<color>.+) '
  '\[ядер - (?P<chip>\d|.+\)),(?: (?P<ram>.+) Гб,)?(?: (?P<sim_card>.+) SIM,)?.*, (?P<resolution>.+x.+), '
  'камера (?P<camera>.+) Мп,.*,(?: (?P<battery>.+) мА\*ч)?.*$',
  'price': '^(?P<price>.+) ₽(?P<old_price>.+)?$'
}

titles = {
  'model': 'Модель',
  'capacity': 'Объём памяти, Гб',
  'display': 'Диагональ экрана, дюйм',
  'color': 'Цвет',
  'chip': 'Число ядер',
  'ram': 'RAM, Гб',
  'sim_card': 'SIM',
  'resolution': 'Разрешение экрана',
  'camera': 'Основная камера, Мп',
  'battery': 'Емкость аккумулятора, мА*ч',
  'price': 'Цена, руб.',
  'old_price': 'Цена (без скидки), руб.'
}

"""System."""

def platform_postfix():
  pname = platform
  label = ''

  if pname == 'linux':
    label = pname
  elif pname == 'win32':
    label = pname + '.exe'
  else:
    sys.exit('This platform is not supported.')

  return label

"""Dictionary functions."""

def print_dct(dct, indent="\t"):
  for key, value in dct.items():
    print(key)

    for e in value:
      print(indent + e)

def merge_dct(dcta, dctb):
  dct = {}

  if not dcta:
    dct = dctb
  else:
    for key, value in dcta.items():
      dct[key] = value + dctb[key]

  return dct

def save_dct(dct, filename='products'):
  with open(filename + '.pkl', 'wb') as f:
    pickle.dump(dct, f)

def load_dct(path):
  with open(path, 'rb') as f:
    dct = pickle.load(f)

  return dct

"""Web page."""

def get_page(driver, structure, page=1):
  driver.get(URL + '&p=' + str(page))
  driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

  sleep(LOAD_TIMEOUT)

  source = driver.page_source
  bs = BeautifulSoup(source, features='lxml')

  result = {}

  if bs.find_all(attrs = {'class': content_class}):
    for key, value in structure.items():
      result[key] = []
      size = len(value)
  
      for e in bs.find_all(attrs = {'class': value[0]}):
        tag_class = ''
  
        if size == 3:
          tag_class = value[2]
  
        tag = e.find(value[1], attrs = {'class': tag_class})
  
        result[key].append(tag.text)

  return result

def get_products(structure, page_count='all'):
  p = 1
  prod = {}

  """Load webdriver (gecko)."""

  optns = webdriver.firefox.options.Options()

  if HEADLESS:
    optns.add_argument('--headless')

  optns.add_argument('--disable-blink-features=AutomationControlled')

  srvc = webdriver.firefox.service.Service(executable_path=DRIVER_PATH + platform_postfix(), log_path=os.devnull)
  drvr = webdriver.Firefox(service=srvc, options=optns)

  while True:
    if page_count != 'all' and page_count + 1 == p:
      break

    prod_page = get_page(drvr, structure, p)

    if not prod_page:
      break

    prod = merge_dct(prod, prod_page)

    p += 1

  drvr.quit()

  return prod

"""Regex."""

def parse_products(dct):
  table = {}

  def get_columns(dct, section):
    subtable = {}

    for c in columns[section]:
      subtable[c] = []

    for e in dct[section]:
      match = re.match(patterns[section], e)
      dctmatch = match.groupdict()

      for key in subtable:
        group = dctmatch[key]

        if group is None:
          group = ''

        subtable[key].append(group)

    return subtable

  for key in columns:
    table.update(get_columns(dct, key))

  return table

"""Export."""

def export_csv(dct, postfix='table'):
  filename = time.strftime('%Y_%m_%d-%H_%M_%S') + '-' + postfix + '.csv'

  rows = zip(*(value.insert(0, titles[key]) or value for key, value in dct.items()))

  with open(TABLE_PATH + filename, 'w') as f:
    tablewriter = csv.writer(f)

    for r in rows:
      tablewriter.writerow(r)

"""Main."""

if __name__ == '__main__':
  products = get_products(elements)

  export_csv(parse_products(products))
