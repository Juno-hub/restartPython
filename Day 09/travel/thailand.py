class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")


if __name__ == "__main__":
    print("Directly implement Thailand module.")
    print("This sentence appear when module is directly implement.")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Call up outside Thailand module")