import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


#################

# 크롬 드라이버 설정
CHROMEDRIVER_PATH = os.path.join("C:\\TEMP", "Chrome_Driver", "chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# 서비스 설정
service = Service(executable_path=CHROMEDRIVER_PATH)

# 드라이버 실행
driver = webdriver.Chrome(service=service, options=options)

# url input
url = 'http://dsp.daesang.com/'
driver.get(url)
driver.maximize_window()
time.sleep(2)
driver.implicitly_wait(20)

# 계정 정보 입력
ID_input = driver.find_element(By.ID, "input-userId")
PWD_input = driver.find_element(By.ID, "input-password")

ID_input.send_keys("209007")
PWD_input.send_keys("@rpa456456")

#로그인 버튼 클릭
login_button = driver.find_element(By.CLASS_NAME, "loginSubmitBtn")
login_button.click()


# 로그인 후 페이지 로드 대기
time.sleep(3)


#식단게시판 이동

driver.switch_to.frame("body")
gnb_list = driver.find_elements(By.CLASS_NAME, "gnb")

for gnb in gnb_list:
    try:
        # 각 gnb 요소 내부에서 '정보채널' 텍스트 포함한 하위 요소 찾기
        info_channel = gnb.find_element(By.XPATH, ".//*[contains(text(), '정보채널')]")
        info_channel.click()
        break  # 클릭 성공 시 반복 종료
    except:
        continue  # 해당 요소에 '정보채널'이 없으면 다음으로

# 클릭해서 가는 방법을 모르겠어서 그냥 url 이동
url = "http://dsp.daesang.com/DS_10/emate_app/bbs/b1407002.nsf/view01?openview"
driver.get(url)   

# 첫 번째 게시글(tr 태그)
first_row = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "table#tbldoclist tr.trout"))
)

# 두 번째 td (게시글 제목 부분)를 클릭
title_cell = first_row.find_elements(By.TAG_NAME, "td")[1]
title_cell.click()

# 새 창 탐색 후 전환
original_window = driver.current_window_handle
WebDriverWait(driver, 10).until(EC.new_window_is_opened)
for window in driver.window_handles:
    if window != original_window:
        driver.switch_to.window(window)
        break

# 새 창에서 다운로드 버튼 클릭
download_button = driver.find_element(By.CLASS_NAME, "attm-btn._loopdown")
download_button.click()

time.sleep(5)