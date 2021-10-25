from selenium import webdriver
from time import sleep


# 切换窗口
driver = webdriver.Chrome()
driver.get(r'F:/python自动化测试/Python测试/自动化/自动化测试18/day01/练习的html/跳转页面/pop.html')
driver.maximize_window()
print(driver.window_handles)
driver.find_element_by_tag_name('a').click()
print(driver.window_handles)
print(driver.current_window_handle)

sleep(4)
driver.switch_to.window(driver.window_handles[0])
sleep(3)
print(driver.name)
print(driver.title)
driver.quit()



