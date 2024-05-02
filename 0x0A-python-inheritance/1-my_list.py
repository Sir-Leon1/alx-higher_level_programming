#!/usr/bin/python3


class MyList(list):
    # Implements sorted printing for the built-in list class

    def print_sorted(self):
        # print list in sorted ascending order
        print(sorted(self))
