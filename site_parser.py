import time
import random
import re
from selenium import webdriver
from pandas import DataFrame
import utils

from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class Parser:
    def __init__(self, driver_type='headless'):
        from config import Config

        self.config = Config()
        self.driver = self.__set_browser_driver(driver_type)
        print("Parser instance created")


    def __set_browser_driver(self, driver_type):
        """
        Handling of browser driver type
        :return:
        """
        if driver_type == 'headless':
            if self.config.os_type == "Windows":
                driver = webdriver.PhantomJS(executable_path='C:/Program Files (x86)/phantomjs/bin/phantomjs.exe',
                                             service_args=self.config.service_args,
                                             desired_capabilities=self.config.dcap)
                driver.set_window_size(1920, 1080)
            else:
                driver = webdriver.PhantomJS(service_args=self.config.service_args,
                                                  desired_capabilities=self.config.dcap)
                driver.set_window_size(1366, 768)
        else:
            #TODO add logic for other webdrivers
            driver = webdriver.Chrome(chrome_options=self.config.chromeOptions,
                                       executable_path='C:\selenium_drivers\chromedriver.exe',
                                       desired_capabilities=self.config.dcap,
                                       service_args=self.config.service_args)
        return driver


    def parse_google(self):
        site = 'http://www.google.com'
        self.driver.get(site)
        print(self.driver.current_url)
        self.driver.save_screenshot(self.config.output_dir + 'test.png')
        self.driver.close()