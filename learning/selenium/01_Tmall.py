import csv
import time
import logging

from selenium.webdriver import Chrome


def get_data():
    items = win.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    for item in items:
        # 旗舰店
        store = item.find_element_by_xpath('.//div[@class="shop"]/a').text
        # 商品描述
        desc = item.find_element_by_xpath('./div[2]/div[2]/a').text
        # 价格
        price = item.find_element_by_xpath('./div[2]/div/div/strong').text
        # 人数
        num = item.find_element_by_xpath('.//div[@class="deal-cnt"]').text
        # 地址
        address = item.find_element_by_xpath('.//div[@class="location"]').text

        with open(f'{commodity}.csv', mode='a', newline='', encoding='utf-8-sig') as f:
            csv_write = csv.writer(f, delimiter=',')
            csv_write.writerow([store, desc, price, num, address])

def main():
    win.get('https://www.taobao.com/')
    win.find_element_by_xpath('//*[@id="q"]').send_keys(commodity)
    win.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
    win.maximize_window()
    time.sleep(15)
    get_data()


if __name__ == '__main__':
    commodity = "手机"
    win = Chrome()
    main()
