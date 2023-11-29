#!/usr/bin/python3
for nb in range(100):
    if nb == 99:
        print(nb)
    else:
        print("{}".format('0' + str(nb) if nb < 10 else nb), end=", ")
