def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    results = []
    for i in a:

        cache[i] = i
        
        if i and -i in cache:
            if i > 0:
                results.append(i)
            else:
                results.append(-i)
        
    return results


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
