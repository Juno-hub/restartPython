# Right alignment, take up ten digit.
print("{0: >10}".format(500))
# If the number is positive, mark '+' and if the number is negative, mark '-'
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# Left alignment, empty is filled "_"
print("{0:_<10}".format(500))
# print ",(comma)" by three digit
print("{0:,}".format(100000000000))
# print ",(comma)" by three digit and mark "+" or "-"
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))
# Mixing what I've learnde so for, empty is filled ^
print("{0:^<+30,}".format(100000000000))
# {0:empty | align | + | space | ,}
# Display decimal point
print("{0:f}".format(5 / 3))
print("{0:.2f}".format(5 / 3))
