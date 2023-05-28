import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep

class ButtonsPage(unittest.TestCase):

    # buttons page Constants
    BUTTONS_PAGE = (By.LINK_TEXT, "Buttons")
    PRIMARY_BTN_CLICK = (By.XPATH, "//button[@class='btn btn-lg btn-primary']")
    SUCCESS_BTN_CLICK = (By.XPATH, "//button[@class='btn btn-lg btn-success']")
    INFO_BTN_CLICK = (By.XPATH, "//button[@class='btn btn-lg btn-info']")
    WARNING_BTN_CLICK = (By.XPATH, "//button[@class='btn btn-lg btn-warning']")
    DANGER_BTN_CLICK = (By.XPATH, "//button[@class='btn btn-lg btn-danger']")
    LINK_BTN_CLICK = (By.XPATH, "//button[@class='btn btn-lg btn-link']")
    LEFT_BTN_CLICK = (By.XPATH, "//button[text()='Left']")
    MIDDLE_BTN_CLICK = (By.XPATH, "//button[text()='Middle']")
    RIGHT_BTN_CLICK = (By.XPATH, "//button[text()='Right']")
    BTN_NR1 = (By.XPATH, "//button[text()='1']")
    BTN_NR2 = (By.XPATH, "//button[text()='2']")
    DROPDOWN_CLICK = (By.ID, "btnGroupDrop1")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://formy-project.herokuapp.com/buttons")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_buttons_page_is_loaded(self):
        current_webpage = self.driver.current_url
        expected_url = "https://formy-project.herokuapp.com/buttons"
        assert current_webpage == expected_url, "Url incorrect"

    def test_page_title(self):
        assert "Formy" in self.driver.title, "Wrong page title"

    def test_click_on_every_button(self):
        primary_btn = self.driver.find_element(*self.PRIMARY_BTN_CLICK)
        primary_btn.click()
        primary_btn_text = primary_btn.text
        self.assertEqual(primary_btn_text, "Primary")

        success_btn = self.driver.find_element(*self.SUCCESS_BTN_CLICK)
        success_btn.click()
        success_btn_text = success_btn.text
        self.assertEqual(success_btn_text, "Success")

        info_btn = self.driver.find_element(*self.INFO_BTN_CLICK)
        info_btn.click()
        info_btn_text = info_btn.text
        self.assertEqual(info_btn_text, "Info")

        warning_btn = self.driver.find_element(*self.WARNING_BTN_CLICK)
        warning_btn.click()
        warning_btn_text = warning_btn.text
        self.assertEqual(warning_btn_text, "Warning")

        danger_btn = self.driver.find_element(*self.DANGER_BTN_CLICK)
        danger_btn.click()
        danger_btn_text = danger_btn.text
        self.assertEqual(danger_btn_text, "Danger")

        link_btn = self.driver.find_element(*self.LINK_BTN_CLICK)
        link_btn.click()
        link_btn_text = link_btn.text
        self.assertEqual(link_btn_text, "Link")

        left_button = self.driver.find_element(*self.LEFT_BTN_CLICK)
        left_button.click()
        left_button_text = left_button.text
        assert left_button_text == "Left", "wrong button name"

        middle_button = self.driver.find_element(*self.MIDDLE_BTN_CLICK)
        middle_button.click()
        middle_button_text = middle_button.text
        assert middle_button_text == "Middle", "Wrong button name"

        right_button = self.driver.find_element(*self.RIGHT_BTN_CLICK)
        right_button.click()
        right_button_text = right_button.text
        self.assertEqual(right_button_text, "Right")

        button_nr1 = self.driver.find_element(*self.BTN_NR1)
        button_nr1.click()
        button_nr1_text = button_nr1.text
        assert button_nr1_text == "1", "Wrong name of button nr1"

        button_nr2 = self.driver.find_element(*self.BTN_NR2)
        button_nr2.click()
        button_nr2_text = button_nr2.text
        assert button_nr2_text == "2", "Wrong name of button nr2"

        dropdown_btn = self.driver.find_element(*self.DROPDOWN_CLICK)
        dropdown_btn.click()
        dropdown_btn_text = dropdown_btn.text
        assert dropdown_btn_text == "Dropdown", "Wrong name of button dropdown"

        # visibility of buttons
        self.assertTrue(primary_btn.is_displayed())
        self.assertTrue(success_btn.is_displayed())
        self.assertTrue(info_btn.is_displayed())
        self.assertTrue(warning_btn.is_displayed())
        self.assertTrue(danger_btn.is_displayed())
        self.assertTrue(link_btn.is_displayed())
        self.assertTrue(left_button.is_displayed())
        self.assertTrue(middle_button.is_displayed())
        self.assertTrue(right_button.is_displayed())
        self.assertTrue(button_nr1.is_displayed())
        self.assertTrue(button_nr2.is_displayed())
        self.assertTrue(dropdown_btn.is_displayed())

    def test_dropdown_btn(self):
        drop_down_btn = self.driver.find_element(*self.DROPDOWN_CLICK)
        drop_down_btn.click()
        self.driver.find_element(By.LINK_TEXT, "Dropdown link 1").click()
        drop_down_btn.click()
        try:
            self.driver.find_element(By.LINK_TEXT, "Dropdown link 2").click()
        except:
            print("Element not found")


    def test_button_hoover(self):
        danger_btn = self.driver.find_element(*self.DANGER_BTN_CLICK)
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(danger_btn).perform()
        var = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-lg btn-danger']")))
        self.assertIsNotNone(var)


    def test_primary_status_buttons(self):
        try:
            primary_btn = self.driver.find_element(*self.PRIMARY_BTN_CLICK)
            self.assertFalse(primary_btn.is_enabled())
        except:
            print("The button is enabled")
    def test_right_status_button(self):
        try:
            right_btn = self.driver.find_element(*self.RIGHT_BTN_CLICK)
            self.assertTrue(right_btn.is_enabled())
        except:
            print(" Right button is disabled")

    def test_dropdown_status_button(self):
        try:
            dropdown_btn = self.driver.find_element(*self.DROPDOWN_CLICK)
            self.assertFalse(dropdown_btn.is_enabled())
        except:
            print("Dropdown button is enabled")














