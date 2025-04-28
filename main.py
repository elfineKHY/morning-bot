import requests
import random
import datetime

# 단어 리스트
words = [
    {"word": "exchange", "meaning": "교환", "examples": ["I exchanged my book with a friend.", "They exchanged greetings.", "We exchanged gifts."]},
    {"word": "equality", "meaning": "평등", "examples": ["Equality is important.", "We fight for equality.", "He believes in equality."]},
    # (나머지 단어들도 여기 추가하면 돼)
]

# 오늘 날짜 기준 랜덤 선택
today = datetime.datetime.now().day
selected = words[today % len(words)]

# 메세지 포맷
content = f"**Word of the Day**\n\n**{selected['word']}** ({selected['meaning']})\n- {selected['examples'][0]}\n- {selected['examples'][1]}\n- {selected['examples'][2]}"

# 디스코드 웹후크
WEBHOOK_URL = "https://discord.com/api/webhooks/~~(네 웹후크 주소)~~"

# 디스코드로 전송
requests.post(WEBHOOK_URL, json={"content": content})
