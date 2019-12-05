def flatten(lst):
    flatten_list = sum(([x] if not isinstance(x, list) else flatten(x)
                        for x in lst), [])
    res: List[Any] = []
    for value in flatten_list:
        if value is not None:
            res.append(value)

    return res


# nested_list = [1, [2, 3, None, 4], [None], [5,[None, 6]], 7]
#
# print(flatten(nested_list))
