from unittest import  TestCase
from selenium import webdriver

#driver=webdriver.Chrome()

# driver.get("http://127.0.0.1:8000/flights/counter")
# print(driver.title)
# print(driver.page_source)
# increase=driver.find_element_by_id("increase")
#
# increase.click()
# increase.click()
# increase.click()
# increase.click()
# increase.click()
#
# for i in range(25):
#     increase.click()
#
#
# decrease=driver.find_element_by_id("decrease")
#
# decrease.click()
# decrease.click()
# decrease.click()
# decrease.click()
# decrease.click()
#
# for i in range(25):
#     decrease.click()


def is_button():
    return True;



class testcounterweb(TestCase):


    def test_increase_button(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:8000/flights/counter")
        increase=driver.find_element_by_id("increase")
        increase.click()
        self.assertEqual(driver.find_element_by_id("result").text,"1")