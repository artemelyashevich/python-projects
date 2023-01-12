class Polinom:
    a = float()
    b = float()
    c = float()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def print(self):
        print(f"{self.a}*x^2 + {self.b}*x + {self.c}")


class QuadraticEquation:
    polinom = Polinom  # composition
    d = float()
    x1 = float()
    x2 = float()

    def __init__(self, polinom):
        self.polinom = polinom
        self.d = self.__calculate_d__()
        self.dir = self.__direction__()

    def find_solution(self):
        try:
            self.__check_d__()
            self.x1 = (-self.polinom.b + self.d ** 0.5) / (2 * self.polinom.a)
            self.x2 = (-self.polinom.b - self.d ** 0.5) / (2 * self.polinom.a)
            self.x_top = -self.polinom.b / 2 * self.polinom.a
            self.y_top = self.polinom.a * (self.x_top ** 2) + self.polinom.b * self.x_top + self.polinom.c
            self.__print_solution__()
            self.__print_result_extremum__()
            self.__print_answer__()
        except Exception as e:
            print(e)

    @staticmethod
    def check_sign(val):
        if val < 0:
            return f"({val})"
        return f"{val}"

    def __print_result_extremum__(self):
        self.__print_details_extremum__()

    def __print_details_extremum__(self):
        print(f"\tx_top = -b / (2 * a) = "
              f"-{self.check_sign(self.polinom.b)} / (2 * {self.check_sign(self.polinom.a)}) = "
              f"{self.x_top};\n\t"
              f"y_top = a * x_top^2 + b * x_top + c = "
              f"{self.check_sign(self.polinom.a)} * {self.check_sign(self.x_top)} + {self.check_sign(self.polinom.b)}"
              f" * {self.check_sign(self.x_top)} + {self.check_sign(self.polinom.c)} = "
              f"{self.y_top};\n")

    def __check_direction__(self):
        if self.polinom.a < 0:
            return 'min'
        return 'max'

    def __print_solution__(self):
        print(f"\nSolution:\n"
              f"\tD = b^2 - 4*a*c = {self.check_sign(self.polinom.b)}^2 - "
              f"4*{self.check_sign(self.polinom.a)}*{self.check_sign(self.polinom.c)} = "
              f"{self.polinom.b ** 2} - {self.check_sign(4 * self.polinom.a * self.polinom.c)} = {self.d};\n"
              f"\tx1 = (-b + sqrt(D)) / (2 * a) = (-{self.check_sign(self.polinom.b)} +"
              f" sqrt({self.d})) / (2 * {self.check_sign(self.polinom.a)}) = {self.x1};\n"
              f"\tx2 = (-b - sqrt(D)) / (2 * a) = (-{self.check_sign(self.polinom.b)} -"
              f" sqrt({self.d})) / (2 * {self.check_sign(self.polinom.a)}) = {self.x2};\n")

    def __print_answer__(self):
        if self.x1 == self.x2:
            print(f"Answer:\n\tx1 = {self.x1}\n\t;"
                  f"{self.__check_direction__()} = {self.y_top}")
        else:
            print(f"Answer:\n\tx1 = {self.x1};\n\tx2 = {self.x2};\n\t"
                  f"{self.__check_direction__()} = {self.y_top};")
        self.__intervall__()

    def __calculate_d__(self):
        return self.polinom.b ** 2 - 4 * self.polinom.a * self.polinom.c

    def __check_d__(self):
        """ Encapsulation """
        if self.d < 0:
            raise Exception('D < 0')

    def __intervall__(self):
        if self.dir:
            print(f"\tФункция убывает до: {self.x_top}\n\t"
                  f"Функция возрастает от: {self.x_top}\n")
        else:
            print(f"\tФункция возрастает до: {self.x_top}\n\t"
                  f"Функция убывает от: {self.x_top}\n")

    def __direction__(self):
        return self.polinom.a > 0

