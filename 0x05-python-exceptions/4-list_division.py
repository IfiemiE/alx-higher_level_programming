#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    prod_list = []
    for i in range(list_length):
        try:
            div = my_list1[i] / my_list2[i]

        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        except TypeError:
            print("wrong type")
            div = 0

        finally:
            prod_list.append(div)

    return (prod_list)
