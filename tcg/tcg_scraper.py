import re
from time import sleep

from bs4 import BeautifulSoup as B
from decouple import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TcgScraper:
    def __init__(self):
        self.GOOGLE_CHROME_BIN = config('GOOGLE_CHROME_BIN')
        self.GOOGLE_CHROME_SHIM = config('GOOGLE_CHROME_SHIM')
        self.chrome_options = Options()
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument('--disable-gpu')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument("--headless")
        self.ignored_exceptions = (NoSuchElementException, StaleElementReferenceException, )

    def get_driver(self):
        if self.GOOGLE_CHROME_SHIM != 'Local':
            self.chrome_options.binary_location = self.GOOGLE_CHROME_BIN
            driver = webdriver.Chrome(options=self.chrome_options)
        else:
            driver = webdriver.Chrome(executable_path='chromeDriver/chromedriver', options=self.chrome_options)

        return driver

    @staticmethod
    def quit_driver(driver):
        driver.quit()

    @staticmethod
    def query(driver, value):
        if value is not None:
            driver.execute_script("$(arguments[0]).click();", value)
        else:
            return 'Error in value'

    @staticmethod
    def get_url(driver, url):

        driver.get(url)

    def open_filters(self, driver):
        your_element = WebDriverWait(driver, timeout=30, ignored_exceptions=self.ignored_exceptions).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="product-price-table"]/div[1]/button')))

        your_element.click()

        # self.driver.find_element_by_xpath('//*[@id="product-price-table"]/div[1]/button').click()

    @staticmethod
    def get_card_data(driver, query_condition):
        print(f'Searching for this condition {query_condition}')
        sleep(5)
        page_source = driver.page_source
        sleep(5)
        soup = B(page_source, 'html.parser')
        cards = soup.find_all('div', {'class': 'product-listing'})
        seller_data_list = []
        for card in cards:
            condition = card.find('a', {'class': 'condition'}).text

            if query_condition == condition:

                seller_name = card.find('a', {'class': 'seller__name'}).text.strip()
                if seller_name != 'Moose Loot' and seller_name != 'Moose Loot Direct':
                    try:
                        total_sales = card.find('span', {'class': 'seller__sales'}).text
                        total_sales = [i for i in total_sales if i.isnumeric()]
                        total_sales = int(''.join(total_sales))
                        price = card.find('span', {'class': 'product-listing__price'}).text.strip('$')
                        shipping_string = card.find('span', {'class': 'product-listing__shipping'}).text
                        if 'included' in shipping_string.lower() or 'free shipping' in shipping_string.lower():
                            shipping = 0
                        else:
                            shipping = re.findall(r"[-+]?\d*\.\d+|\d+", shipping_string)
                            shipping = ''.join(shipping)

                        total_price = float(price) + float(shipping)

                        seller_data_list.append(
                            {
                                'price': total_price,
                                'gold': True if total_sales >= 10000 else False,
                            }
                        )

                        if len(seller_data_list) == 5:
                            break
                    except AttributeError:
                        continue
                else:
                    # Filter for query failed for some reason
                    print('Query Failed')
        print(seller_data_list)
        return seller_data_list

    def filter_value(self, driver, query):

        condition_list = ['Lightly Played Foil', 'Near Mint Foil', 'Moderately Played Foil',
                          'Heavily Played Foil', 'Damaged Foil']

        if query != 'Foil' and query in condition_list:
            query = query.replace('Foil', '').strip()

        elif query != 'Foil' and query not in condition_list:
            pass
        else:
            pass
        q = {
            # 'next_page': self.driver.find_element_by_xpath('//*[@id="priceTableContainer"]/div/nav/ul/a[4]'),
            'clear': driver.find_element_by_xpath('//*[@id="detailsFilters"]/div/div/ul[5]/li[1]/a'),
            'Near Mint': driver.find_element_by_xpath('//*[@id="detailsFilters"]/div/div/ul[5]/li[2]/a'),
            'Lightly Played': self.wait(driver, '//*[''@id="detailsFilters"]/div/div/ul[5]/li[3]/a'),
            'Moderately Played': self.wait(driver, '//*[@id="detailsFilters"]/div/div/ul[5]/li[4]/a'),
            'Heavily Played': self.wait(driver, '//*[@id="detailsFilters"]/div/div/ul[5]/li[5]/a'),
            'Damaged': driver.find_element_by_xpath('//*[@id="detailsFilters"]/div/div/ul[5]/li[6]/a'),
            'Unopened': driver.find_element_by_xpath('//*[@id="detailsFilters"]/div/div/ul[5]/li[7]/a'),
            'Normal': driver.find_element_by_xpath('//*[@id="detailsFilters"]/div/div/ul[4]/li[2]/a'),
            'Foil':  driver.find_element_by_xpath('//*[@id="detailsFilters"]/div/div/ul[4]/li[3]/a'),
            'four_or_more': driver.find_element_by_xpath('//*[@id="detailsFilters"]/div/div/ul[2]/li[2]/a'),
            'English': driver.find_element_by_xpath('//*[@id="detailsFilters"]/div/div/ul[6]/li[2]/a'),
            'Chinese (S)': driver.find_element_by_xpath('//*[@id="detailsFilters"]/div/div/ul[6]/li[3]/a'),
            'all_non_english': driver.find_element_by_xpath('//*[@id="detailsFilters"]/div/div/ul[6]/li[4]/a'),
            'Chinese (T)': driver.find_element_by_xpath('//*[@id="detailsFilters"]/div/div/ul[6]/li[5]/a'),
            'French': driver.find_element_by_xpath('//*[@id="detailsFilters"]/div/div/ul[6]/li[6]/a'),
            'German': driver.find_element_by_xpath('//*[@id="detailsFilters"]/div/div/ul[6]/li[7]/a'),
            'Italian': driver.find_element_by_xpath('//*[@id="detailsFilters"]/div/div/ul[6]/li[8]/a'),
            'Japanese': driver.find_element_by_xpath('//*[@id="detailsFilters"]/div/div/ul[6]/li[9]/a'),
            'Korean': driver.find_element_by_xpath('//*[@id="detailsFilters"]/div/div/ul[6]/li[10]/a'),
            'Portuguese': driver.find_element_by_xpath('//*[@id="detailsFilters"]/div/div/ul[6]/li[11]/a'),
            'Russian': driver.find_element_by_xpath('//*[@id="detailsFilters"]/div/div/ul[6]/li[12]/a'),
            'Spanish': driver.find_element_by_xpath('//*[@id="detailsFilters"]/div/div/ul[6]/li[13]/a'),
        }

        return q.get(query)

    def wait(self, driver, path):
        x_element = WebDriverWait(driver, timeout=30, ignored_exceptions=self.ignored_exceptions).until(
            expected_conditions.presence_of_element_located((
                By.XPATH, path)))
        return x_element





