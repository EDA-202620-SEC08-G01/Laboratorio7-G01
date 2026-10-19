
def default_compare(key, element):
    if key == bst.node.get_key(element):
        return 0
    elif key > bst.node.get_key(element):
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
    else:
        return get_node(root[key])
    
def get(my_bst, key):
    return get_node(my_bst, key)
    
     