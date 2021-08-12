# Generated by Selenium IDE

import time
import sys
import win32api, win32con
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from datetime import datetime
from debug_browser import DebugBrowser
import testraw


class CleanAllCase:

    def __init__(self):
        # Step # | name | target | value
        chrome_driver = r'.\drivers\chromedriver.exe'
        # chrome_options = Options()
        # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9000")
        # self.driver = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)
        self.driver = webdriver.Chrome(executable_path=chrome_driver, options=DebugBrowser().debug_chrome())
        # 1 | open | Chrome with debugger address |\
        # if not self.driver.toString().contains("null"):
        #     self.driver.quit()
        cur_handle = self.driver.current_window_handle  # get current handle
        all_handle = self.driver.window_handles  # get all handles
        target_url = "https://907826.app.netsuite.com/app/center/card.nl?sc=-29&whence="
        for h in all_handle:
            if h != cur_handle:
                self.driver.switch_to.window(h)  # Switch to the new pop-up window
                break
        # 2 | open | /app/center/card.nl?sc=-29&whence= |\
        time.sleep(2)
        self.driver.set_window_size(960, 1080)
        self.driver.set_window_position(0, 0)
        self.driver.get(target_url)
        if not ("https://907826.app.netsuite.com/app/center/" in self.driver.current_url):
            win32api.MessageBox(0, "Please login first and try again. :)", "Please Login",
                                win32con.MB_OK)
            sys.exit(0)

    def teardown_method(self):
        # Step # | name | target | value
        self.driver.close()
        # 1 | close | Chrome with debugger address |\

    def refresh_list(self):
        # Step # | name | target | value
        js_top = "var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js_top)
        # 1 | scroll | Scroll to the top of window |\
        element = self.driver.find_element(By.XPATH, "//div[2]/div/div/h2")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 2 | MouseMoveAt | Title: Paul's All Case View | hover element
        refresh_icon = "//div[2]/div/div/div/span[3]"
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, refresh_icon))
            )
        finally:
            element = self.driver.find_element(By.XPATH, refresh_icon)
            actions = ActionChains(self.driver)
            actions.move_to_element(element)
            actions.click(element).perform()
        # 3 | move mouse and click | Refresh Icon | hover element

    def refresh_list_down(self):
        # Step # | name | target | value
        # 1 | scroll | Scroll to the top of window |\
        title_list = "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[2]/div[1]/h2"
        refresh_icon = "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[2]/div[1]/div/span[3]"
        element = self.driver.find_element(By.XPATH, refresh_icon)
        ele = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[2]/div["
                                                 "1]/div")
        self.driver.execute_script("arguments[0].style.display='block';", ele)
        self.driver.execute_script("arguments[0].style.display='block';", element)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, title_list))
            )
        finally:
            element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div["
                                                         "1]/div[2]")
            self.driver.execute_script("arguments[0].scrollIntoView(true)", element)
            element = self.driver.find_element(By.XPATH, title_list)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
        # 2 | MouseMoveAt | Title: Paul's All Case View | hover element

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, refresh_icon))
            )
        finally:
            element = self.driver.find_element(By.XPATH, refresh_icon)
            # ele = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[2]/div["
            #                                          "1]/div")
            # self.driver.execute_script("arguments[0].style.display='block';", ele)
            # self.driver.execute_script("arguments[0].style.display='block';", element)
            # time.sleep(3)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            element.click()
        # 3 | move mouse and click | Refresh Icon | hover element
        element = self.driver.find_element(By.XPATH, title_list)
        self.driver.execute_script("arguments[0].scrollIntoView(true)", element)

    def clean_all_case(self):
        # Step # | name | target | value
        tab_case = "/html/body/div[1]/div[1]/div[2]/ul[4]/li[2]/a/span"
        filename = datetime.now().strftime("%b_%d_%Y") + "_clean_list_log.txt"
        file1 = open(filename, "a+")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, tab_case))
            )
        finally:
            self.driver.find_element(By.XPATH, tab_case).click()
        # 1 | click | case tab |
        number_sum = "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[1]/div[2]/div/div/form/div[2]/table[" \
                     "2]/tbody/tr/td/table/tbody/tr/td/a"
        # first_table = "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[1]/div[2]/div/div/div/div/table"
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, number_sum))
            )
        finally:
            time.sleep(1)
            ele = self.driver.find_element(By.XPATH, number_sum)
        html = ele.get_attribute('innerHTML')
        case_sum = int(html)
        log = 0
        # 2 | read | case number |
        while case_sum > 0:
            if case_sum <= 0:
                # win32api.MessageBox(0, "No more case in queue. :)", "Cleaning Done", win32con.MB_OK)
                # sys.exit(0)
                break
            else:
                # table_content = "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[1]/div[
                # 2]/div/div/div/div/table"
                table_content = "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[1]/div[" \
                                "2]/div/div/div/div"
                first_row_inner_xpath = "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[1]/div[" \
                                        "2]/div/div/div/div/table/tbody/tr[1]/td "
                ele = self.driver.find_element(By.XPATH, first_row_inner_xpath)
                text = ele.get_attribute('innerHTML')
                if text == "No Search Results Match Your Criteria.":
                    break
                    # win32api.MessageBox(0, "No more case in queue. :)", "Cleaning Done", win32con.MB_OK)
                    # sys.exit(0)
                ele = self.driver.find_element(By.XPATH, table_content)
                html = ele.get_attribute('innerHTML')
                soup = BeautifulSoup(html, 'html5lib')
                tables = soup.findAll('table')
                tab = tables[0]
                table_body = tab.tbody
                tr_group = table_body.find_all('tr')
                target = int(len(tr_group) - 1)  # number of tr
                log += target
                print(target)
                for tr in tr_group:
                    if not ("text" in tr['class']):
                        td_group = tr.find_all('td')
                        txt = td_group[5].text
                        case_num = td_group[8].text
                        file1.write(case_num.rstrip() + '\t' + txt + '\n')
                        print(case_num)

                # 2 | count | case number in one page |
            first_row_xpath = "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[1]/div[" \
                              "2]/div/div/div/div/table/tbody/tr[1]/td[8]/span "
            last_row_xpath = "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[1]/div[" \
                             "2]/div/div/div/div/table/tbody/tr[" + str(target) + "]/td[8]/span"
            # print(last_row_xpath)
            input_box = "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[1]/div[" \
                        "2]/div/div/div/div/table/tbody/tr[1]/td[8]/span/div/span/div[1]/input "
            select_close = "/html/body/div[7]/div/div/div[15]"
            # 3 | click | first row |
            self.driver.find_element(By.XPATH, first_row_xpath).click()
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, input_box))
                )
            finally:
                self.driver.find_element(By.XPATH, input_box).send_keys("Closed")
                time.sleep(1)
                self.driver.find_element(By.XPATH, input_box).click()
            # 4 | shift + last line

            ele = self.driver.find_element(By.XPATH, last_row_xpath)
            action_chains = ActionChains(self.driver)
            action_chains.key_down(Keys.SHIFT).click(ele).key_up(Keys.SHIFT).perform()
            # 5 | click | id=uir_totalcount |
            js_top = "var q=document.documentElement.scrollTop=0"
            self.driver.execute_script(js_top)
            self.driver.find_element(By.ID, "uir_totalcount").click()
            # 6 |  refresh the list
            self.refresh_list()
            time.sleep(2)
            self.refresh_list()
            time.sleep(2)
            self.refresh_list()
            self.driver.find_element(By.XPATH, tab_case).click()
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, number_sum))
                )
            finally:
                ele = self.driver.find_element(By.XPATH, number_sum)
            html = ele.get_attribute('innerHTML')
            case_sum = int(html)
        file1.close()
        return log
        # 7 |  update the case number

    def change_criteria(self, search_type, key_word):
        js_top = "var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js_top)
        tab_case = "/html/body/div[1]/div[1]/div[2]/ul[4]/li[2]/a/span"
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, tab_case))
            )
        finally:
            self.driver.find_element(By.XPATH, tab_case).click()
        title = "//div[2]/div/div/h2"
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, title))
            )
        finally:
            element = self.driver.find_element(By.XPATH, title)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            # 1 | mouseMoveAt | Title: Paul's All case view | hover element
            # element.click()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div["
                                                          "1]/div[1]/div/div"))
            )
        finally:
            element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div["
                                                         "1]/div[1]/div/div")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            element.click()
            # 2 | mouseMoveAt | Configure Icon | hover element
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div["
                               "1]/div[1]/div/div/ul/li[3]/a"))
            )
        finally:

            element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div["
                                                         "1]/div[1]/div/div/ul/li[3]/a")
            while element.get_attribute("innerHTML") is None:
                element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div["
                                                             "1]/div[1]/div/div/ul/li[3]/a")
            while not ("Edit" in element.get_attribute("innerHTML")):
                element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div["
                                                             "1]/div[1]/div/div/ul/li[3]/a")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            element.click()
            # 3 | mouseMoveAt and click | Edit Icon | hover element
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/div[2]/div[3]/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/a"))
            )
        finally:
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/table[1]/tbody/tr["
                                               "1]/td/table/tbody/tr/td[2]/a").click()
        criteria_subject = "/html/body/div[1]/div[2]/div[3]/table[1]/tbody/tr[3]/td/div[1]/div/div/table/tbody/tr[" \
                           "2]/td/div/div[8]/div/form/div[6]/table/tbody/tr[4]/td[1]"
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, criteria_subject))
            )
        finally:
            self.driver.find_element(By.XPATH, criteria_subject).click()
        # actions = ActionChains(self.driver)
        # actions.move_to_element(criteria_subject).perform()
        arrow = "/html/body/div[1]/div[2]/div[3]/table[1]/tbody/tr[3]/td/div[1]/div/div/table/tbody/tr[2]/td/div/div[" \
                "8]/div/form/div[6]/table/tbody/tr[4]/td[1]/div/div/span/span[2]/a"
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, arrow))
            )
        finally:
            element = self.driver.find_element(By.XPATH, arrow)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            element.click()

        iframe = "/html/body/div[9]/div[2]/div[1]/div/div/iframe"
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, iframe))
            )
        finally:
            # 4 | mouseMoveAt and click | Arrow | hover element

            element = self.driver.find_element(By.XPATH, iframe)
            self.driver.switch_to.frame(element)

        textbox_1 = "/html/body/div[1]/div/div[4]/form/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/div[" \
                    "1]/span[2]/span "
        textbox_1_1 = "/html/body/div[1]/div/div[4]/form/table/tbody/tr[" \
                      "2]/td/table/tbody/tr/td/table/tbody/tr/td/div[1]/span[2]/span/div[1]/input "
        textbox_2 = "Case_TITLE"
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, textbox_1))
            )
        finally:
            self.driver.find_element(By.XPATH, textbox_1).click()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, textbox_1_1))
            )
        finally:
            self.driver.find_element(By.XPATH, textbox_1_1).send_keys(search_type)
            # 3 | Input | Search Type
        self.driver.find_element(By.NAME, textbox_2).click()
        self.driver.find_element(By.NAME, textbox_2).send_keys(Keys.CONTROL + "a");
        self.driver.find_element(By.NAME, textbox_2).send_keys(key_word)
        # 4 | Input | Search Key Words
        element = "/html/body/div[1]/div/div[4]/form/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr/td[" \
                  "1]/table/tbody/tr/td[2]/input"
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, element))
            )
        finally:
            self.driver.find_element(By.XPATH, element).click()
            # 5 | Click | Edit
        element = "/html/body/div[1]/div[2]/div[3]/table[2]/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/input"
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, element))
            )
        finally:
            self.driver.find_element(By.XPATH, element).click()
        # 6 | Click | Save

    def take_task(self):
        # Step # | name | target | value
        tab_home = "/html/body/div[1]/div[1]/div[2]/ul[3]/li/a"
        # self.driver.find_element(By.XPATH, tab_home).click()
        target_url = "https://907826.app.netsuite.com/app/center/card.nl?sc=-29&whence=#"
        self.driver.get(target_url)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, tab_home))
            )
        finally:
            self.driver.find_element(By.XPATH, tab_home).click()
            self.refresh_list_down()
        # 1 | click | case tab |
        number_sum = "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[2]/div[2]/div/div/form/div[" \
                     "2]/table/tbody/tr/td/table/tbody/tr/td/a"
        # first_table = "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[1]/div[2]/div/div/div/div/table"
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, number_sum))
            )
        finally:
            ele = self.driver.find_element(By.XPATH, number_sum)
            # self.driver.execute_script("arguments[0].scrollIntoView(true)", ele)
        html = ele.get_attribute('innerHTML')
        case_sum = int(html)
        # 2 | read | case number |
        while case_sum > 0:
            if case_sum <= 0:
                # win32api.MessageBox(0, "No more case in queue. :)", "Cleaning Done", win32con.MB_OK)
                # sys.exit(0)
                break
            else:
                # table_content = "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[1]/div[
                # 2]/div/div/div/div/table"
                table_content = "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[2]/div[2]/div/div/div"
                first_row_inner_xpath = "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[2]/div[" \
                                        "2]/div/div/div/div/table/tbody/tr[1]/td"
                ele = self.driver.find_element(By.XPATH, first_row_inner_xpath)
                # self.driver.execute_script("arguments[0].scrollIntoView(true)", ele)
                text = ele.get_attribute('innerHTML')
                if text == "No Search Results Match Your Criteria.":
                    break
                    # win32api.MessageBox(0, "No more case in queue. :)", "Cleaning Done", win32con.MB_OK)
                    # sys.exit(0)
                first_pencil = "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[2]/div[" \
                               "2]/div/div/div/div/table/tbody/tr[1]/td[2]/a[1]"
                input_name = "/html/body/div[1]/div[2]/div[3]/form/table/tbody/tr[2]/td/table/tbody/tr[" \
                             "1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/div/span[2]/span/div[1]/input"
                my_name = "/html/body/div[8]/div/div/table/tbody/tr/td"
                save_icon = "/html/body/div[1]/div[2]/div[3]/form/table/tbody/tr[" \
                            "1]/td/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/input "
                element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div["
                                                             "2]/div[1]/h2")
                self.driver.execute_script("arguments[0].scrollIntoView(true)", element)
                # print(last_row_xpath)
                # 3 | click | first row |
                try:
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, first_pencil))
                    )
                finally:
                    time.sleep(3)
                    element = self.driver.find_element(By.XPATH, first_pencil)
                    element.click()
                try:
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, input_name))
                    )
                finally:
                    self.driver.find_element(By.XPATH, input_name).send_keys(Keys.CONTROL + "a")
                    self.driver.find_element(By.XPATH, input_name).send_keys("Paul Wu")
                    time.sleep(3)
                    self.driver.find_element(By.XPATH, input_name).send_keys(Keys.ENTER)
                # try:
                #     WebDriverWait(self.driver, 10).until(
                #         EC.presence_of_element_located((By.XPATH, my_name))
                #     )
                # finally:
                #     time.sleep(2)
                #     self.driver.find_element(By.XPATH, my_name).click()
                # 4 | shift + last line
                self.driver.find_element(By.XPATH, save_icon).click()
                time.sleep(1)
                self.refresh_list_down()
                self.driver.find_element(By.XPATH, tab_home).click()
                try:
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, number_sum))
                    )
                finally:
                    ele = self.driver.find_element(By.XPATH, number_sum)
                    self.driver.execute_script("arguments[0].scrollIntoView(true)", ele)
                html = ele.get_attribute('innerHTML')
                case_sum = int(html)

            # 7 |  update the case number

    def resend_all_case(self):
        # Step # | name | target | value
        filename = datetime.now().strftime("%b_%d_%Y") + "_resend_log.txt"
        file1 = open(filename, "a+")
        tab_case = "/html/body/div[1]/div[1]/div[2]/ul[4]/li[2]/a/span"
        self.driver.find_element(By.XPATH, tab_case).click()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, tab_case))
            )
        finally:
            self.driver.find_element(By.XPATH, tab_case).click()
        # 1 | click | case tab |
        number_sum = "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[1]/div[2]/div/div/form/div[2]/table[" \
                     "2]/tbody/tr/td/table/tbody/tr/td/a "
        # first_table = "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[1]/div[2]/div/div/div/div/table"
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, number_sum))
            )
        finally:
            time.sleep(1)
            ele = self.driver.find_element(By.XPATH, number_sum)
        html = ele.get_attribute('innerHTML')
        case_sum = int(html)
        # 2 | read | case number |
        while case_sum > 0:
            if case_sum <= 0:
                # win32api.MessageBox(0, "No more case in queue. :)", "Cleaning Done", win32con.MB_OK)
                # sys.exit(0)
                break
            else:
                # table_content = "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[1]/div[
                # 2]/div/div/div/div/table"
                table_content = "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[1]/div[" \
                                "2]/div/div/div/div"
                first_row_inner_xpath = "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[1]/div[" \
                                        "2]/div/div/div/div/table/tbody/tr[1]/td "
                ele = self.driver.find_element(By.XPATH, first_row_inner_xpath)
                text = ele.get_attribute('innerHTML')
                if text == "No Search Results Match Your Criteria.":
                    break
                    # win32api.MessageBox(0, "No more case in queue. :)", "Cleaning Done", win32con.MB_OK)
                    # sys.exit(0)
                ele = self.driver.find_element(By.XPATH, table_content)
                html = ele.get_attribute('innerHTML')
                soup = BeautifulSoup(html, 'html5lib')
                tables = soup.findAll('table')
                tab = tables[0]
                table_body = tab.tbody
                number_tr = int(len(table_body.find_all('tr'))) - 1
                print(number_tr)
                # 2 | count | case number in one page |
                first_row_xpath = "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[1]/div[" \
                                  "2]/div/div/div/div/table/tbody/tr[1]/td[8]/span "
                last_row_xpath = "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[1]/div[" \
                                 "2]/div/div/div/div/table/tbody/tr[" + str(number_tr) + "]/td[8]/span"
                # print(last_row_xpath)
                input_box = "/html/body/div[1]/div[2]/div/div/div/div[5]/div[2]/div[1]/div[" \
                            "2]/div/div/div/div/table/tbody/tr[1]/td[8]/span/div/span/div[1]/input "
                select_close = "/html/body/div[7]/div/div/div[15]"
                tr_group = table_body.find_all('tr')
                log_group = []
                try:
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, first_row_xpath))
                    )
                finally:
                    self.driver.find_element(By.XPATH, first_row_xpath).click()
                try:
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, input_box))
                    )
                finally:
                    self.driver.find_element(By.XPATH, input_box).send_keys("Closed")
                    time.sleep(1)
                    self.driver.find_element(By.XPATH, input_box).click()
                # 4 | shift + last line

                ele = self.driver.find_element(By.XPATH, last_row_xpath)
                action_chains = ActionChains(self.driver)
                action_chains.key_down(Keys.SHIFT).click(ele).key_up(Keys.SHIFT).perform()
                # 5 | click | id=uir_totalcount |
                js_top = "var q=document.documentElement.scrollTop=0"
                self.driver.execute_script(js_top)
                self.driver.find_element(By.ID, "uir_totalcount").click()
                # 6 |  refresh the list
                for tr in tr_group:
                    if not ("text" in tr['class']):
                        td_group = tr.find_all('td')
                        txt = td_group[5].text
                        case_num = td_group[8].text
                        file1.write(case_num.rstrip() + '\t' + txt + '\n')
                        log_id = txt.split("LogId ", 1)[1]
                        print(log_id)
                        print(case_num)
                        log_group.append(log_id)
                resend_worker = testraw.TestPsd()
                resend_worker.psd_resend(log_group)
                resend_worker.teardown_method()

                self.refresh_list()
                self.driver.find_element(By.XPATH, tab_case).click()
                self.refresh_list()
                try:
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, number_sum))
                    )
                finally:
                    ele = self.driver.find_element(By.XPATH, number_sum)
                html = ele.get_attribute('innerHTML')
                case_sum = int(html)
                time.sleep(2)
        file1.close()

    def cloud_ftp(self, profile_name):
        target_url = "http://psdtool.tc.net/psdTool/"
        self.driver.get(target_url)
        search_input = "/html/body/form/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td[2]/input"
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, search_input))
            )
        finally:
            ele = self.driver.find_element(By.XPATH, search_input)
            ele.send_keys(profile_name)
            self.driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[2]"
                                               "/td[2]/div/table/tbody/tr/td[3]/input").click()
        notes_input = "/html/body/form/table/tbody/tr[3]/td/div/table/tbody/tr[3]/td/table/tbody/tr[2]/td/div[1]/div[" \
                      "2]/div/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/textarea "
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, notes_input))
            )
        finally:
            time.sleep(1)
            qualifier = self.driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[3]/td/div/table/tbody/tr["
                                                           "3]/td/table/tbody/tr[2]/td/div[1]/div[4]/table/tbody/tr["
                                                           "2]/td[1]").get_attribute("innerHTML")
            ediid = self.driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[3]/td/div/table/tbody/tr["
                                                       "3]/td/table/tbody/tr[2]/td/div[1]/div[4]/table/tbody/tr[2]/td["
                                                       "2]").get_attribute("innerHTML")
            ele = self.driver.find_element(By.XPATH, notes_input)
            username = qualifier + ediid
            print(username)
            ele.send_keys("\n" + "Cloud SFTP:" + "\n" + "U: " + username + "\n")
            var = profile_name.split()
            profile_id = self.driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[3]/td/div/table/tbody/tr["
                                                            "3]/td/table/tbody/tr[2]/td/div[1]/div[1]/table/tbody/tr["
                                                            "1]/td[2]").get_attribute("innerHTML")
            password = var[0] + profile_id + "!"
            print(password)
            ele.send_keys("P: " + password)
            self.driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[3]/td/div/table/tbody/tr["
                                               "3]/td/table/tbody/tr[2]/td/div[1]/div[2]/div/table/tbody/tr["
                                               "3]/td/input").click()

            profile_manage = "/html/body/form/table/tbody/tr[2]/td[1]/table/tbody/tr/td/table/tbody/tr/td[" \
                             "4]/table/tbody/tr/td[1]/a "
            ftp_setup = "/html/body/form/table/tbody/tr[2]/td[1]/table/tbody/tr/td/div[4]/table/tbody/tr[" \
                        "6]/td/table/tbody/tr/td "
            setup_inbox = "/html/body/form/table/tbody/tr[3]/td/div/table/tbody/tr[2]/td[1]/input[1]"
            element = self.driver.find_element(By.XPATH, profile_manage)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, ftp_setup))
                )
            finally:
                ele = self.driver.find_element(By.XPATH, ftp_setup)
                actions = ActionChains(self.driver)
                actions.move_to_element(ele)
                actions.click(ele).perform()
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, setup_inbox))
                )
            finally:
                ele = self.driver.find_element(By.XPATH, setup_inbox)
                ele.send_keys(profile_name)
                self.driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[3]/td/div/table/tbody/tr[2]/td["
                                                   "1]/input[2]").click()
                self.driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[3]/td/div/div["
                                                   "1]/div/table/tbody/tr[3]/td[2]/input").send_keys(username)
                self.driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[3]/td/div/div["
                                                   "1]/div/table/tbody/tr[4]/td[2]/input").send_keys(password)
                self.driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[3]/td/div/div["
                                                   "1]/div/table/tbody/tr[5]/td/input[2]").click()
                self.driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[3]/td/div/div["
                                                   "1]/div/table/tbody/tr[6]/td/input").click()

        # # 3 | click | first row |
        # self.driver.find_element(By.XPATH, first_row_xpath).click()
        # try:
        #     WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, input_box))
        #     )
        # finally:
        #     self.driver.find_element(By.XPATH, input_box).send_keys("Closed")
        #     time.sleep(1)
        #     self.driver.find_element(By.XPATH, input_box).click()
        # # 4 | shift + last line
        #
        # ele = self.driver.find_element(By.XPATH, last_row_xpath)
        # action_chains = ActionChains(self.driver)
        # action_chains.key_down(Keys.SHIFT).click(ele).key_up(Keys.SHIFT).perform()
        # # 5 | click | id=uir_totalcount |
        # js_top = "var q=document.documentElement.scrollTop=0"
        # self.driver.execute_script(js_top)
        # self.driver.find_element(By.ID, "uir_totalcount").click()
        # # 6 |  refresh the list
        # self.refresh_list()
        # self.refresh_list()
        # self.refresh_list()
        # self.driver.find_element(By.XPATH, tab_case).click()
        # try:
        #     WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, number_sum))
        #     )
        # finally:
        #     ele = self.driver.find_element(By.XPATH, number_sum)
        # html = ele.get_attribute('innerHTML')
        # case_sum = int(html)
        # # 7 |  update the case number
