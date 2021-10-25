from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


# 弹框
# driver1 = webdriver.Chrome()
# driver1.get(r'F:\python自动化测试\Python测试\自动化\自动化测试18\day01\练习的html\弹框的验证\dialogs.html')
#
# alter_btn = driver1.find_element_by_id('alert')
# confirm = driver1.find_element_by_xpath('//*[@id="confirm"]')
# alter_btn.click()
# sleep(3)
# driver1.switch_to.alert.accept()
# sleep(3)
# confirm.click()
# driver1.switch_to.alert.dismiss()
#
# sleep(5)
# driver1.quit()

# 上传文件
driver2 = webdriver.Chrome()
driver2.get(r'F:/python自动化测试/Python测试/自动化/自动化测试18/day01/练习的html/上传文件和下拉列表/autotest.html')
driver2.implicitly_wait(3)

driver2.find_element_by_id('accountID').send_keys('123456')
driver2.find_element_by_id('passwordID').send_keys('uio111')
driver2.find_element_by_id('areaID').click()
driver2.find_element_by_css_selector('#areaID > option[value="beijing"]').click()
driver2.find_element_by_id('areaID').click()
driver2.find_element_by_xpath('//*[@name="u3" and @value="spring"]').click()

driver2.find_element_by_xpath('/html/body/form/table/tbody/tr[7]/td/input').send_keys(r'D:/BaiduNetdiskDownload/testbook/Selenium2+Python自动化测试实战（第二版）.pdf')

sleep(4)
driver2.find_element_by_id('buttonID').click()

driver2.quit()














