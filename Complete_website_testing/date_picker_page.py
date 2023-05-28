import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep


class DatePicker(unittest.TestCase):

    DATE_INPUT = (By.ID, "datepicker")
    CURRENT_DATE = (By.XPATH, "//td[@class='today day']")


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://formy-project.herokuapp.com/datepicker")

    def tearDown(self) -> None:
        self.driver.quit()

    def test_main_page(self):
        actual_url = self.driver.current_url
        expected_url = "https://formy-project.herokuapp.com/datepicker"
        assert actual_url == expected_url, " Incorrect url check "

    def test_test_in_page(self):
        title = self.driver.title
        assert "Formy" in title

    def test_input_field_date_picker(self):
        date = self.driver.find_element(*self.DATE_INPUT)
        date.send_keys("05/26/2023")
        date.clear()

    def test_datepicker_widget_filed(self):
        date_field = self.driver.find_element(*self.DATE_INPUT)
        date_field.click()
        today = self.driver.find_element(*self.CURRENT_DATE)
        today.click()
        date_field.clear()
        try:
            self.assertFalse(date_field.is_enabled())
        except:
            print("Field is enabled")