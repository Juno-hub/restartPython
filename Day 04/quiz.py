# Q) 사이트 별로 비밀번호를 만들어주는 프로그램을 작성하시오.

# Ex) http://naver.com
# 규칙1: http:// 부분은 제외 => naver.com
# 규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3: 남은 글자 중 처음 세자리 + 글자 개수+ 글자 내 'e'의 개수 + '!'로 구성
#             (nav)                   (5)         (1)              (!)

# A) Password: nav51!

# Q) http://google.com

# My answer
url = "http://google.com"
slash_first_index = url.index("/")  # 5
slashIndex = slash_first_index + 2  # 7, To consider HTTPS protocol
pointIndex = url.index(".")  # 13
name = url[slashIndex:pointIndex]  # google
init = name[:3]  # goo
letterCount = len(name)  # 6
eCount = name.count("e")  # 1
rule3 = init + str(letterCount) + str(eCount) + "!"

print("Password: " + rule3)

# 나도코딩 answer
url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[: my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(url, password))

# Debriefing
# My code has many lines and variables.
# Example of

#         slash_first_index = url.index("/")
#         slashIndex = slash_first_index + 2,

# this code can replace

#         my_str = url.replace("http://", "")

# Also,
#         my_str = my_str[: my_str.index(".")]

# like this I should have reduced the number of variable.
