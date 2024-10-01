a,b,c  = int(input()), int(input()), int(input())

if a == b == c:
    print("Равносторонний треугольник")
elif a == b or b == c or a == c:
    print("Равнобедренный треугольник")
elif a + c == b or a + b == c or a == c + b:
    print("Прямоугольный треугольник")
else:
    print("Разносторонний треугольник")
