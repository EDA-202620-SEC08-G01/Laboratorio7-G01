from DataStructures.Tree import bst_node as bn
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl

def new_map():
    """
    Crea un nuevo árbol binario de búsqueda (BST) vacío.

    :returns: Árbol binario de búsqueda vacío
    :rtype: dict
    """
    return {"root": None, "type": "BST"}

def remove_node(root, key):
    if root is None:
        return None
    
    cmp = default_compare(key, root)
    
    if cmp == 0:
        if root["left"] is None:
            return root["right"]
        elif root["right"] is None:
            return root["left"]
        else:
            min_node = get_min_node(root["right"])
            root["key"] = min_node["key"]
            root["value"] = min_node["value"]
            root["right"] = remove_node(root["right"], min_node["key"])
    elif cmp == 1:
        root["right"] = remove_node(root["right"], key)
    else:
        root["left"] = remove_node(root["left"], key)
    
    return root

def remove(my_bst, key):
    my_bst["root"] = remove_node(my_bst["root"], key)
    return my_bst

def floor_node(root, key):
    if root is None:
        return None
    
    cmp = default_compare(key, root)
    
    if cmp == 0:
        return root
    elif cmp == -1:
        return floor_node(root["left"], key)
    else:
        right_floor = floor_node(root["right"], key)
        if right_floor is not None:
            return right_floor
        else:
            return root

def floor(my_bst, key):
    return floor_node(my_bst["root"], key)

def ceiling_node(root, key):
    if root is None:
        return None
    
    cmp = default_compare(key, root)
    
    if cmp == 0:
        return root
    elif cmp == 1:
        return ceiling_node(root["right"], key)
    else:
        left_ceiling = ceiling_node(root["left"], key)
        if left_ceiling is not None:
            return left_ceiling
        else:
            return root

def ceiling(my_bst, key):
    return ceiling_node(my_bst["root"], key)

def select_node(root, k):
    if root is None:
        return None
    
    left_size = size_tree(root["left"])
    
    if k < left_size:
        return select_node(root["left"], k)
    elif k > left_size:
        return select_node(root["right"], k - left_size - 1)
    else:
        return root

def select(my_bst, k):
    return select_node(my_bst["root"], k)

def rank_node(root, key):
    if root is None:
        return 0
    
    cmp = default_compare(key, root)
    
    if cmp == -1:
        return rank_node(root["left"], key)
    elif cmp == 1:
        left_size = size_tree(root["left"])
        return left_size + 1 + rank_node(root["right"], key)
    else:
        return size_tree(root["left"])

def rank(my_bst, key):
    return rank_node(my_bst["root"], key)

def insert_node (root, key,  value):
    if root is None:
        return bn.new_node(key,value)
         
    cmp= default_compare(key,root)
    
    if cmp == 0 :
        root["value"]= value
    elif cmp ==1 :
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["left"] = insert_node(root["left"], key, value)    
    return root 

def put (my_bst, key, value):
    return insert_node(my_bst, key, value)    
    
def default_compare(key, element):
    if key == bn.get_key(element):
        return 0
    elif key > bn.get_key(element):
        return 1
    return -1

def size_tree(root):
    if root is None:
        return 0
    else:
        return size_tree(root['left']) + 1 + size_tree(root['right'])

def size(my_bst):
    return size_tree(my_bst['root'])


def get_node(root, key):
    if root is None:
        return None
    
    cmp = default_compare(key, root)
    
    if cmp == 0:
        return root
    elif cmp == 1:
        return get_node(root["right"], key)
    else: 
        return get_node(root["left"], key)

def get(my_bst, key):
    return get_node(my_bst, key)

def contains(my_bst, key):
    return get_node(my_bst, key) is not None

def is_empty(my_bst):
    return size(my_bst) == 0

def key_set_tree(root, key_set):
    if root is None:
        return key_set
    else:
        key_set_tree(root['left'], key_set)
        al.add_last(key_set, bn.get_key(root))
        key_set_tree(root['right'], key_set)
        return key_set

def key_set(my_bst):
    resultado = al.new_list()
    return key_set_tree(my_bst['root'], resultado)

def value_set_tree(root, value_set):
    if root is None:
        return value_set
    else:
        value_set_tree(root['left'], value_set)
        al.add_last(value_set, bn.get_value(root))
        value_set_tree(root['right'], value_set)
        return value_set

def value_set(my_bst):
    resultado = al.new_list()
    return value_set_tree(my_bst['root'], resultado)

def get_min_node(root):
    if root is None:
        return None
    elif root["left"] is None:
        return root
    else:
        return get_min_node(root["left"])

def get_min(my_bst):
    return get_min_node(my_bst['root'])

def get_max_node(root):
    if root is None:
        return None
    elif root["right"] is None:
        return root
    else:
        return get_max_node(root["right"])

def get_max(my_bst):
    return get_max_node(my_bst['root'])

def delete_min_node(root):
    if root is None:
        return None
    elif root["left"] is None:
        return root["right"]
    else:
        root["left"] = delete_min_node(root["left"])
        return root

def delete_min(my_bst):
    my_bst['root'] = delete_min_node(my_bst['root'])
    return my_bst






def delete_max_node(root):
    if root is None:
        return None
    elif root["right"] is None:
        return root["left"]
    else: 
        root["right"] = delete_max_node(root["right"])
        return root
    
def delete_max(my_bst):
    my_bst["root"] = delete_max_node(my_bst("root"))
    return my_bst



def height_node(root):
    if root is None:
        return 0
    left_height = height_node["left"]
    right_height = height_node["right"]
    
    return 1 + max(left_height, right_height)

def height(my_bst):
    return height_node(my_bst["root"])
        
    
def keys_range(root, key_initial, key_final, list_key):
    if root is None:
        return list_key
    
    key = root["key"]

    if key_initial < key:
        keys_range(root["left"], key_initial, key_final, list_key)
        
    if key_initial <= key <= key_final:
        sl.add_last(list_key, key)    
    
    if key < key_final:
        keys_range(root["right"], key_initial, key_final, list_key)
        
    return list_key

def keys(my_bst, key_initial, key_final):
    list_key = sl.new_list
    keys_range(my_bst["root"], key_initial, key_final, list_key)
    return list_key


def values_range(root, key_initial, key_final, list_key):
    if root is None:
        return list_key
    
    key = root["key"]

    if key_initial < key:
        values_range(root["left"], key_initial, key_final, list_key)
        
    if key_initial <= key <= key_final:
        sl.add_last(list_key, root["value"])    
    
    if key < key_final:
        values_range(root["right"], key_initial, key_final, list_key)    
        
    return list_key

def values(my_bst, key_initial, key_final):
    list_key = sl.new_list
    values_range(my_bst["root"], key_initial, key_final, list_key)
    return list_key
