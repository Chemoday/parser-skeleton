import time
import random
import re
from selenium import webdriver
import utils

from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import os

class Parser:
    def __init__(self,
                 driver_type='phantom',
                 browser_mode='headless'):
        from config import Config

        self.config = Config()
        self.driver = self.__set_browser_driver(driver_type, browser_mode)
        print("Parser instance created")


    def __set_browser_driver(self, driver_type, browser_mode):
        """
        Handling of browser driver type
        :return:
        """
        if driver_type == 'phantom':
            if self.config.os_type == "Windows":
                driver = webdriver.PhantomJS(executable_path='C:/Program Files (x86)/phantomjs/bin/phantomjs.exe',
                                             service_args=self.config.service_args,
                                             desired_capabilities=self.config.dcap,
                                             service_log_path=os.path.devnull)
                driver.set_window_size(1920, 1080)
            else:
                driver = webdriver.PhantomJS(service_args=self.config.service_args,
                                                  desired_capabilities=self.config.dcap,
                                             service_log_path=os.path.devnull)
                driver.set_window_size(1366, 768)

        elif driver_type == 'firefox':
            print('running firefox')
            from selenium.webdriver.firefox.options import Options
            firefox_options = Options()
            firefox_options.add_argument('--disable-logging')
            if browser_mode == 'headless':
                firefox_options.headless = True

            driver = webdriver.Firefox(firefox_options=firefox_options,
                                       executable_path=self.config.firefox_path,
                                       service_log_path=os.path.devnull)

        elif driver_type == 'chrome':
            from selenium.webdriver.chrome.options import Options
            print('running chrome')
            chrome_options = Options()

            if browser_mode == 'headless':
                chrome_options.headless = True

            driver = webdriver.Chrome(chrome_options=chrome_options,
                                       executable_path=self.config.chrome_path)
                                       # desired_capabilities=self.config.dcap,
                                       # service_args=self.config.service_args)
        else:
            raise AttributeError('Driver type should be | phantom | firefox | chrome')

        return driver


    def parse_google(self):
        site = 'http://www.google.com'
        self.driver.get(site)
        print(self.driver.current_url)
        self.driver.save_screenshot(self.config.output_dir + 'test.png')
        self.driver.close()