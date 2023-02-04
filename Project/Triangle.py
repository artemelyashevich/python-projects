class Triangle:
    a = int()
    b = int()
    c = int()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def print(self):
        print("A = {} \nB = {} \nC= {}".format(self.a, self.b, self.c))


class SearchTriangle:
    triangle = Triangle
    p = float()

    def __init__(self, triangle):
        self.triangle = triangle

    def answer(self):
        try:
            self.__check__()
            self.p = (self.triangle.a + self.triangle.b + self.triangle.c) / 2
            self.__is_triangle__()
            self.__solution_perimetr__()
            self.__solution_square__()
        except Exception as e:
            print(e)

    def __solution_perimetr__(self):
        print(f"P = a + b + c = "
              f"{self.triangle.a} + {self.triangle.b} + {self.triangle.c} = "
              f"{self.__find_perimetr__()}")

    def __find_perimetr__(self):
        return str(self.triangle.a + self.triangle.b + self.triangle.c)

    def __find_square__(self):
        square = (self.p * (self.p - self.triangle.a) * (self.p - self.triangle.b) * (self.p - self.triangle.c)) ** 0.5
        return square

    def __solution_square__(self):
        print(f"S = (p * (p - a) * (p - b) * (p - c) ^ 0.5 = "
              f"(({self.p} * ({self.p} - {self.triangle.a}) * ({self.p} - {self.triangle.b}) * ({self.p} - {self.triangle.c})) ^ 0.5 = "
              f"{self.__find_square__()} \n")

    def __is_triangle__(self):
        if self.triangle.a == self.triangle.b \
                and self.triangle.b == self.triangle.c:
            return print('\nТреугольник: Равносторонний')
        if self.triangle.a == self.triangle.b \
                or self.triangle.a == self.triangle.c \
                or self.triangle.c == self.triangle.b:
            return print('\nТреугольник: Равнобедренный')
        if ((self.triangle.a ** 2) + (self.triangle.b ** 2) == self.triangle.c ** 2) \
                or ((self.triangle.a ** 2) + (self.triangle.c ** 2) == self.triangle.b ** 2) \
                or ((self.triangle.b ** 2) + (self.triangle.c ** 2) == self.triangle.a ** 2):
            return print('\nТреугольник: Прямоугольный')
        return print('\nТреугольник: Произвольный')

    def __check__(self):
        if (self.triangle.a + self.triangle.b < self.triangle.c) \
                or (self.triangle.a + self.triangle.c < self.triangle.b) \
                or self.triangle.b + self.triangle.c < self.triangle.a:
            raise Exception("Такой треугольник не существует")
        return True
