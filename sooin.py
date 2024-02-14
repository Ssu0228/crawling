#기본 설정
'''
from selenium.webdriver.chrome.service import Service 
from selenium import webdriver

serv = Service("C:/chromedriver/chromedriver.exe")
'''

#커맨드 창 없이 창 열기_기본 설정
'''
from selenium import webdriver 

from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW

serv=Service("C:/chromedriver/chromedriver.exe")
serv.creation_flags=CREATE_NO_WINDOW

driver=webdriver.Chrome(service=serv)'''


#창 열기
'''
driver.get("http://www.naver.com") 
'''

#창 최대화 시키기
'''
driver.maximize_window()
'''

#창 최소화 시키기
'''
driver.minimize_window()
'''

#버튼 클릭하기
'''
driver.get("http://gg.gg/webcrawlingtest")
p='//*[@id="homePageLinks"]/ul/li/a'
e=driver.find_element('xpath',p)
e.click()'''

#입력하기
'''
e.send_keys('')
'''

#엔터치기
'''
from selenium.webdriver.common.keys import Keys
e.send_keys(Keys.RETURN)'''

#기다리기
'''
import time
time.sleep()
'''

#유튜브 검색하기
'''
from selenium import webdriver 

from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
import time

serv=Service("C:/chromedriver/chromedriver.exe")
serv.creation_flags=CREATE_NO_WINDOW

driver=webdriver.Chrome(service=serv)

driver.get('https://www.youtube.com/results?search_query=%EB%B7%94+inner+child')

time.sleep(2)

p='//input[@id="search"]'
e=driver.find_element('xpath',p)
#e.send_keys('winterbear 뷔')

from selenium.webdriver.common.keys import Keys
e.send_keys(Keys.RETURN)

time.sleep(2)
p1='//a[@id="thumbnail"]'
elements=driver.find_elements('xpath',p1)

time.sleep(2)
driver2=webdriver.Chrome(service=serv)
driver2.get(elements[2].get_attribute('href'))'''


#네이버 주식 웹크롤링

from selenium import webdriver 

from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW

serv=Service("C:/chromedriver/chromedriver.exe")
serv.creation_flags=CREATE_NO_WINDOW

driver=webdriver.Chrome(service=serv)
driver.get("http://www.naver.com")
time.sleep(2)

p='//*[@id="shortcutArea"]/ul/li[6]/a/span[2]'
e=driver.find_element('xpath',p)
e.click()
time.sleep(2)

p='//*[@id="stock_items"]'
e=driver.find_element('xpath',p)
e.send_keys('하이브')
from selenium.webdriver.common.keys import Keys
e.send_keys(Keys.RETURN)


#학교종이
'''
from selenium import webdriver 

from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
import time

serv=Service("C:/chromedriver/chromedriver.exe")
serv.creation_flags=CREATE_NO_WINDOW

driver=webdriver.Chrome(service=serv)

driver.get('https://v4.schoolbell-e.com/ko/gate/home?return_uri=https:%2F%2Fschoolbell-e.com%2Fko%2Fmain%2Fhome')
time.sleep(2)

p='/html/body/schoolbelle-root/div/app-gate/app-gate-home/div[1]/div[3]/div[1]/div/button[1]'
e=driver.find_element('xpath',p)
e.click()
time.sleep(2)

p='/html/body/schoolbelle-root/div/app-gate/app-gate-login/div/div[1]/div/form/div[1]/div/phone-number-input/div/input'
e=driver.find_element('xpath',p)
e.click()
e.send_keys('010-2561-6436')
time.sleep(2)

p='/html/body/schoolbelle-root/div/app-gate/app-gate-login/div/div[1]/div/form/div[2]/div[1]/input'
e=driver.find_element('xpath',p)
e.click()
e.send_keys('rhdfyo8193')
time.sleep(2)

p='/html/body/schoolbelle-root/div/app-gate/app-gate-login/div/div[1]/div/form/div[3]/button'
e=driver.find_element('xpath',p)
e.click()
time.sleep(3)

p='/html/body/app-root/app-main/div[1]/app-main-home/div[2]/div[1]/div[1]/app-my-group-slides/div/ngu-carousel/div/div[1]/div/ngu-tile[2]/div/div[1]/div/div[1]'
e=driver.find_element('xpath',p)
e.click()
time.sleep(3)'''
#e 와 p 를 한 변수로 계속 써도 괜찮아~ (e2, e3 이렇게 바꾸지 않고..)

#학교종이_안내문 출력하기(f, formatting 이용)
'''
for i in range(10):
    p=f'/html/body/app-root/app-main/div[1]/app-main-group/div[2]/div[1]/div[2]/div/app-group-board/div/div/virtual-scroller/div[2]/div[3]/div[{i+1}]/div/app-letter-item-short/div/div/div/div[2]/h6/app-translation-viewer/span'
    e=driver.find_element('xpath',p)
    print(e.text)'''

#텍스트 파일로 저장하기
'''
text='안녕하세요.'
file=open('test.txt','w')
file.write(text)
file.close()'''

#학교종이_안내문 출력+텍스트 파일로 저장
'''
file=open('학교종이.txt','w')

for i in range(10):
    p=f'/html/body/app-root/app-main/div[1]/app-main-group/div[2]/div[1]/div[2]/div/app-group-board/div/div/virtual-scroller/div[2]/div[3]/div[{i+1}]/div/app-letter-item-short/div/div/div/div[2]/h6/app-translation-viewer/span'
    e=driver.find_element('xpath',p)
    file.write(e.text+'\n')

file.close()'''

#네이버 뉴스 검색창 캡쳐하기
'''
from selenium import webdriver 

from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW

import time

serv=Service("C:/chromedriver/chromedriver.exe")
serv.creation_flags=CREATE_NO_WINDOW

driver=webdriver.Chrome(service=serv)
time. sleep(2)

driver.maximize_window()

driver.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query='+'방탄 군대')
time. sleep(2)

driver.save_screenshot('bts army.png')
'''

#캡쳐 미션
'''
from selenium import webdriver 

from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW

import time

serv=Service("C:/chromedriver/chromedriver.exe")
serv.creation_flags=CREATE_NO_WINDOW

driver=webdriver.Chrome(service=serv)
time. sleep(2)

s=['뷔', '정국', '진']

driver.maximize_window()
for i in range(len(s)):
    driver.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query='+s[i])
    time.sleep(2)
    driver.save_screenshot(s[i]+'.png')
    time.sleep(2)
'''

