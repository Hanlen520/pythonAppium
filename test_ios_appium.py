from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import time


# 获得机器屏幕大小x,y
def getSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    print(x, y)
    return x, y


# 屏幕向上滑动
def swipeUp(driver, t):
    l = getSize(driver)
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.75)  # 起始y坐标
    y2 = int(l[1] * 0.25)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)


# 屏幕向下滑动
def swipeDown(driver, t):
    l = getSize(driver)
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.25)  # 起始y坐标
    y2 = int(l[1] * 0.75)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)


# 屏幕向左滑动
def swipLeft(driver, t):
    l = getSize(driver)
    x1 = int(l[0] * 0.75)   # x 坐标
    y1 = int(l[1] * 0.5)    # y 坐标
    x2 = int(l[0] * 0.05)   # x 坐标
    driver.swipe(x1, y1, x2, y1, t)


# 屏幕向右滑动
def swipRight(driver, t):
    l = getSize(driver)
    x1 = int(l[0] * 0.05)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.75)
    driver.swipe(x1, y1, x2, y1, t)


# 判断元素是否存在
def is_element_exist(driver, content):
    source = driver.page_source
    # print(source)
    if content in source:
        return True
    else:
        return False


desired_caps = {
    # 基本
    'platformName': 'IOS',
    'automationName': 'xcuitest',

    # 应用APP
    'app': 'com.apple.Health',  # 已存在的应用 直接用 bundleId
    # 'app': '/Users/micllo/Downloads/appium/ios/TestApp.app'  #  .app包路径
           
    # 模拟器 8
    # 'platformVersion': '13.4',
    # 'deviceName': 'iPhone 8',
    # 'udid': '647616B3-44E3-4198-8578-E22FFD8EE43D'

    # 模拟器 11
    'platformVersion': '13.4',
    'deviceName': 'iPhone 11',
    'udid': '5F302EEC-C5AA-489D-924D-45FB91C9C894'

    # 真机
    # 'platformVersion': '10.3',
    # 'deviceName': 'iPhone 7',
    # 'udid': '3cbb25d055753f2305ec70ba6dede3dca5d500bb'

}

driver = webdriver.Remote('192.168.31.10:4723/wd/hub', desired_caps)
driver.implicitly_wait(3)

# 1.从屏幕底部往上划
swipeUp(driver, 1000)
time.sleep(2)

# 2.点击 Browse 图标
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Browse"]').click()
time.sleep(2)

# 3.输入框搜索 Heart
# search_input = driver.find_element_by_xpath('//XCUIElementTypeSearchField[@name="Search"]')
search_input = driver.find_element_by_name("Search")
search_input.click()
time.sleep(1)
search_input.send_keys("Heart")
time.sleep(2)

# 4.等待"Nutrition"内容消失
res1 = is_element_exist(driver, "Nutrition")
print("内容 Nutrition 是否存在: " + str(res1))
time.sleep(2)

# 5.判断是否存在"Data"内容
res2 = is_element_exist(driver, "Data")
print("内容 Data 是否存在: " + str(res2))
time.sleep(2)

# 6.点击"Heart Rate"进入
driver.find_element_by_xpath('(//XCUIElementTypeOther[@name="feeditem_identifier"])[1]/XCUIElementTypeButton').click()
time.sleep(2)

# 7.点击"Add Data"
# driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Add Data"]').click()
driver.find_element_by_name("Add Data").click()
time.sleep(2)

# 8.在'BPM'中输入 66
# bpm_input = driver.find_element_by_xpath('//XCUIElementTypeTextField[@name="BPM"]')
bpm_input = driver.find_element_by_name("BPM")
bpm_input.click()
bpm_input.send_keys("66")
time.sleep(2)

# 9.点击'Add'
# driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Add"]').click()
driver.find_element_by_name("Add").click()
time.sleep(2)

# 10.关闭应用
driver.quit()



# # 获取计算结果
# answer_el = driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name=\"Answer\"]")
# print(answer_el.text)
# # 隐藏键盘
# driver.hide_keyboard()
# # 截屏
# driver.get_screenshot_as_file("test1.png")
#
#
# # 点击 弹框按钮 并确认
# popup_btn = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"Check calendar authorized\"]")
# popup_btn.click()
# time.sleep(2)
# driver.get_screenshot_as_file("test2.png")
#
# ok_btn = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"OK\"]")
# ok_btn.click()
# time.sleep(1)
#
# # 获取拖动条元素
# seekbar_el = driver.find_element_by_xpath("//XCUIElementTypeSlider[@name=\"AppElem\"]")
# print(seekbar_el.text)
#
#
# # # 获取拖动条 高度与宽度
# # width = seekbar_el.size.get("width")
# # height = seekbar_el.size.get("height")
# # print("width : " + str(width))
# # print("height : " + str(height))
# #
# # # 获取拖动条 坐标
# # x = seekbar_el.location.get("x")
# # y = seekbar_el.location.get("y")
# # x2 = int(width * 0.75)
# # print("x : " + str(x))
# # print("y : " + str(y))
# # print("x2 : " + str(x2))
#
# # 滑动条：右滑
# # driver.swipe(x, y, x2, y, 1000)
# # TouchAction(driver).press(x=149, y=303).move_to(x=189, y=305).release().perform()
#
# # time.sleep(2)
# # print(seekbar_el.text)


