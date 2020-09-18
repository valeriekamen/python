def merge_lists(lists):
    new_list_dict = {}
    for l in lists:
        for item in l:
            if not item in new_list_dict:
                new_list_dict[item] = 1
            else:
                n = new_list_dict[item]
                new_list_dict[item] = n + 1
    print(new_list_dict)

    new_list = []
    for n in new_list_dict: 
        new_list.extend([n] * new_list_dict[n])
    
    print(new_list)

lists = [[1,4,5],[1,3,4],[2,6]]
tom = lists

merge_lists(lists)

"""
Cheating easy way with built in sort
def merge_lists(lists):
    new_list = []
    for l in lists:
        for item in l:
            new_list.append(item)

    new_list.sort()
    return new_list


Very inefficient

def where_it_goes(item, items_list):
    for i, l in enumerate(items_list):
        if item <= l:
            return i 
    return len(items_list)

def merge_lists(lists):
    new_list = []
    for l in lists:
        for item in l:
            pos = where_it_goes(item, new_list)
            new_list.insert(pos, item)

    print(new_list)
    return new_list

"""