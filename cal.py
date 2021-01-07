import pickle
import time


def calc(x, i):
    global result
    str2 = ""
    try:
        file = open("database.py", "ab")
        result = eval(x)
        i += 1
        print("="+result)
        data = str(i) + ")" + str(x) + "=" + str(result) + "added at " + str(time.time())
        pickle.dump(data, file)
        file.close()
    except NameError:
        print("invalid name")
    except SyntaxError:
        print("invalid syntax")
    ch = input("------------")
    if ch == "n":
        return
    str2 = input(result)
    str1 = str(result) + str2
    calc(str(str1), i)
