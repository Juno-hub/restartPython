# Q) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건1: 랜덤으로 날짜를 뽑아야 함.
# 조건2: 월별 날짜는 다름을 감안하여 최소 일 수인 28 이내로 정함.
# 조건3: 매월 1~3일은 스터디 준비를 해야하므로 제외함.

# (출력물 예제)
# 오프라인 스터디 모임 날짜는 매월 x 일로 선정하였습니다.

from random import *

randomDateGenerator = randint(4, 28)

print("오프라인 스터디 모임 날짜는 매월 " + str(randomDateGenerator) + " 일로 선정하였습니다.")

# Debriefing
# 1. When I use random function, insert from random import *
# 2. Use str(), if variable is not string
