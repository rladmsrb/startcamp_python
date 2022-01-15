import random


# 점심 메뉴 저장

menu = ['제육볶음', '닭강정', '볶음밥', '함박스테이크']

# print(menu)
phone = {'제육볶음' : '123-4567', '닭강정': '234-5687', '볶음밥' : '332-1234', '함박스테이크' : '342-1234'}

choice = random.choice(menu)
print('오늘의 추천 메뉴 =>', choice)
print('주문전화 =>', phone[choice])

