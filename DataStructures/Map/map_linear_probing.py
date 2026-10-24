from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me
from DataStructures.List import array_list as al
import random as rd

EMPTY = "__EMPTY__"

def new_map(num_elements, load_factor, prime=109345121):

    capacity = mf.next_prime(num_elements / load_factor)
    scale = rd.randint(1, prime - 1)
    shift = rd.randint(0, prime - 1)

    table = al.new_list()
    for i in range(capacity):
        al.add_last(table, me.new_map_entry(None, None))

    hashtable = {
        "prime": prime,
        "capacity": capacity,
        "scale": scale,
        "shift": shift,
        "table": table,
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0,
    }
    return hashtable

def is_available (table, pos):
    entry = al.get_element(table, pos)
    key = me.get_key(entry)
    return key is None or key == EMPTY

def default_compare (key, entry):
    entry_key = me.get_key(entry)
    if key == entry_key:
        return 0
    elif key > entry_key:
        return 1
    else:
        return -1

def find_slot (hashtable, key):
    capacity = hashtable["capacity"]
    table = hashtable["table"]
    
    index = mf.hash_value(hashtable, key)
    first_avail = None
    visited = 0
    found_empty = False
    
    while visited < capacity and not found_empty:
        entry = al.get_element(table, index)
        if is_available(table, index):
            if first_avail is None:
                first_avail = index
            if me.get_key(entry) is None:
                found_empty = True
        elif default_compare(key, entry) == 0:
            return index
        visited += 1
        index = (index + 1) % capacity
    return -(first_avail + 1)
    
def rehash (hashtable):
    old_table = hashtable["table"]
    old_capacity = hashtable["capacity"]
    new_capacity = mf.next_prime(2 * old_capacity)
    new_table = al.new_list()
    for i in range(new_capacity):
        al.add_last(new_table, me.new_map_entry(None, None))
        
    hashtable["capacity"] = new_capacity
    hashtable["table"] = new_table

    for i in range(old_capacity):
        old_entry = al.get_element(old_table, i)
        key = me.get_key(old_entry)
        if key is not None and key != EMPTY:
            value = me.get_value(old_entry)
            index = mf.hash_value(hashtable, key)
            
            while not is_available(new_table, index):
                index = (index + 1) % new_capacity
            al.change_info(new_table, index, me.new_map_entry(key, value))
            
    hashtable["current_factor"] = hashtable["size"] / new_capacity
    return hashtable

def put (hashtable, key, value):
    capacity = hashtable["capacity"]
    table = hashtable["table"]
    
    index = find_slot(hashtable, key)
    if index >= 0:
        me.set_value(al.get_element(table, index), value)
        return hashtable
    
    index = -(index + 1)
    al.change_info(table, index, me.new_map_entry(key, value))
    hashtable["size"] += 1
    hashtable["current_factor"] = hashtable["size"] / capacity

    if hashtable["current_factor"] > hashtable["limit_factor"]:
        rehash(hashtable)
    return hashtable

def contains (hashtable, key):
    index = find_slot(hashtable, key)
    return index >= 0

def get (hashtable, key):
    index = find_slot(hashtable, key)
    if index >= 0:
        entry = al.get_element(hashtable["table"], index)
        return me.get_value(entry)
    return None

def remove (hashtable, key):
    index = find_slot(hashtable, key)
    if index >= 0:
        entry = al.get_element(hashtable["table"], index)
        me.set_key(entry, EMPTY)
        me.set_value(entry, None)
        hashtable["size"] -= 1
        hashtable["current_factor"] = hashtable["size"] / hashtable["capacity"]
    return hashtable

def size (hashtable):
    return hashtable["size"]

def is_empty (hashtable):
    return hashtable["size"] == 0

def key_set (hashtable):
    keys = al.new_list()
    for i in range(hashtable["capacity"]):
        entry = al.get_element(hashtable["table"], i)
        key = me.get_key(entry)
        if key is not None and key != EMPTY:
            al.add_last(keys, key)
    return keys

def value_set (hashtable):
    values = al.new_list()
    for i in range(hashtable["capacity"]):
        entry = al.get_element(hashtable["table"], i)
        key = me.get_key(entry)
        if key is not None and key != EMPTY:
            al.add_last(values, me.get_value(entry))
    return values

