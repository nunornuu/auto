from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains


driver1 = webdriver.Chrome()
driver1.get('F:/python自动化测试/Python测试/自动化/day01/练习的html/滑动验证/mousedrag.html')
driver1.maximize_window()
tar = driver1.find_element_by_xpath('//*[@id="box"]/div[3]')

ActionChains(driver1).click_and_hold(tar).perform()

ActionChains(driver1).move_by_offset(100, 0).perform()
# ActionChains(driver1).release().perform()
sleep(3)

