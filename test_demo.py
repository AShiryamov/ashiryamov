import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def before_after():
    print('before_after')
    yield
    print('\nafter_after')

def test_demo1(): #запустить в терминале как pytest -v -s (-s для вывода принтов)
    assert 2 == 2

def test_demo2(before_after):
    assert 1 == 1


