import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep

class FileUploadTests(unittest.TestCase):

    FILE_SELECT = (By.XPATH, "//button[@class='btn btn-secondary btn-choose']")
    RESET_BTN = (By.XPATH, "//button[@class='btn btn-warning btn-reset']")
    UPLOAD_FILES = (By.ID, "file-upload-field")



    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://formy-project.herokuapp.com/fileupload")

    def tearDown(self) -> None:
        self.driver.quit()

    def test_current_url(self):
        try:
            current_url = self.driver.current_url
            expected_url = "https://formy-project.herokuapp.com/fileupload"
            self.assertEqual(current_url,expected_url)
        except:
            print("Error, wrong url ")

    def test_select_file(self):
        file = self.driver.find_element(*self.FILE_SELECT)
        file.send_keys("D:/test.txt")
        reset = self.driver.find_element(*self.RESET_BTN)
        reset.click()
        sleep(3)

    def test_button_name(self):
        btn_reset = self.driver.find_element(*self.RESET_BTN)
        btn_reset_text = btn_reset.text
        self.assertEqual(btn_reset_text, "Reset")
        btn_chose_file = self.driver.find_element(*self.FILE_SELECT)
        btn_chose_file_text = btn_chose_file.text
        self.assertEqual(btn_chose_file_text, "Choose")

    def test_upload_file(self):
        file_input = self.driver.find_element(*self.UPLOAD_FILES)
        file_input.send_keys("D:/test.txt")
        reset = self.driver.find_element(*self.RESET_BTN)
        reset.click()





