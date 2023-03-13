#!/usr/bin/python3
for i in range(100):
    if i == 99:
<<<<<<< HEAD
        print(f"{i}")
    else:
        print(f"{i:02}", end=", ")
=======
        print("{}".format(i))
    else:
        print("{:02}".format(i), end=", ")
>>>>>>> 49f36a77b2d281a1c56da2da806b4ef055c1854d
