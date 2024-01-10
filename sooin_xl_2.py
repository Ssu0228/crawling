#기본 설정
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service("C:/chromedriver/chromedriver.exe")
serv.creation_flags = CREATE_NO_WINDOW   
driver = webdriver.Chrome(service = serv)

#모듈 불러오기
import time, datetime, os # timesleep, 파일 이름을 위한 현재 시간, 파일 열기 모듈
import openpyxl # 파이썬이 엑셀 열게 해주는 모듈  

#파일 이름 저장
now=str(datetime.datetime.now()) [:16] #시간 불러오기-초 단위까지 자르기
folderName=now.replace(':','_') #:을 _로 바꿈
os.mkdir(folderName) #mkdir= make directory('폴더 이름')

#검색, 저장        
key_word=['비트코인','이더리움','세종시 맛집','살 빼는 운동'] #검색어

wb=openpyxl.Workbook() #워크북 열기

for i in range(len(key_word)): #key_word 리스트 길이만큼 반복
    ws=wb.create_sheet() #worksheet 생성
    ws.title=key_word[i] #worksheet 이름을 검색어로 변경

    url = "https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=" + key_word[i]
    driver.get(url)
    time.sleep(2)
    
