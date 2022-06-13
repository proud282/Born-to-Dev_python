# สังเกตpattern
'''print("2 x 1 = 2")
print("2 x 2 = 4")
print("2 x 3 = 6")

x = 1
y = 2*x
print("2 x", x, "=", y)

x = x+1
y = 2*x
print("2 x", x, "=", y)'''

'''for x in range(12):
   print("2 x", x+1, "=", 2*(x+1))'''

for x in range(12):
   for y in range(12): #วนซ้ำloopเล็กก่อน วนครบแล้ว ค่อยวนloopใหญ่ต่อ
      print(x+1 ,"x", y+1, "=", (x+1)*(y+1))