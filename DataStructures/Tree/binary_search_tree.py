
from DataStructures.Tree import bst_node as bn

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
        get_node(root["right"], key)
    else: 
        get_node(root["left"], key)
    
def get(my_bst, key):
    return get_node(my_bst, key)
    
     