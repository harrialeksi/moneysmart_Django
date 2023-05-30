# PROJECT: MoneySmart
# AUTHOR: @superbaby81230
# CREATED: 14/5/2023
# MODIFIED: 21/5/2023

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import requests
from bs4 import BeautifulSoup


def get_cards(url):

    # initialize the webdriver
    driver = webdriver.Chrome()
    # navigate to the webpage
    driver.get(url)

    # click "Load more" button amap
    moreButton = driver.find_elements("xpath", '//div[@class="pagination-button"]/button')
    
    while moreButton:
        driver.execute_script('arguments[0].click();', moreButton[0])
        # Delay 3s
        time.sleep(3)
        moreButton = driver.find_elements("xpath", '//div[@class="pagination-button"]/button')

    # find anchor with "More detail" text-it's class name ="link-toggle"
    details = driver.find_elements("xpath", '//a[@class="link-toggle"]')
     # print the contents of each element
    
    for element in details:
        #click buttons
        driver.execute_script('arguments[0].click();', element)
        # time.sleep(1)

    # Get card Data
    cards = driver.find_elements(By.CLASS_NAME, 'listing-card')

    data = []
    for i, card in enumerate(cards):
        try:
            img_src = card.find_element(
                'xpath', './/div[@class="listing-card__image"]//img').get_attribute("src")
        except NoSuchElementException:
            img_src = None
        try:
            disclosure = card.find_element(
                By.CLASS_NAME, 'listing-card__disclosure').text
        except NoSuchElementException:
            disclosure = None
        try:
            title = card.find_element(
                'xpath', './/h2[@class="listing-card__title"]').text
        except NoSuchElementException:
            title = None
        try:
            badge_execlusive = card.find_element(
                'xpath', './/div[@class="badge badge--exclusive"]//div[@class="badge__label"]').text
        except NoSuchElementException:
            badge_execlusive = None
        try:
            badge_label = card.find_element(
                'xpath', './/div[@class="badge"]//div[@class="badge__label"]').text
        except NoSuchElementException:
            badge_label = None
        try:
            badge_primary = card.find_element(
                'xpath', './/div[@class="badge badge--primary"]//div[@class="badge__label"]').text
        except NoSuchElementException:
            badge_primary = None
        try:
            snippet = card.find_element(
                'xpath', './/div[@class="promotion-snippet__content"]').get_attribute('innerHTML')
        except NoSuchElementException:
            snippet = None
        try:
            snippet_img = card.find_element(
                'xpath', './/div[@class="promotion-snippet__image"]//img').get_attribute("src")
        except NoSuchElementException:
            snippet_img = None

        card_usp = card.find_elements(By.CLASS_NAME, 'listing-card__usp-group')
        card_usp_data = []
        for i, element in enumerate(card_usp):
            card_usp_data.append({'ratio':  element.find_element('xpath', './/dd').text, 'text': element.find_element('xpath', './/dt').text})

        try:
            promotion = card.find_element('xpath', './/li[@class="tab-list is-active"][@data-id="promotions"]').get_attribute('innerHTML')
        except NoSuchElementException:
            promotion = None
        try:
            keyFeatures = card.find_element('xpath', './/li[@class="tab-list"][@data-id="key_features"]').get_attribute('innerHTML')
        except NoSuchElementException:
            keyFeatures = None
        try:
            annualInterest = card.find_element('xpath', './/li[@class="tab-list"][@data-id="annual_interest_rate_and_fees"]').get_attribute('innerHTML')
        except NoSuchElementException:
            annualInterest = None
        try:
            incomeRequirement = card.find_element('xpath', './/li[@class="tab-list"][@data-id="minimum_income_requirements"]').get_attribute('innerHTML')
        except NoSuchElementException:
            incomeRequirement = None
        try:
            cardAssociation = card.find_element('xpath', './/li[@class="tab-list"][@data-id="card_association"]').get_attribute('innerHTML')
        except NoSuchElementException:
            cardAssociation = None
        try:
            wirelessPayment = card.find_element('xpath', './/li[@class="tab-list"][@data-id="wireless_payment"]').get_attribute('innerHTML')
        except NoSuchElementException:
            wirelessPayment = None
        try:
            repayment = card.find_element('xpath', './/li[@class="tab-list"][@data-id="repayment_summary"]').get_attribute('innerHTML')
        except NoSuchElementException:
            repayment = None
        try:
            travel_inconvenience = card.find_element('xpath', './/li[@class="tab-list"][@data-id="travel_inconvenience"]').get_attribute('innerHTML')
        except NoSuchElementException:
            travel_inconvenience = None
        try:
            interestRate = card.find_element('xpath', './/li[@class="tab-list"][@data-id="interest_rate"]').get_attribute('innerHTML')
        except NoSuchElementException:
            interestRate = None
        try:
            bonus_interest_rate = card.find_element('xpath', './/li[@class="tab-list"][@data-id="bonus_interest_rate"]').get_attribute('innerHTML')
        except NoSuchElementException:
            bonus_interest_rate = None

        data.append({
            "img_src": img_src,
            "disclosure": disclosure,
            "title": title,
            "badge_execlusive": badge_execlusive,
            "badge_label": badge_label,
            "badge_primary": badge_primary,
            "snippet": snippet,
            "snippet_img": snippet_img,
            'usp': card_usp_data,
            'promotion': promotion,
            'keyFeatures': keyFeatures,
            'annualInterest': annualInterest,
            'incomeRequirement': incomeRequirement,
            'cardAssociation': cardAssociation,
            'wirelessPayment': wirelessPayment,
            'repayment': repayment,
            'travel_inconvenience': travel_inconvenience,
            "interestRate": interestRate,
            "bonusInterestRate": bonus_interest_rate
        })

    driver.quit()
    return data
