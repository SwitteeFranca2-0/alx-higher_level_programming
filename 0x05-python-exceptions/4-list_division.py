#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            new_list.append(div)
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(0)
    return new_list
