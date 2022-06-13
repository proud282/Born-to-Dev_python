# Lecture 47 : การใช้งาน Break และ Continue
'''for x in range(12):
    for y in range(12):
        print(x + 1, "x", y + 1, "=", (x + 1) * (y + 1))
    break'''
#break = คำสั่งให้ออกจากloop

'''for x in range(12):
    for y in range(12):
        print(x + 1, "x", y + 1, "=", (x + 1) * (y + 1))
        break #ออกเฉพาะloop y'''

'''for x in range(12):
    break
    for y in range(12):
        print(x + 1, "x", y + 1, "=", (x + 1) * (y + 1))
         '''

for val in "hello":
    if val == "l":
        continue
    print(val)

print("The end")