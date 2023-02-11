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
            self.__check__(self)
            self.p = (self.triangle.a + self.triangle.b + self.triangle.c) / 2
            self.__is_triangle__()
            self.__solution_perimetr__(self)
            self.__solution_square__(self)
        except Exception as e:
            print(e)

    @staticmethod
    def __solution_perimetr__(self):
        print(f"P = a + b + c = "
              f"{self.triangle.a} + {self.triangle.b} + {self.triangle.c} = "
              f"{self.__find_perimetr__(self)}")

    @staticmethod
    def __find_perimetr__(self):
        return str(self.triangle.a + self.triangle.b + self.triangle.c)

    @staticmethod
    def __find_square__(self):
        square = (self.p * (self.p - self.triangle.a) * (self.p - self.triangle.b) * (self.p - self.triangle.c)) ** 0.5
        return square

    @staticmethod
    def __solution_square__(self):
        print(f"S = (p * (p - a) * (p - b) * (p - c) ^ 0.5 = "
              f"(({self.p} * ({self.p} - {self.triangle.a}) * ({self.p} - {self.triangle.b}) * ({self.p} - {self.triangle.c})) ^ 0.5 = "
              f"{self.__find_square__(self)} \n")

    def __is_triangle__(self):
        if self.triangle.a == self.triangle.b \
                and self.triangle.b == self.triangle.c:
            print('\nТреугольник: Равносторонний')
            return 1
        if self.triangle.a == self.triangle.b \
                or self.triangle.a == self.triangle.c \
                or self.triangle.c == self.triangle.b:
            print('\nТреугольник: Равнобедренный')
            return 2
        if ((self.triangle.a ** 2) + (self.triangle.b ** 2) == self.triangle.c ** 2) \
                or ((self.triangle.a ** 2) + (self.triangle.c ** 2) == self.triangle.b ** 2) \
                or ((self.triangle.b ** 2) + (self.triangle.c ** 2) == self.triangle.a ** 2):
            print('\nТреугольник: Прямоугольный')
            return 3
        print('\nТреугольник: Произвольный')
        return 4

    @staticmethod
    def __check__(self):
        if (self.triangle.a + self.triangle.b < self.triangle.c) \
                or (self.triangle.a + self.triangle.c < self.triangle.b) \
                or self.triangle.b + self.triangle.c < self.triangle.a:
            raise Exception("Такой треугольник не существует")
        return True


def test(array):
    equilateral = int()
    isosceles = int()
    rectangular = int()
    arbitrary = int()

    for item in array:
        el = item.__is_triangle__()
        if el == 1:
            equilateral += 1
        elif el == 2:
            isosceles += 1
        elif el == 3:
            rectangular += 1
        elif el == 4:
            arbitrary += 1

    test_info(equilateral, isosceles, rectangular, arbitrary)


def test_info(equilateral, isosceles, rectangular, arbitrary):
    print(f"\n\tРавносторонних: {equilateral}\n"
          f"\tРавнобедренных: {isosceles}\n"
          f"\tПрямоугольных: {rectangular}\n"
          f"\tПроизвольных: {arbitrary}\n")


def main():
    array = []

    tr1 = Triangle(3, 4, 5)
    tr1_ = SearchTriangle(tr1)
    tr1_.answer()

    array.append(tr1_)

    tr2 = Triangle(7, 5, 4)
    tr2_ = SearchTriangle(tr2)
    tr2_.answer()

    array.append(tr2_)

    test(array)

if __name__ == "__main__":
    main()
