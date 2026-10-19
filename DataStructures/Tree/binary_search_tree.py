
from DataStructures.Tree import bst_node as bn
def insert_node (root, key,  value):
     if root is None:
         return bn.new_node(key,value)
         
    cmp= default_compare(key,root)
    
    if cmp == 0 :
         root["value"]= value
    elif cmp ==1 :
        insert_node(root["right"], ke, value)
    else:
         insert_node(root["left"], ke, value)    
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
        get_node(root["right"], key)
    else: 
        get_node(root["left"], key)
    
def get(my_bst, key):
    return get_node(my_bst, key)
    
     