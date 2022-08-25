from math import sqrt


def smallestWord(test):
    # Using sorted() method
    test = sorted(test)

    # Print first word
    print(test[0])


if __name__ == "__main__":

    s = "text text2"
    l = list(s.split(" "))
    print(l)
    smallestWord(l)
