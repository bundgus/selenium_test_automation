import os
import unittest
from datetime import datetime
from time import sleep

import selenium_base


class MetaShoppingReport(selenium_base.SeleniumBase):

    # login to cp
    def test_cp_login(self):
        self.driver.get(self.base_cp_url + "/community/login")
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(self.login)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(self.password)
        self.driver.find_element_by_id("loginButton").click()

    def test_launch_meta_shopping_report(self):
        sleep(2)
        self.driver.find_element_by_link_text("SabreSonic® CSS Shopping Cache Report")
        self.driver.get(self.base_cp_url + "/community/launch/693874324")
        page_text = 'Top 3 Daily Cached Shops by Meta'
        self.driver.find_element_by_xpath("//*[contains(text(),'" + page_text + "')]")
        sleep(2)
        screenshot_path = os.path.join(os.getcwd(), 'log',
                                       str(datetime.now().isoformat(timespec='milliseconds')).replace(':', '-')
                                       + '_test_launch_meta_shopping_report.png')
        self.driver.save_screenshot(screenshot_path)


if __name__ == "__main__":
    unittest.main()
