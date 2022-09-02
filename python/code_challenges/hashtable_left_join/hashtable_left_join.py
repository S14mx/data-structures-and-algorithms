

def left_join(hash1, hash2):
    join_list = []
    for _bucket in hash1._buckets:

        if _bucket is not None:
            join_list_key = [key for key in _bucket.head.value.keys()][0]
            join_list_value1 = hash1.get(
                join_list_key)
            if hash2.contains(join_list_key):
                join_list_value2 = hash2.get(
                    join_list_key)
            else:
                join_list_value2 = None
            join_list.append(
                [join_list_key, join_list_value1, join_list_value2])
    return join_list
