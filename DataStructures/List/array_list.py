def new_list():
    newlist = {
        "elements": [],
        "size": 0,
    }
    return newlist

def get_element(my_list, index):
    
    return my_list["elements"][index]

def is_present(my_list, element,  cmp_function):
    
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
            if keyexist:
                return keypos
    return -1

def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    
def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    
def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range')
    return my_list["elements"][0]

def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    return False

def last_element(my_list):
    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range')
    return my_list["elements"][my_list["size"] - 1]

def delete_element(my_list, pos):
    if pos >= my_list["size"] or pos < 0:
        raise Exception('IndexError: list index out of range')
    my_list["elements"].pop(pos)
    my_list["size"] -= 1
    return my_list

def remove_first(my_list):
    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range')
    my_list["size"] -= 1
    return my_list["elements"].pop(0)

def remove_last(my_list):
    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range')
    my_list["size"] -= 1
    return my_list["elements"].pop(my_list["size"] - 1)

def insert_element(my_list, pos, element):
    if pos > my_list["size"] or pos < 0:
        raise Exception('IndexError: list index out of range')
    my_list["elements"].insert(pos, element)
    my_list["size"] += 1
    return my_list

def change_info(my_list, pos, new_info):
    if pos >= my_list["size"] or pos < 0:
        raise Exception('IndexError: list index out of range')
    my_list["elements"][pos] = new_info
    return my_list

def exchange(my_list, pos1, pos2):
    if pos1 >= my_list["size"] or pos1 < 0 or pos2 >= my_list["size"] or pos2 < 0:
        raise Exception('IndexError: list index out of range')
    my_list["elements"][pos1] = my_list["elements"][pos2]
    my_list["elements"][pos2] = my_list["elements"][pos1]
    return my_list

def sub_list(my_list, pos_i, num_elements):
    if pos_i >= my_list["size"] or pos_i < 0 or num_elements < 0 or num_elements > my_list["size"] - pos_i:
        raise Exception('IndexError: list index out of range')
    
    sublist = {
        "elements": my_list["elements"][pos_i:pos_i + num_elements],
        "size": num_elements,
    }
    return sublist

def default_sort_criteria(element1, element2):
    return element1 < element2

def selection_sort(my_list, default_sort_criteria):
    size = my_list["size"]
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if default_sort_criteria(my_list["elements"][j], my_list["elements"][min_index]):
                min_index = j
        if min_index != i:
            exchange(my_list, i, min_index)
    return my_list

def insertion_sort(my_list, default_sort_criteria):
    size = my_list["size"]
    for i in range(1, size):
        key = my_list["elements"][i]
        j = i - 1
        while j >= 0 and default_sort_criteria(key, my_list["elements"][j]):
            my_list["elements"][j + 1] = my_list["elements"][j]
            j -= 1
        my_list["elements"][j + 1] = key
    return my_list

def shell_sort(my_list, default_sort_criteria):
    n = my_list["size"]
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            elem = my_list["elements"][i]
            j = i
            while j >= gap and not default_sort_criteria(my_list["elements"][j - gap], elem):
                my_list["elements"][j] = my_list["elements"][j - gap]
                j -= gap
            my_list["elements"][j] = elem
        gap //= 2
    return my_list

def merge_sort(my_list, default_sort_criteria):
    if my_list["size"] <= 1:
        return my_list

    mid = my_list["size"] // 2
    left_half = new_list()
    right_half = new_list()

    for i in range(mid):
        add_last(left_half, get_element(my_list, i))
    for i in range(mid, my_list["size"]):
        add_last(right_half, get_element(my_list, i))

    merge_sort(left_half, default_sort_criteria)
    merge_sort(right_half, default_sort_criteria)

    i = j = k = 0
    while i < left_half["size"] and j < right_half["size"]:
        if default_sort_criteria(get_element(left_half, i), get_element(right_half, j)):
            change_info(my_list, k, get_element(left_half, i))
            i += 1
        else:
            change_info(my_list, k, get_element(right_half, j))
            j += 1
        k += 1

    while i < left_half["size"]:
        change_info(my_list, k, get_element(left_half, i))
        i += 1
        k += 1

    while j < right_half["size"]:
        change_info(my_list, k, get_element(right_half, j))
        j += 1
        k += 1

    return my_list

def quick_sort(my_list, default_sort_criteria):
    if my_list["size"] <= 1:
        return my_list

    pivot = get_element(my_list, my_list["size"] // 2)
    left = new_list()
    right = new_list()

    for i in range(my_list["size"]):
        if i == my_list["size"] // 2:
            continue
        elem = get_element(my_list, i)
        if default_sort_criteria(elem, pivot):
            add_last(left, elem)
        else:
            add_last(right, elem)

    quick_sort(left, default_sort_criteria)
    quick_sort(right, default_sort_criteria)

    my_list["elements"] = left["elements"] + [pivot] + right["elements"]
    my_list["size"] = left["size"] + 1 + right["size"]

    return my_list