#!/usr/bin/python3

def list_division(my_List_1, my_list_2, list_length):
    new_list = []
    for i in range (0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("Wrong type")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
