
def negate(list_of_lists_of_numbers):
    return [
        [-item for item in t_list]
        for t_list in list_of_lists_of_numbers
    ]
