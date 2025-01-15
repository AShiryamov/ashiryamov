import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser

def test_open_browser(browser):
    browser.get("https://www.mvideo.ru/?ysclid=m5y518yddk349489640")
    orders = browser.find_element(By.LINK_TEXT, 'Телевизор Hi VHIT-32H229MS')
    orders.click()
    adress = browser.find_element(By.LINK_TEXT, 'Телевизор Hi VHIT-32H229MS')
    assert adress.text == 'Телевизор Hi VHIT-32H229MS'
