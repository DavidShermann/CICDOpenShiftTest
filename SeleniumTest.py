import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
import unittest

from webdriver_manager.chrome import ChromeDriverManager


class test_selenium_weather(unittest.TestCase):
    def setUp(self) -> None:
        option = Options()
        option.add_argument("--headless");
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
        self.driver.get("http://127.0.0.1:5000")

    def test_location_positive(self):
        name = "Haifa"
        self.driver.find_element(By.XPATH, '/html/body/center/form/textarea').send_keys(name)
        self.driver.find_element(By.XPATH, '/html/body/center/form/button').click()
        self.assertEqual(self.driver.find_element(By.XPATH, '/html/body/center/table/tbody/tr[1]/td[1]').text, "Time")

    def test_location_negative(self):
        name = "32142131"
        self.driver.find_element(By.XPATH, '/html/body/center/form/textarea').send_keys(name)
        self.driver.find_element(By.XPATH, '/html/body/center/form/button').click()
        self.assertEqual(self.driver.find_element(By.CLASS_NAME, 'alert').text, "Invalid City/Country Inserted!!!")

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
