# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    cache = {}
    listed_results = [] # Ends up being a nested list of outputs

    for path in files:
        
        # File_item is just the substring after the last '/'
        file_item = path.split('/')[-1]

        # ends up looking like: {'/foo' : '/bin/foo'}
        if file_item in cache:
            # If the file_item is already in cache we append to the list of values
            cache[file_item].append(path)
        else:
            # if the file_item isn't already in the cache we create an entry for it
            cache[file_item] = [path]


    for query in queries:

        if query in cache:
            listed_results.append(cache[query])

    # Make our nested lists into one list
    results = []

    for sublist in listed_results:
        for item in sublist:
            results.append(item)

    return results

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
