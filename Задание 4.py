a = int(input("Первая сторона "))
b = int(input("Вторая сторона "))
c = int(input("Третья сторона "))
if c<a+b and b<a+c and a<c+b:
    print("Треугольник существует")
else:
    print("Треугольник не существует")
    
