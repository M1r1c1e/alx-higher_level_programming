#!/usr/bin/python3
for numb in range(100):
    if numb == 99:
        print(numb)
    else:
        print("{}".format('0' + str(numb) if b < 10 else numb), end=", ")
