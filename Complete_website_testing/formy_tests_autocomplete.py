import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep

class Autocomplete(unittest.TestCase):

    # Autocomplete page Constants
    AUTOCOMPLETE_PAGE = (By.LINK_TEXT, "Autocomplete")
    ADDRESS_FIELD = (By.CLASS_NAME, "form-control")
    STREET_FIELD1 = (By.ID, "street_number")
    STREET_FIELD2 = (By.ID, "route")
    CITY = (By.ID, "locality")
    STATE = (By.ID, "administrative_area_level_1")
    ZIP_CODE = (By.ID, "postal_code")
    COUNTRY = (By.ID, "country")


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://formy-project.herokuapp.com/")

    def tearDown(self):
        self.driver.quit()


    def test_home_page_title(self):
        assert "Formy" in self.driver.title

    def test_url(self):
        actual_url = self.driver.current_url
        expected_url = "https://formy-project.herokuapp.com/"
        assert actual_url == expected_url, "Incorrect url return"

    def test_autocomplete_page(self):
        page = self.driver.find_element(*self.AUTOCOMPLETE_PAGE)
        page.click()
        address = self.driver.find_element(*self.ADDRESS_FIELD)
        address.send_keys("First Street")
        street1 = self.driver.find_element(*self.STREET_FIELD1)
        street1.send_keys("Independentei Street")
        street2 = self.driver.find_element(*self.STREET_FIELD2)
        street2.send_keys("Second Street")
        city = self.driver.find_element(*self.CITY)
        city.send_keys("New York")
        state = self.driver.find_element(*self.STATE)
        state.send_keys("Statele Unite Ale Maramuresului")
        zip_code = self.driver.find_element(*self.ZIP_CODE)
        zip_code.send_keys("123456")
        country = self.driver.find_element(*self.COUNTRY)
        country.send_keys("Romania")
        street1.clear(),street2.clear(),city.clear(),state.clear(),zip_code.clear(),country.clear()
        self.driver.back()





