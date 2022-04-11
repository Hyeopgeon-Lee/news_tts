import requests
import re
from bs4 import BeautifulSoup

# 네이버는 정상적인 접근(사용자 직접 네이버 접속)이 아닌 웹 크롤링 등 비정상적인 접근을 방지 하게 위해 HTTP 해더 정보를 요구함
# HTTP 해더는 웹URL에 접속할 때, 네이버 서버에 제공하는 메타 정보
# 네이버는 HTTP 해더 정보 중 User-Agent 값의 유무를 체크함
# 따라서 네이버에 임의의 값을 넣어줌
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

# 신문기사 출력
print(naver_news)

f = open("mynews.txt", "w",  encoding="UTF-8")
f.write(naver_news)
f.close()



