from time import sleep
from selenium import webdriver


driver1 = webdriver.Chrome()
driver1.get('https://www.jd.com/')
driver1.maximize_window()
# driver1.implicitly_wait(15)
# 输入框
driver1.find_element_by_id('key').send_keys('游戏本')
# 点击按钮
driver1.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()

sleep(10)
driver1.execute_script('window.scrollTo(0,1300)')
sleep(1)
driver1.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[14]/div/div[1]/a/img').click()

print(driver1.window_handles)
driver1.switch_to.window(driver1.window_handles[1])
driver1.find_element_by_id("InitCartUrl").click()
sleep(5)


driver1.quit()







