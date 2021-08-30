# 导入浏览器驱动
from selenium import webdriver
import datetime
import time


#
def login():
    browser.get('https://www.taobao.com')
    browser.maximize_window()
    time.sleep(1)

    # if browser.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]')
    if browser.find_element_by_link_text('亲，请登录'):
        browser.find_element_by_link_text('亲，请登录').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="login"]/div[1]/i').click()
        print('请在10秒内进行手机扫码')
        # 等待用户扫码
        time.sleep(10)
        browser.get('https://cart.taobao.com/cart.htm')
    time.sleep(2)
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(times):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if now >= times:
            while True:
                try:
                    if browser.find_element_by_xpath('//*[@id="J_SelectAll1"]'):
                        browser.find_element_by_xpath('//*[@id="J_SelectAll1"]').click()
                        break
                except:
                    print('找不到全选按钮')

            while True:
                try:
                    if browser.find_element_by_xpath('//*[@id="J_Go"]'):
                        browser.find_element_by_xpath('//*[@id="J_Go"]').click()
                        print('结算成功')
                        break
                except:
                    pass
            while True:
                try:
                    if browser.find_element_by_link_text('提交订单'):
                        browser.find_element_by_link_text('提交订单').click()
                        now_1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                        print('抢购成功，时间为', now_1)
                        break
                except:
                    print('再次尝试提交订单')
            time.sleep(0.01)


if __name__ == '__main__':
    times = input('请输入抢购时间，格式：2021-08-31 00:00:00.000000:')
    browser = webdriver.Firefox(executable_path='./geckodriver.exe')
    login()
    buy(times)
