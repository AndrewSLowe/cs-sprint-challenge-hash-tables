# Weights is a list, length and limit are just integers

def get_indices_of_item_weights(weights, length, limit):
    """
    Answer: tuple with item indexes, sorted (higher, lower)
    """
    if length < 1:
        return None
    
    cache = {}

    for index, weight in enumerate(weights):

        cache[weight] = index

        target_weight = limit - weight
            
        if target_weight in cache:

            index_1 = cache.get(target_weight)
            index_2 = cache.get(weight)
            
            if index_1 != index_2:
                return (index_1, index_2) if index_1 >= index_2 else (index_2, index_1)

get_indices_of_item_weights([4, 4], 2, 8)   # doesn't pass test 2