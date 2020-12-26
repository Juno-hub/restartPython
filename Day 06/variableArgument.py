# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("Name: {0}\tAge: {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)


def profile(name, age, *language):
    print("Name: {0}\tAge: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile("유재석", 20, "Pyhton", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")