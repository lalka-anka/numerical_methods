# coding=utf-8
import math


def ctg(x):
    return math.cos(x) / math.sin(x)


def function(x):
    return ctg(x + 0.2) - x*x


def first_function_derivation(x):
    return -2 * x - 1 / (math.pow(math.sin(x + 0.2), 2))


def second_function_derivation(x):
    return -2 + 2 * math.cos(x + 0.2) / math.pow(math.sin(x + 0.2), 3)


def phi(x):
    return x + (-1 / first_function_derivation(x)) * function(x)


class Algos:

    def __init__(self):
        self.confines = (0.5, 1)
        self.x_0 = 0.5
        self.accuracy = 5e-06

    def half_division(self):
        num = (self.confines[1] - self.confines[0]) / self.accuracy
        iteration_count = int(math.ceil(math.log(num, 2)))
        print("iterations count: ", iteration_count)
        (left, right) = self.confines
        for _ in range(iteration_count):
            mid = (left + right) / 2
            if function(left) * function(mid) < 0:
                right = mid
            elif function(mid) * function(right) < 0:
                left = mid
            elif function(left) == 0:
                return function(left)
            elif function(right) == 0:
                return function(right)
            elif function(mid) == 0:
                return function(mid)
            else:
                raise Exception("Error")

        return left, right

    def newton_method(self):
        counter = 0
        x_n = self.x_0

        while True:
            counter += 1
            new_x_n = x_n - function(x_n) / first_function_derivation(x_n)
            if self.accuracy >= math.fabs(new_x_n - x_n):
                print("iterations count: ", counter)
                return new_x_n
            x_n = new_x_n

    def modified_newton_method(self):
        counter = 0
        x_n = self.x_0

        while True:
            counter += 1
            new_x_n = x_n - function(x_n) / first_function_derivation(self.x_0)
            if self.accuracy >= math.fabs(new_x_n - x_n):
                print("iterations count: ", counter)
                return new_x_n
            x_n = new_x_n

    def chords_method(self):
        counter = 0
        x_n = self.confines[1] if self.x_0 == self.confines[0] else self.confines[0]

        while True:
            counter += 1
            new_x_n = x_n - (function(x_n) * (x_n - self.x_0)) / (function(x_n) - function(self.x_0))
            if self.accuracy >= math.fabs(new_x_n - x_n):
                print("iterations count: ", counter)
                return new_x_n
            x_n = new_x_n

    def movable_chords_method(self):
        counter = 0
        x_n_previous = self.x_0

        if self.x_0 == self.confines[0]:
            x_n = self.confines[1]
        else:
            x_n = self.confines[0]

        while True:
            counter += 1
            new_x_n = x_n - (function(x_n) * (x_n - x_n_previous)) / (function(x_n) - function(x_n_previous))
            if self.accuracy >= math.fabs(new_x_n - x_n):
                print("iterations count: ", counter)
                return new_x_n
            x_n_previous = x_n
            x_n = new_x_n

    def solve_simple_iteration_method(self):
        counter = 0
        x_n = self.x_0

        while True:
            counter += 1
            new_x_n = phi(x_n)
            if self.accuracy >= math.fabs(new_x_n - x_n):
                print("iterations count: ", counter)
                return new_x_n
            x_n = new_x_n
