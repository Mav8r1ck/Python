number1=int(input('Enter class 1:\n'))
number2=int(input('Enter class 2:\n'))
number3=int(input('Enter class 3:\n'))

class1 = number1 // 2+number1%2
class2 = number2 // 2+number2%2
class3 = number3 // 2+number3%2

print('For class 1 ', class1)
print('For class 2 ', class2)
print('For class 3 ', class3)
print('For all', class1+class2+class3)