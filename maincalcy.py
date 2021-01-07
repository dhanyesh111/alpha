import cal
import history
import population
print("CHOICES:\n 1)Open Calculator \n 2)Show Full History \n 3)Show Specific Line In History\n 4)Clear History \n "
      "5)Load population \n 6)Insert into database \n 7)Clear database \n 8)Search  \n 9)Exit")
choices=("1","2","3","4","5","6","7","8","9")
while True:
    try:
        ch=int(input("Enter your choice"))
        if ch==1:
            str1 = input()
            ch = ["+", "-", "*", "/"]
            i = 0
            cal.calc(str1, i)
        elif ch==2:
            history.printfull()
        elif ch == 3:
            line=int(input("enter the line"))
            history.printline(line+1)
        elif ch==4:
            history.clearhistory()
        elif ch==5:
            population.load_db()
        elif ch == 6:
            population.insert()
        elif ch == 7:
            population.clear()
        elif ch == 8:
            population.select(input())
        elif ch == 9:
            break
        else:
            print("invalid option")
    except ValueError:
        print("invalid option")

