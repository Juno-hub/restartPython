#애완동물을 소개해주세요~

animal = "고양이"
name = "해피"
age = 6
hobby = "낮잠"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "입니다")
# print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아합니다.")
# 'comma(,)는 " + + "과 같은 역할을 하는데 자료형 구분 없이 ex) str(age), str 함수없이 작성이 가능하다. 하지만 콤마를 사용하면 항상 한 칸 띄어쓰기 처리가 된다.
print(name,"는 ",age, "살이며, ",hobby,"을 아주 좋아합니다.")
print(name + "는 어른일까요? " + str(is_adult))