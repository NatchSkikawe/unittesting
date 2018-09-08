def count_unique(list):
    """Count the number of distinct elements in a list.
    The list can contain any kind of elements, including duplicates and nulls in any order,
    (In PyDoc there are different formats for parameters and returns, Use what you prefer)
    :param list:  list of elements to find distinct elements of
    :return: the number of distinct elements in list
    Examples:
    >>> count_unique(['a','b','b','b','a','c','c'])
    3
    >>> count_unique(['a','a','a','a'])
    1
    >>> count_unique([ ])
    0
    >>> count_unique(['feels','sleepy','want','sleep'])
    4
    """
    a = set(list)
    return len(a)

def binary_search(list, element):
    """Searching the binary in the list.
       :param list: list of elements to find distinct elements of
              element: elements in the list that want to find
       :return: Return index of the matching element or "None" if the search element is not in the list
       Examples:
       >>> binary_search([1, 2, 3, 4], 1)
       0
       >>> binary_search([1, 2, 4, 5], 5)
       3
       >>> binary_search([1, 2, 4, 6], 0)
       'None'
       >>> binary_search([6, 2, 4, 1], 0)
       'None'
       >>> binary_search([], 5)
       'The list is empty'
       """
    list.sort()
    if element == None:
        raise TypeError("Search element must not be none")
    if len(list) == 0:
        return "The list is empty"


    lower = 0
    upper= len(list)
    while lower < upper:
        x = lower + (upper - lower) // 2
        if list[x] == element:
            return x
        elif element > list[x]:
            if lower == x:
              break
            lower = x
        elif element < list[x]:
            upper = x

    return "None"

