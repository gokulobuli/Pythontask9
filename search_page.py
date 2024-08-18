# search_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_name(self, name):
        name_input = self.wait.until(EC.presence_of_element_located((By.NAME, 'name')))
        name_input.clear()
        name_input.send_keys(name)

    def select_sort_by(self, option_text):
        sort_dropdown = self.wait.until(EC.presence_of_element_located((By.NAME, 'sort')))
        sort_dropdown.send_keys(option_text)

    def select_gender(self, gender):
        gender_dropdown = self.wait.until(EC.presence_of_element_located((By.NAME, 'gender')))
        gender_dropdown.send_keys(gender)

    def click_search(self):
        search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Search"]')))
        search_button.click()
