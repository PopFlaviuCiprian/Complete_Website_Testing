import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep

class EnabledDisabled(unittest.TestCase):

    FIELD_INPUT_1 = (By.XPATH, "//input[@class='form-control']")
    FIELD_INPUT_2 = (By.ID, "input")


    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://formy-project.herokuapp.com/enabled")
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_page_title(self):
        assert "Formy" in self.driver.title, "Incorrect tile"

    def test_page_is_correct(self):
        actual_url = self.driver.current_url
        expected_url = "https://formy-project.herokuapp.com/enabled"
        assert actual_url == expected_url, "Url error"

    def test_if_field_1_is_enabled(self):
        field_1 = self.driver.find_element(*self.FIELD_INPUT_1)
        try:
            self.assertTrue(field_1.is_enabled())
        except:
            print("Field input is disabled")

    def test_if_field_2_is_enabled(self):
        try:
            field_2 = self.driver.find_element(*self.FIELD_INPUT_2)
            self.assertFalse(field_2.is_enabled())
        except:
            print("Field is enabled")

