#Lecture 48 : ตัวอย่างการพัฒนาโปรแกรมแบบวนซ้ำ
'''number = int(input())
for i in range(number):
    print("*")'''

'''number = int(input())
    print(number*"*")''' # 3--> ***


'''number = int(input())
for x in range(number): 
    text = ""
    for y in range(x+1): #วนloopเพิ่มจำนวนขึ้นเรื่อยๆ
        text += "*"     #สร้างstring เพราะการที่ตัวเลขจะต่อกันได้จะต้องเองstring+กัน
    print(text)'''

number = int(input())
for x in range(number): #ใช้loop for เมื่อมีจำนวนรอบที่แน่นอน
    print("*"*(x+1))

'''
5
*
**
***
****
*****

Process finished with exit code 0
'''
