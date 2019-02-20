#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'justin.郑'

from selenium import webdriver
import time

browser = webdriver.PhantomJS()


def login():
    browser.get("http://www.sucaihuo.com/member/info.html")
    browser.find_element_by_xpath('//*[@id="username"]').send_keys('****@qq.com')
    browser.find_element_by_xpath('//*[@id="pwd"]').send_keys('******')
    browser.find_element_by_xpath('//*[@id="btn_reg"]').click()
    time.sleep(3)

    browser.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/ul/li[2]/a').click()
    time.sleep(3)

    try:
        print('进入')
        browser.find_element_by_css_selector('.today').click()
        time.sleep(3)
        browser.quit()
    except:
        browser.quit()

    print("game over")

if __name__ == '__main__':
    login()