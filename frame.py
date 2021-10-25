from selenium import webdriver
from time import sleep


# 框架
# driver1 = webdriver.Chrome()
# driver1.get(r'F:/python自动化测试/Python测试/自动化/自动化测试18/day01/练习的html/frame.html')
# driver1.find_element_by_id('input1').send_keys('sadasd')
# sleep(4)
#
# driver1.close()

driver2 = webdriver.Chrome()
driver2.get(r'F:/python自动化测试/Python测试/自动化/自动化测试18/day01/练习的html/main.html')
a = driver2.find_element_by_id('id1').text
driver2.switch_to.frame(0)
driver2.find_element_by_id('input1').send_keys('where')


# b = of1.find_element_by_id('input1').text

# driver2.execute_script('alert("hah")')
# print(driver2.get_window_size())
# print(driver2.get_window_position())
# print(driver2.get_window_rect())
# driver2.set_window_rect(200, 200)

sleep(5)
driver2.quit()


