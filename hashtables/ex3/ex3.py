def intersection(arrays):
    """
    YOUR CODE HERE
    """
    _list = set(arrays[0])

    for i in range(len(arrays)):
        
        _list = list(set(_list) & set(arrays[i]))

    # result is a list of the intersecting values
    return _list

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))