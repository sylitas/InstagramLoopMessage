from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def login_to_instagram():
    Username=browser.find_element_by_name("username")
    Username.send_keys(username)
    Password=browser.find_element_by_name("password")
    Password.send_keys(password)
    browser.find_element_by_xpath("//button[@type='submit']").click()

def skip_buttons():
    browser.find_element_by_xpath("//div[@class='cmbtv']/button[@type='button']").click()
    browser.find_element_by_xpath("//div[@class='mt3GC']/button[@class='aOOlW   HoLwm ']").click()

def navigate_to_sender():
    browser.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg.KtFt3 > div > div:nth-child(2) > a > svg').click()
    elements = browser.find_elements_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div')
    length = len(elements)   
    for i in range(length):
        find_user = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[{}]/a/div/div[2]/div[1]/div/div/div/div'.format(str(i+1)))
        if find_user.text == userToSpam:
            find_user.click()

def send_jokes(time_between_jokes):
    message_entry=browser.find_element_by_css_selector('#react-root > section > div > div.qF0y9.Igw0E.IwRSH.eGOV_.acqo5._4EzTm > div > div > div.DPiy6.qF0y9.Igw0E.IwRSH.eGOV_.acqo5.vwCYk > div.uueGX > div > div.qF0y9.Igw0E.IwRSH.eGOV_.acqo5._4EzTm > div > div > div.qF0y9.Igw0E.IwRSH.eGOV_.acqo5.vwCYk.ItkAi > textarea')
    while True:
        message_entry.send_keys(message_to_send)
        browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
        time.sleep(time_between_jokes)

#-------------------------------
username = input("Tên đăng nhập: ")
password = input("Mật Khẩu: ")
userToSpam = input("Tên người nhắn để spam: ")
message_to_send= input("Nội dung tin nhắn spam: ")
time_between_jokes = int(input("Thời gian spam: "))
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get('https://instagram.com/')
browser.implicitly_wait(5)
login_to_instagram()
skip_buttons()
navigate_to_sender()
send_jokes(time_between_jokes)