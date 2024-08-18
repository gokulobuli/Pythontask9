# test_search.py
import pytest
from selenium import webdriver
from search_page import SearchPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_search(driver):
    driver.get("https://www.imdb.com/search/name/")

    # Step 2: Use the SearchPage class to perform the search
    search_page = SearchPage(driver)
    search_page.enter_name('Tom Hanks')
    search_page.select_sort_by('Birth Date')
    search_page.select_gender('Male')
    search_page.click_search()


