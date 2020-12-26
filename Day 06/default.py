def profile(name, age, main_lang):
    print("Name: {0}\tAge: {1}\tMain language: {2}".format(name, age, main_lang))


profile("유재석", 20, "Python")
profile("김태호", 25, "Java")

# Same school, grade, class
def profileS(name, age=17, main_lang="Python"):
    print("Name: {0}\tAge: {1}\tMain language: {2}".format(name, age, main_lang))


profileS("유재석")
profileS("김태호")