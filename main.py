# coding=utf-8
from algos import Algos


if __name__ == '__main__':
    algos = Algos()

    print("Метод половинного деления")
    print(algos.half_division())
    print("------------------------------------------------")

    print("Метод Ньютона")
    print(algos.newton_method())
    print("------------------------------------------------")

    print("Модифицированный метод Ньютона")
    print(algos.modified_newton_method())
    print("------------------------------------------------")

    print("Метод хорд")
    print(algos.chords_method())
    print("------------------------------------------------")

    print("Метод подвижных хорд")
    print(algos.movable_chords_method())
    print("------------------------------------------------")

    print("Метод простой итерации")
    print(algos.solve_simple_iteration_method())
    print("------------------------------------------------")