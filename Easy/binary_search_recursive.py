def binary_search_recursive(a_list, item):
    """Performs recursive binary search of an integer in a given, sorted, list.
    a_list -- sorted list of integers
    item -- integer you are searching for the position of
    """
    first = 0
    last = len(a_list) - 1
    if len(a_list) == 0:
        return ' was not found in the list'.format(item=item)
    else:
        i = (first + last) // 2
        if item == a_list[i]:
            return ' found'.format(item=item)
        else:
            if a_list[i] < item:
                return binary_search_recursive(a_list[i+1:], item)
            else:
                return binary_search_recursive(a_list[:i], item)
            
binary_search_recursive([0,2,4,6,8,10],6)