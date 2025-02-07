# Python array or list

def run():
    my_arrays = [1, 3, 5, 2, 4]

    print("------------------------------------------------------------")
    print("Array:", my_arrays)
    print("First Index:", my_arrays[0])
    print("Last Index:", my_arrays[-1])
    print("Length of Array:", len(my_arrays))
    
    my_arrays.append(9)
    print("Add 9 to Array:", my_arrays)
    
    removed_value = my_arrays.pop(3)
    print("Pop 3rd Index of Array:", my_arrays, " -> Removed value:", removed_value)
    
    my_arrays.sort()
    print("Sort Array:", my_arrays)

    my_arrays.reverse()
    print("Reverse Array:", my_arrays)
    
    index = my_arrays.index(3)
    print("Index of value of 3:", index)

    # another_index = my_arrays.index(6) # Throws ValueError: 6 is not in list
    # print("Index of non existing value (6):", another_index)
    
    second_arrays = [15, 22, 13, 81]
    print("Second Array:", second_arrays)

    my_arrays.extend(second_arrays)
    print("Extend Aecond Array to Array:", my_arrays)
    
    my_arrays.clear()
    print("Clear Array:", my_arrays)
