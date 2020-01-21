from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from get_towns import get_towns

class town_scrape():
    def __init__(self):
        self.client = webdriver.Chrome('C:\\Users\\rdonnelly\\Documents\\GitHub\\chromedriver.exe')
        self.client.get('https://www.google.com/maps')
        self.to = ['121 Chanlon Road New Providence NJ','117 Seber Road Hackettstown NJ']
        elem = self.client.find_element_by_class_name('tactile-searchbox-input')
        elem.clear()
        elem.send_keys('121 Chanlon Road New Providence NJ')
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.client.find_element_by_class_name('iRxY3GoUYUY__taparea').click()
        time.sleep(5)
    def get_time(self,town,file):
        elem = self.client.find_element_by_id('directions-searchbox-1')
        elem = elem.find_element_by_class_name('tactile-searchbox-input')
        elem.clear()
        elem.send_keys(town + ' NJ')
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        for i in self.to:
            elem = self.client.find_element_by_id('directions-searchbox-0')
            elem = elem.find_element_by_class_name('tactile-searchbox-input')
            elem.clear()
            elem.send_keys(i)
            elem.send_keys(Keys.RETURN)
            time.sleep(5)
            elem = self.client.find_element_by_class_name('section-layout')
            miles,t = '',''
            for j in elem.find_elements_by_tag_name('span'):
                if 'min' in j.text: t = j.text
            for j in elem.find_elements_by_tag_name('div'):
                if 'miles' in j.text: miles = j.text
            file.write(str(i)+','+str(town)+','+str(t) + ',' + str(miles))
            file.write('\n')
           
    def close(self):
        self.client.close()


a = town_scrape()
with open('results.txt', 'w') as file:
    file.write('work,location,time,miles\n')
    for i in get_towns():
        print(i)
        a.get_time(i,file)
        time.sleep(15)
a.close()