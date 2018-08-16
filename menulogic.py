import random

def reply(text):

    lunch_menu = '분식', '한식', '일식', '중식', '양식', '기타', '정말 제가 골라야 하나요?'
    dinner_menu = '분식', '한식', '일식', '중식', '양식', '기타', '저녁은 됐고.. 술이나 마실까요?'
    Korean_snack = '라면', '떡볶이', '순대', '튀김', '만두', '김밥', '모르겠는데요...'
    Korean = '김치찌개', '낙곱새', '순대국', '해장국', '감자탕', '국수', '냉면', '죽', '갈비찜', '쭈꾸미', '오늘은 다이어트 어때요?'
    Japanese = '돈부리', '라멘', '스시', '회덮밥', '벤또', '카레', '돈까스', '이랏샤이마세!!!'
    Chinese = '짬뽕', '냉짬뽕', '짜장면', '볶음밥', '탕수육', '군만두', '깐쇼새우', '양꼬치엔 역시 칭따오(응?)'
    Europian = '파스타', '피자', '샐러드', '빵', '수프', '샌드위치', '햄버거'
    undefined = '쌀국수', '편의점 도시락', '아무거나...'
    alcohol = '소주', '맥주', '소맥', '폭탄주', '고량주', '와인', '사케', '막걸리', '동동주'
    snack_for_alcohol = '삼겹살', '치킨', '보쌈', '족발', '피자', '양꼬치', '곱창/막창', '감자튀김', '김치전'
    snack = '빵', '과자', '케이크', '마카롱', '초콜릿', '파이', '파이썬(뭐라구?)'
    drink = '커피', '홍차', '녹차', '주스', '에이드', '밀크티', '버블티', '낮술(응?)'
    delivery = '호토모토', '서브웨이', '프레시코드', '핫베어케밥김밥', '메뉴 추가해 주세요ㅠㅠ'
    store = '창업허브 3층', '모두의 부엌(복지타운 1층)', '홍대개미', '낙곱새', '을밀대', '오레노라멘♥', '굴다리식당', '여명', '맹그로브', '은행골', '홍루이젠', '맘스터치', '락희옥', '김재운의 초밥사랑', '본죽'

    cheer_up = '인생은 끊임없는 반복, 반복에 지치지 않는 자가 성취한다. - by 미생', '우리는 모두 자신의 힘으로 발견한 내용을 가장 쉽게 익힌다. - by 도널드 크누스(생활코딩 펌)'

    Alan = '지속가능하게 갈아넣으세요ㅎㅎㅎ'
    Joeun = 'T~WL도 각자 가드닝을 해주시면 좋을 것 같애요'
    Zzae = '단락 배분 좋구요, 첫 문장에 500원 있고, 아주 좋아요!'
    Jihyun = '여러분~ 2분 드릴테니 한번 풀어보세요'
    TC = '이게 데잇걸즈 커뮤니티 매니저에 지원했던 자소서에요, 근데 옆에서 보니까 저는 못할것 같아요^^;;'
    Blue = '파이에 햇볕을 쬐면... 파이썬.'
    CM = '(웃으면서)여러분~ 출석체크 시작할게요'
    Anne = '(떨리는 목소리로) 제가 지금 엄청 긴장이 되는데요...'

    if "점심메뉴" in text:
        menu = str(random.choice(lunch_menu))
        return menu
    elif "저녁메뉴" in text:
        menu = str(random.choice(dinner_menu))
        return menu
    elif "분식메뉴" in text:
        menu = str(random.choice(Korean_snack))
        return menu
    elif "한식메뉴" in text:
        menu = str(random.choice(Korean))
        return menu
    elif "일식메뉴" in text:
        menu = str(random.choice(Japanese))
        return menu
    elif "중식메뉴" in text:
        menu = str(random.choice(Chinese))
        return menu
    elif "양식메뉴" in text:
        menu = str(random.choice(Europian))
        return menu
    elif "기타메뉴" in text:
        menu = str(random.choice(undefined))
        return menu
    elif "술메뉴" in text:
        menu = str(random.choice(alcohol))
        return menu
    elif "안주메뉴" in text:
        menu = str(random.choice(snack_for_alcohol))
        return menu
    elif "간식메뉴" in text:
        menu = str(random.choice(snack))
        return menu
    elif "음료메뉴" in text:
        menu = str(random.choice(drink))
        return menu
    elif "배달메뉴" in text:
        menu = str(random.choice(delivery))
        return menu
    elif "식당메뉴" in text:
        menu = str(random.choice(store))
        return menu

    elif "격려" in text:
        word = str(random.choice(cheer_up))
        return word

    elif "애란선생님" in text:
        return Alan
    elif "배로선생님" in text:
        return Joeun
    elif "지해선생님" in text:
        return Zzae
    elif "지현선생님" in text:
        return Jihyun
    elif "TC은정님" in text:
        return TC
    elif "블루님" in text:
        return Blue
    elif "CM성윤님" in text:
        return CM
    elif "Anne님" in text:
        return Anne

    else:
        return None
