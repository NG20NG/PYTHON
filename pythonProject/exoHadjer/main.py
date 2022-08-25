from equations import try_agan, first_deg, second_deg
from limit import limit_test

if __name__ == "__main__":
    on = True
    while on:
        print("1 - First-Degree Equation")
        print("2 - Second-Degree Equation")
        print("3 - limits")
        try:
            choose_equation = int(input("choose a function :"))
            if choose_equation == 1:
                first_deg()
                try_agan(on)

            elif choose_equation == 2:
                second_deg()
                try_agan(on)

            elif choose_equation == 3:
                limit_test()
                try_agan(on)

            print("=================================")
        except:
            print("---------ERROR---------")
