#!/usr/bin/python3
for num in range(0, 80):
    s = num % 10
    t = num / 10
    print("{}".format(s),"{}".format(t), end='\n')
