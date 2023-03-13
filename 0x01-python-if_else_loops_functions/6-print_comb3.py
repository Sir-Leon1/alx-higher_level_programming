#!/usr/bin/python3
for z in range(10):
    for x in range(z + 1, 10):
        if z == 8 and x == 9:
<<<<<<< HEAD
            print(f"{z}{x}")
        else:
            print(f"{z}{x}", end=", ")
=======
            print("{}{}".format(z, x))
        else:
            print("{}{}".format(z, x), end=", ")
>>>>>>> 49f36a77b2d281a1c56da2da806b4ef055c1854d
