#!/usr/bin/python3
for ir in range(100):
    if int(ir / 10) != ir % 10 and int(ir / 10) < ir % 10:
        print("{}{}".format(int(ir / 10), ir % 10), end="")
        if (ir != 89):
            print(", ", end="")
print("")
