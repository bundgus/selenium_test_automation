from selenium import webdriver
import unittest
import time
from datetime import datetime
import os


class SeleniumBase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome("C:/path/to/chromedriver")
        self.login = 'login goes here'
        self.password = 'password goes here'

        self.base_cp_url = "https://emergo5.sabre.com"

        self.driver.implicitly_wait(60)
        self.logpath = os.path.join('log', 'testlog.log')

        self.testStartTime = str(datetime.now().isoformat(timespec='milliseconds'))

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        with open(self.logpath, 'a') as log_file:
            log_entry = (self.testStartTime
                         + ',' + str(datetime.now().isoformat(timespec='milliseconds'))) \
                         + ',' + '.'.join(str(self.id()).split('.')[1:]) \
                         + ',' + str(round(t, 1))
            print(log_entry)
            log_file.write(log_entry)
            log_file.write('\n')


if __name__ == "__main__":
    unittest.main()
