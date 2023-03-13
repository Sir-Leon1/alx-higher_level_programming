#!/usr/bin/python3
for j in range(97, 123):
    if chr(j) not in ["q", "e"]:
<<<<<<< HEAD
        print(f"{chr(j)}", end="")
=======
        print("{}".format(chr(j)), end="")
>>>>>>> 49f36a77b2d281a1c56da2da806b4ef055c1854d
