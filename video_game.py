import csv
import sys

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory(lista):
    for key, value in lista.items():
        print(str(key)+" : "+str(value))


def display_inventory_ABC(list):
    inv2 = sorted(list.items())
    for key, value in inv2:
        print(str(key)+" : "+str(value))
    print('\n')


def display_inventory_sorted(list):
    sorted_inv = sorted(list.items(), key= lambda t:t[1])
    for key, value in reversed(sorted_inv):
      print(str(key)+" : "+str(value))


def display_inventory_sorted_Nice(list):
    sorted_inv = sorted(list.items(), key= lambda pair:pair[1])
    print('-'*20)
    print('{:>11} | {}'.format('item name','count'))
    print('-'*20)
    for key, value in reversed(sorted_inv):
      print('{:>11} | {:>5}'.format(str(key),str(value)))
    print('-'*20+'\n ')


def add_to_inventory(inventory, added_items):
    for item in added_items:
        item_value = inventory.get(item,0)+1
        inventory.update({item:item_value})


def add_to_inventory_steps(inventory, added_items):
    for item in added_items:
        if item in inventory:
            new_value = inventory.get(item)+1
            inventory.update({item:new_value})
        else:
            inventory.update({item:1})


def import_inventory(file):
    with open(file,'r') as file_for_read:
        reader = csv.reader(file_for_read)
        clear_items = []
        for i in reader:
            items = i
            for a in items:
                clear_items.append(a)
    return clear_items


def export_inventory(inventory, file):
    with open (file,'w+') as file_for_write:
        #the_writer= csv.writer(file_for_write)
        for k,v in inventory.items():
            file_for_write.write((k+',')*v)



display_inventory_ABC(inv)
add_to_inventory(inv, dragon_loot)
display_inventory_sorted_Nice(inv)
add_to_inventory(inv,import_inventory(sys.argv[1]))
display_inventory_sorted_Nice(inv)
export_inventory(inv,"export_inventory.csv")