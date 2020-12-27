# Q) There is your company's rule that employee make a report every week.
# Your report should be made like under form.
# - X week Report -
# Department:
# Name:
# Summary:

# Code a programm make the first ~ 50th week report file.

# Rule: File should have name like '1 week.txt', '2 week.txt', ...

# My answer
for weeks in range(1, 51):
    with open(str(weeks) + " week.txt", "w", encoding="utf8") as report_file:
        report_file.write("- " + str(weeks) + " week Report -")
        report_file.write("\nDepartment: ")
        report_file.write("\nName: ")
        report_file.write("\nSummary: ")

# 나도코딩 answer
for i in range(1, 51):
    with open(str(i) + " week.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} week Report -".format(i))
        report_file.write("\nDepartment: ")
        report_file.write("\nName: ")
        report_file.write("\nSummary: ")
