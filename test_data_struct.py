import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from random import randint

from data import WEBSITE_LIST


USERS_USER_AGENT_DICT = {
        "firefox":r"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0",
        "edge":r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35",
        "chrome":r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"            
                        }

def create_chrome_driver(ublock:bool, headless:bool=True):
    ublock_path = os.getcwd()+"\\uBlock.crx"
    chrome_driver_path = os.getcwd()+"\\chrome\\chromedriver.exe"

    user_agent = USERS_USER_AGENT_DICT["chrome"]
    chrome_options = webdriver.ChromeOptions()
    if headless:chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"user-agent={user_agent}")
    if ublock:
        chrome_options.add_extension(ublock_path)

    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    return driver

def create_firefox_driver(ublock:bool, headless:bool=True):
    ublock_path = os.getcwd()+"\\uBlock.xpi"
    firefox_driver_path = os.getcwd() + "\\ff\\geckodriver.exe"
    user_agent = USERS_USER_AGENT_DICT["firefox"]
    firefox_options = webdriver.FirefoxOptions()
    if headless:firefox_options.add_argument("--headless")
    firefox_options.add_argument(f"user-agent={user_agent}")
    if ublock:
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.add_extension(ublock_path)

    driver = webdriver.Firefox(executable_path=firefox_driver_path, options=firefox_options, firefox_profile=firefox_profile)
    return driver

def create_edge_driver(ublock:bool, headless:bool=True):
    ublock_path = os.getcwd()+"\\uBlock.crx"
    edge_driver_path = os.getcwd() + "\\edge\\msedgedriver.exe"
    user_agent = USERS_USER_AGENT_DICT['edge']
    edge_options = webdriver.EdgeOptions()
    if headless:edge_options.add_argument("--headless")
    edge_options.add_argument(f"user-agent={user_agent}")
    if ublock:
        edge_options.add_extension(ublock_path)
    driver = webdriver.Edge(executable_path=edge_driver_path, options=edge_options)
    return driver

def test_struct(website_url:str):
    website_data = WEBSITE_LIST.get(website_url)
    print(website_data.keys())
    main_menu = website_data.get("main_menu")
    if main_menu: print("MAIN MENU:",main_menu)
    specifics = website_data.get("specifics")
    if specifics:print("EXTRA DATA:", specifics)
    print("\nAll starting endpoints")
    endpoints = website_data.get("endpoints")
    for x in endpoints.keys():
        print(str(endpoints[x]).split(";"))

    sub_endpoints = website_data.get("sub-endpoints")
    for x in sub_endpoints.keys():
        print("\n"+sub_endpoints[x])
        print("xpaths")
        for y in sub_endpoints[x].keys():
            print(str(sub_endpoints[x][y]).split(";"))

    pass

def test_xpath_list(website_url:str, xpath_list:list, driver):
    driver.get(website_url)
    time.sleep(3)
    count = 0
    for x_path in xpath_list:
        print(count)
        count+=1
        input()
        element = driver.find_element("xpath", x_path)
        element.click()
        time.sleep(2)

def s_find_element(driver, type_find, identificaiton):
    try:
        return driver.find_element(type_find, identificaiton)
    except:
        return None

def retry_3times_relies_prev_multiple(driver, last_type_find, last_css, next_type_find, next_css):
    element = None
    count = 0
    while element == None and count < 3:
        count+=1
        try:
            element = driver.find_elements(next_type_find, next_css)
            return element
        except: #attempt to refresh
            driver.refresh()
            last_el = driver.find_elements(last_type_find, last_css)
            last_el.click()
            time.sleep(2)

def retry_3times_relies_prev_single(driver, last_type_find, last_css, next_type_find, next_css):
    element = None
    count = 0
    while element == None and count < 3:
        count+=1
        try:
            element = driver.find_element(next_type_find, next_css)
            return element
        except: #attempt to refresh
            driver.refresh()
            last_el = driver.find_element(last_type_find, last_css)
            last_el.click()
            time.sleep(2)


def test_ss_list(website_url:str, ss_list:list, driver):
    driver.get(website_url)
    time.sleep(4)
    #input()
    count = 0
    refresh_mem =[]
    for csss in ss_list:
        type_find, css = str(csss).split(";")
        special = None
        try:
            special, type_find = type_find.split(":")
        except:
            pass
        print(count)
        count+=1
        #input()
        print(type_find)
        if special == "refresh_sens":
            refresh_mem.append((type_find, css))
        
        if special == "rand": #randomly index result
            try:
                elements = driver.find_elements(type_find, css)
            except:
                if special == "relies_prev":#check if in a state that requires to run last command
                    last_type_find, last_css = refresh_mem.pop()
                    elements = retry_3times_relies_prev_multiple(driver, last_type_find, last_css, type_find, css)

            rand_ind = randint(1,len(elements))-1
            element = elements[rand_ind]


        elif special: # specific indexed result
            if special[:2] == "ind":
                try:
                    elements = driver.find_elements(type_find, css)
                except:
                    if special == "relies_prev":#check if in a state that requires to run last command
                        last_type_find, last_css = refresh_mem.pop()
                        elements = retry_3times_relies_prev_multiple(driver, last_type_find, last_css, type_find, css)
                    #elements = driver.find_elements(type_find, css)
                ind = special.split("ind")
                print(ind)
                element = elements[ind]
        else:
            try:
                element = driver.find_elements(type_find, css)
            except: #attempt to refresh
                if special == "relies_prev": #check if in a state that requires to run last command
                    last_type_find, last_css = refresh_mem.pop()
                    element = retry_3times_relies_prev_single(driver, last_type_find, last_css, type_find, css)
                
        element.click()
        time.sleep(3)
    input("OUT")

if __name__ == "__main__":
    #c_driver = create_chrome_driver(True, False)
    c_driver = create_edge_driver(True, False)
    website_to_test = "https://www.youtube.com/"
    #csss_list = ["css selector;style-scope yt-icon-button[aria-label='Guide']", ""]
    seleniumsselector_list = ["refresh_sens:id;guide-icon", "relies_prev:partial link text;Trending", "rand:id;title-wrapper"]
    #sequential_xpaths_to_test = ['//*[@id="guide-icon"]', '/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[3]/div/ytd-guide-entry-renderer[1]', '/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[3]/div/ytd-guide-entry-renderer[1]/a']
    #test_xpath_list(website_to_test, sequential_xpaths_to_test, e_driver)
    test_ss_list(website_to_test, seleniumsselector_list, c_driver)
    #test_struct("https://www.youtube.com/")
    pass