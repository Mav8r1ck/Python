n = int(input('Введите n minutes: '))


day = 60*24
h = (day-n)//60
m = (day-60*h)-n

print(int(h),str(":"),int(m))