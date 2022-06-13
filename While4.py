#มาลองสร้างโปรแกรมที่ใช้ loop for กัน
#ทำเครื่องคิเลขบวกเลข วนซ้ำแบบมีจำนวนรอบแน่นอน
'''inputRound = int(input("Please Enter Number : ")) #inputจำนวนรอบ
sum = 0
for x in range(inputRound): #ใช้loop for
    inputNumber = int(input("x :")) #ใช้เครื่องหมายลูกน้ำไม่ได้'''

inputRound = int(input("Please Enter Number : ")) #inputจำนวนรอบ
sum = 0
print(list(range(inputRound)))
for x in range(inputRound): #ใช้loop for
    inputNumber = int(input("x"+str(x+1)+":")) #ใช้+ได้แต่จะerrorตรงx str(x)คือตัวกำหนดXเริ่มต้น ex.str(x) = x0 /  str(x+1) = x1
#Process finished with exit code 0