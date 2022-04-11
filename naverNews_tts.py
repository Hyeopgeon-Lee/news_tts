import pyttsx3
import requests
import re
from bs4 import BeautifulSoup

# 네이버의 해더의 User-Agent 값 체크로 인해 임의 값을 넣음
headers = {"User-Agent":"Seoul Gangseo Campus of Korea Polytechnics College, Dept. of Data Analysis / Python Education"}

# 수집할 신문기사 URL
webpage = requests.get("https://news.naver.com/main/read.naver?mode=LSD&mid=sec&sid1=101&oid=215&aid=0000983912", headers=headers)

# URL로부터 읽은 HTML 내용을 파이썬에서 처리할 수 있게 파싱하기
soup = BeautifulSoup(webpage.content, "html.parser")

# 수집한 신문기사 문자열의 앞에 자바스크립크 함수가 붙어있어 스크립트 제거
soup.select_one("#articleBodyContents > script").decompose();

# 신문기사 본문 내용을 문자열로 저장하기
naver_news = soup.select_one("#articleBodyContents").get_text().strip()

# 마침표 다음 문자에 띄어쓰기 없는 경우를 해결하기위해 .뒤에 띄어쓰기되도록 설정
naver_news = re.sub(r"[.]", ". ", naver_news)

# TTS 읽을 내용 출력
print(naver_news)

# TTS를 사용하기 위해 초기화
tts = pyttsx3.init()

# 말하기 속도 조절(기본값 : 200 / 값이 클수록 말속도가 빠르며, 작으면 느림)
tts.setProperty("rate", 180)

# 말하기
tts.say(naver_news)

# 파이썬이 종료되는 것을 막기 위해 말 끝날 때까지 대기
tts.runAndWait()

# 종료하기
tts.stop()
