import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep

class RadioButtons(unittest.TestCase):

    RADIO_BTN1 = (By.ID, "radio-button-1")
    RADIO_BTN2 = (By.XPATH, "//input[@value='option2']")
    RADIO_BTN3 = (By.NAME, "exampleRadios")


    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://formy-project.herokuapp.com/radiobutton")
        self.driver.implicitly_wait(15)


    def tearDown(self) -> None:
        self.driver.quit()


    def test_main_page(self):
        current_url = self.driver.current_url
        expected_url = "https://formy-project.herokuapp.com/radiobutton"
        self.assertEqual(current_url,expected_url)

    def test_page_title(self):
        assert "Formy" in self.driver.title

    def test_select_radio_button_1(self):
        btn1 = self.driver.find_element(*self.RADIO_BTN1)
        btn1.click()
        try:
            self.assertFalse(btn1.is_displayed())
        except:
            print("Radio button 1 is displayed")
        try:
            self.assertFalse(btn1.is_enabled())
        except:
            print("Radio button 1 is enabled")
        try:
            self.assertFalse(btn1.is_selected())
        except:
            print("Radio button 1 is selected")


    def test_select_radio_button_2(self):
        btn2 = self.driver.find_element(*self.RADIO_BTN2)
        btn2.click()
        try:
            self.assertFalse(btn2.is_displayed())
        except:
            print("Radio button 2 is displayed")
        try:
            self.assertFalse(btn2.is_enabled())
        except:
            print("Radio button 2 is enabled")
        try:
            self.assertFalse(btn2.is_selected())
        except:
            print("Radio button 2 is selected")


    def test_select_radio_button_3(self):
        btn3 = self.driver.find_element(*self.RADIO_BTN3)
        btn3.click()
        try:
            self.assertFalse(btn3.is_displayed())
        except:
            print("Radio button 3 is displayed")
        try:
            self.assertFalse(btn3.is_enabled())
        except:
            print("Radio button 3 is enabled")
        try:
            self.assertFalse(btn3.is_selected())
        except:
            print("Radio button 3 is selected")

    def test_radio_buttons_text(self):
        btn1 = self.driver.find_element(*self.RADIO_BTN1)
        btn1_text = btn1.text
        btn2 = self.driver.find_element(*self.RADIO_BTN2)
        btn2_text = btn2.text
        btn3 = self.driver.find_element(*self.RADIO_BTN3)
        btn3_text = btn3.text
        try:
            assert "Radio button 1" in btn1_text
        except:
            print("Assertion error, incorrect text of the element ")

        try:
            assert "Radio button 2" in btn2_text
        except:
            print("Error, incorrect text of radio button 2")

        try:
            assert "Radio button 3" in btn3_text
        except:
            print("Error, the text on radio button 3 is incorrect ")



