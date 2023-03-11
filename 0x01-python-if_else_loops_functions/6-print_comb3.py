#!/usr/bin/python3
for z in range(10):
	for x in range(z + 1,10):
		if z == 8 and x == 9:
			print(f"{z}{x}")
		else:
			print(f"{z}{x}", end=", ")
