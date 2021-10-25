from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep


driver1 = webdriver.Chrome()
driver1.get('https://www.taobao.com/')
driver1.maximize_window()
# driver1.implicitly_wait(15)
# 输入框
driver1.find_element_by_id('q').send_keys('游戏本')
driver1.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()

print(driver1.window_handles)
# driver1.switch_to.window(driver1.window_handles[0])
driver1.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys('123')
sleep(1)
driver1.find_element_by_id('fm-login-password').send_keys('123')
sleep(1)
driver1.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
tar = driver1.find_element_by_xpath('//*[@id="nc_1_n1z"]')

ActionChains(driver1).click_and_hold(tar).perform()

ActionChains(driver1).move_by_offset(100, 0).perform()





