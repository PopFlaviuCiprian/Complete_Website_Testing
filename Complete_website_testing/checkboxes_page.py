import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep

class CheckboxPage(unittest.TestCase):

    HIDDEN_MENU = (By.XPATH, "//span[@class='navbar-toggler-icon']")
    CHECKBOX_1 = (By.ID, "checkbox-1")
    CHECKBOX_2 = (By.ID, "checkbox-2")
    CHECKBOX_3 = (By.ID, "checkbox-3")


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://formy-project.herokuapp.com/checkbox")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_page_is_loaded(self):
        current_page = self.driver.current_url
        expected_url = "https://formy-project.herokuapp.com/checkbox"
        assert current_page == expected_url, "Incorrect url"

    def test_main_title(self):
        assert "Formy" in self.driver.title, "Wrong page title"

    def test_hidden_menu(self):
        try:
            hidden_menu = self.driver.find_element(*self.HIDDEN_MENU)
            self.assertTrue(hidden_menu.is_displayed())
        except:
            print("Element is not displayed")

    def test_element_is_enabled(self):
        try:
            element = self.driver.find_element(*self.HIDDEN_MENU)
            self.assertFalse(element.is_enabled())
        except:
            print("The element is enabled")

    def test_checkbox_1_is_selected(self):
        checkb1 = self.driver.find_element(*self.CHECKBOX_1)
        checkb1.click()
        try:
            self.assertFalse(checkb1.is_selected())
        except:
            print("The checkbox 1 is selected")

    def test_checkbox_nr1_text(self):
        try:
            check_b1 = self.driver.find_element(*self.CHECKBOX_1)
            check_box_text = check_b1.text
            assert check_box_text == "Checkbox1"
        except:
            print("Assertion error, there are too many spaces in Checkbox nr. 1 text")

    def test_checkbox_nr1_is_visible(self):
        check_box_nr1 = self.driver.find_element(*self.CHECKBOX_1)
        self.assertTrue(check_box_nr1.is_displayed())

    def test_checkbox_nr1_is_enabled(self):
        try:
            element = self.driver.find_element(*self.CHECKBOX_1)
            self.assertFalse(element.is_enabled())
        except:
            print("The Checkbox 1  is enabled")


    def test_checkbox_nr2_is_selected(self):
        check_b2 = self.driver.find_element(*self.CHECKBOX_2)
        check_b2.click()
        # sleep(3)
        try:
            self.assertFalse(check_b2.is_selected())
        except:
            print("The checkbox nr2 is selected")

    def test_checkbox_nr2_text(self):
        try:
            check_b2 = self.driver.find_element(*self.CHECKBOX_2)
            check_box_text = check_b2.text
            assert check_box_text == "Checkbox2"
        except:
            print("Assertion error, there are too many spaces in Checkbox nr.2 text even if the text is correct")

    def test_checkbox_nr2_is_visible(self):
        check_box_nr2 = self.driver.find_element(*self.CHECKBOX_2)
        self.assertTrue(check_box_nr2.is_displayed())

    def test_checkbox_nr2_is_enabled(self):
        try:
            element = self.driver.find_element(*self.CHECKBOX_2)
            self.assertFalse(element.is_enabled())
        except:
            print("The Checkbox 2 is enabled")

    def test_checkbox_nr3_is_selected(self):
        check_b3 = self.driver.find_element(*self.CHECKBOX_3)
        check_b3.click()
        # sleep(3)
        try:
            self.assertFalse(check_b3.is_selected())
        except:
            print("The checkbox nr3 is selected")

    def test_checkbox_nr3_text(self):
        try:
            check_b3 = self.driver.find_element(*self.CHECKBOX_3)
            check_box_text = check_b3.text
            assert check_box_text == "Checkbox3"
        except:
            print("Assertion error, there are too many spaces in Checkbox nr 3 text even if the text is correct")

    def test_checkbox_nr3_is_visible(self):
        check_box_nr3 = self.driver.find_element(*self.CHECKBOX_3)
        self.assertTrue(check_box_nr3.is_displayed())

    def test_checkbox_nr3_is_enabled(self):
        try:
            element = self.driver.find_element(*self.CHECKBOX_3)
            self.assertTrue(element.is_enabled())
        except:
            print("The Checkbox 3 is disabled")


