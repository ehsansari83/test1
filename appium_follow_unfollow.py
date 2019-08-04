from appium import webdriver
from time import sleep
import unittest
import pandas as pd
import datetime
import random
from random import randint
from selenium.common.exceptions import NoSuchElementException

#import competitor_list3.CSV

class InstagramFollowTest(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'Galaxy S9'
        desired_caps['noReset'] = 'true'
        desired_caps['appPackage'] = 'com.instagram.android'
        desired_caps['appActivity'] = 'com.instagram.mainactivity.MainActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    def tearDown(self):
        self.driver.quit()

    def test_follow_unfollow(self):
        #finding the search icon and clicking it
        search_box = self.driver.find_element_by_accessibility_id("Search and Explore")
        #search_icon = search_box.find_element_by_id("com.instagram.android:id/tab_icon")
        search_box.click()
        sleep(3)

        #sending keys on the search bar with 'Instagram'
        search_bar = self.driver.find_element_by_id("com.instagram.android:id/action_bar_search_edit_text")
        search_bar.click()
        sleep(2)
        search_bar.send_keys('instagram')
        click_instagram  = self.driver.find_element_by_id("com.instagram.android:id/row_search_user_username")
        click_instagram.click()
        sleep(2)

        #itrating the follow un follow
        #try:
        for i in range(0,100):
            try:
                following_button = self.driver.find_element_by_accessibility_id('Following Instagram button')
                following_button.click()
                sleep(randint(3,6))

                unfollow_confirm = self.driver.find_element_by_id('com.instagram.android:id/follow_sheet_unfollow_row')
                unfollow_confirm.click()
                sleep(randint(3,6))


                follow_button = self.driver.find_element_by_accessibility_id('Follow Instagram button')
                follow_button.click()
                sleep(randint(3,6))

            except NoSuchElementException:
                search_bar = self.driver.find_element_by_id("com.instagram.android:id/action_bar_search_edit_text")
                search_bar.click()
                sleep(2)
                search_bar.send_keys('instagram')
                click_instagram  = self.driver.find_element_by_id("com.instagram.android:id/row_search_user_username")
                click_instagram.click()
                sleep(2)

            print(i)

        for j in range(0,100):
            try:
                follow_button = self.driver.find_element_by_accessibility_id('Follow Instagram button')
                follow_button.click()
                sleep(randint(3,6))

                following_button = self.driver.find_element_by_accessibility_id('Following Instagram button')
                following_button.click()
                sleep(randint(3,6))

                unfollow_confirm = self.driver.find_element_by_id('com.instagram.android:id/follow_sheet_unfollow_row')
                unfollow_confirm.click()
                sleep(randint(3,6))

            except NoSuchElementException:
                search_bar = self.driver.find_element_by_id("com.instagram.android:id/action_bar_search_edit_text")
                search_bar.click()
                sleep(4)
                search_bar.send_keys('instagram')
                click_instagram  = self.driver.find_element_by_id("com.instagram.android:id/row_search_user_username")
                click_instagram.click()
                sleep(4)

            print(i+j)



            #follow_button = self.driver.find_element_by_id('com.instagram.android:id/row_profile_header_button_follow')
            #follow_button.click()
            #sleep(randint(1,3))

            #following_button = self.driver.find_element_by_id('com.instagram.android:id/row_profile_header_button_follow')
            #following.click()
            #sleep(randint(1,3))

            #unfollow_confirm = self.driver.find_element_by_id('com.instagram.android:id/button_positive')
            #unfollow_confirm.click()
            #sleep(randint(1,2))



        print(datetime.datetime.now())
        sleep(3)

if __name__=='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(InstagramFollowTest)
    unittest.TextTestRunner(verbosity = 1).run(suite)
