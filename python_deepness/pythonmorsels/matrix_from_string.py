
def matrix_from_string(string):
    """Convert string-based rows of numbers to list of lists."""

    t_list = [item.split(" ") for item in string.split("\n") if item.replace(" ", "")]
    r_list = []

    for index, item_list in enumerate(t_list):
        r_list.append([])
        for element in item_list:
            if element:
                element = element.replace(" ", "")
                r_list[index].append(float(element))

    return r_list
