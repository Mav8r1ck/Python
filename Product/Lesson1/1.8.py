a=int(input('Расстояние между рядами:\n'))
b=int(input('Расстояние между дырками:\n'))
N=int(input('Количество дырок:\n'))

length= (((a*2*N)-a)+((b*2)*(N-1)))+1
print('legth = ', length)