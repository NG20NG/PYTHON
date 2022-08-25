
from cmath import sqrt


def try_agan(e):
    end_func = input("try agan ? :")
    if end_func:
        e = False


def first_deg():
    try:
        a = int(input("a = "))
        b = int(input("b = "))
        f = input("function = ")

        def sol(e, c):
            print("-----------------")
            print(f"f(x) = {a}x {e} {b}")
            print(f"1 : {a}x = {c}{b}")
            print(f"2 : x = {c}{b} / {a}")
            print(f"3 : x = {c}{b / a}")
            print("-----------------")

        if f == "+":
            sol(f, "-")
        elif f == "-":
            sol(f, "")
        else:
            print("---------not a function---------")
    except:
        print("---------NAN---------")


def second_deg(elem):
    try:
        a = int(input("a = "))
        b = int(input("b = "))
        c = int(input("c = "))
        delta = sqrt(pow(b, 2) - 4 * a * c)
        delta2 = pow(b, 2) - (4 * a * c)
        print("(1) -----------------")
        print("D = B² − 4AC")
        print(f"D = {b}² - 4{a}{c}")
        print(f"D = {pow(b, 2)} - 4*{a}*{c}")
        print(f"D = {delta2}")
        print(f"D = {delta}")
        if delta2 < 0:
            print("(2) -----------------")
            print("Si Δ < 0 : L'équation ax² + bx + c = 0 n'a pas de solution réelle.")
            print(f"x = -{b} - {delta} / 2*{a}")
            print(f"x = -{b} + {delta} / 2*{a}")
            print("(3) -----------------")
            print(f"x = -{b} - {delta} / {2*a}")
            print(f"x = -{b} + {delta} / {2*a}")
            print("no solution for this one")
            print("-----------------")
        elif delta2 == 0:
            print("(2) -----------------")
            print("Si Δ = 0 : L'équation ax² + bx + c = 0 a une unique solution : -b / 2a")
            print("x = -b / 2a")
            print("(3) -----------------")
            print(f"x = -{b} / 2{a}")
            print("-----------------")
        elif delta2 > 0:
            print("(2) -----------------")
            print("Si Δ > 0 : L'équation ax² + bx + c = 0 a deux solutions distinctes : ")
            print("x1 = -b - √D / 2a")
            print("x2 = -b + √D / 2a")
            print("(3) -----------------")
            print(f"x1 = {-b} - √{delta} / 2{a}")
            print(f"x1 = {-b} + √{delta} / 2{a}")
            print("-----------------")
    except:
        print("---------NAN---------")
