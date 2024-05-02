#!/usr/bin/python3


class MyInt(int):
    # invert int operators == and !=

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
