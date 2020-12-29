# import glob

# print(glob.glob("*.py")) All of file of extension is py

# os : basic function support operating system
# import os

# print(os.getcwd())  # 현재 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("This folder already exists.")
#     os.rmdir(folder)
#     print(folder, "Remove the folder.")
# else:
#     os.makedirs(folder)
#     print(folder, "Make a folder.")
# print(os.listdir())

# import time

# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime

# print("Today's date is ", datetime.date.today())

today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은", today + td)