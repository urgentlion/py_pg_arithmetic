test1 = bool("testing type conversion")
print(test1)

test2 = int(9.8)
print(test2)

test3 = int(False)
print(test3)

test4 = str(bool(12 // 2 - 5))
test5 = str(bool(12.0 // 2 - 5))
test6 = str(bool(1 // 2 - 5))

print(test4)
print(test5)
print(test6)