from selenium import webdriver
import pyautogui
import time
browser = webdriver.Chrome("C:/chromedr/chromedriver") #change or set the path to this dir
print("Youtube Aud/Vid Downloader")
print("1. Youtube Audio")
print("2. Youtube Video")
print("3. Quit")
choose = input("Choose: ")
while(True):
    if choose == '1':
        browser.get("https://ytmp3.cc/en11/")
        yout_audio_url = input("Enter url: ")
        browser.find_element_by_id('input').send_keys(yout_audio_url)
        time.sleep(2)
        browser.find_element_by_id('submit').click()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="buttons"]/a[1]').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="buttons"]/a[3]').click()
        continue
    elif choose == '2':
        ini_str_video = input("Enter Url: ")
        res_string_video = ini_str_video[19:]
        new_str_video = "https://www.youtubepp" + res_string_video
        time.sleep(3)
        browser.get(new_str_video)
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="mp4"]/table/tbody/tr[1]/td[3]/a').click()
        time.sleep(20)
        browser.find_element_by_xpath('//*[@id="process-result"]/div/a').click()
        continue
    elif choose == '3':
        quit()
    else:
        quit()
        

    
        
